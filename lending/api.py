# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import json

import frappe
from frappe import _
from frappe.utils import flt, getdate

from lending.loan_management.doctype.process_loan_security_shortfall.process_loan_security_shortfall import (
	create_process_loan_security_shortfall,
)


@frappe.whitelist()
def get_repayment_schedule(loan_product: str, loan_amount: float, rate_of_interest: float, tenure: int, repayment_frequency: str | None, repayment_start_date: str | None = None) -> list[dict]:
	"""
	API to get the repayment schedule for given loan product and repayment frequency
	"""

	repayment_schedule = frappe.new_doc("Loan Repayment Schedule")
	repayment_schedule.loan_product = loan_product
	repayment_schedule.repayment_frequency = repayment_frequency or "Monthly"
	repayment_schedule.repayment_method = "Repay Over Number of Periods"
	repayment_schedule.repayment_periods = tenure
	repayment_schedule.rate_of_interest = rate_of_interest
	repayment_schedule.posting_date = getdate()
	repayment_schedule.repayment_start_date = getdate(repayment_start_date)
	repayment_schedule.loan_amount = loan_amount
	repayment_schedule.current_principal_amount = loan_amount
	repayment_schedule.moratorium_tenure = 0
	repayment_schedule.moratorium_type = ""

	repayment_schedule.repayment_schedule_type = frappe.db.get_value("Loan Product", loan_product, "repayment_schedule_type")
	repayment_schedule.validate()

	response = {
		"loan_amount": repayment_schedule.loan_amount,
		"rate_of_interest": repayment_schedule.rate_of_interest,
		"tenure": tenure,
		"repayment_start_date": repayment_schedule.repayment_start_date,
		"repayment_periods": []
	}

	for row in repayment_schedule.get("repayment_schedule"):
		response["repayment_periods"].append({
			"payment_date": row.payment_date,
			"principal_amount": flt(row.principal_amount, 2),
			"interest_amount": flt(row.interest_amount, 2),
			"total_payment": flt(row.total_payment, 2),
			"balance_loan_amount": flt(row.balance_loan_amount, 2)
		})

	frappe.response["message"] = response

@frappe.whitelist()
def update_loan_security_price(data: dict):
	"""
	API to bulk update loan security price
	Note this API assumes only one record exists for updating loan securities
	"""

	frappe.has_permission("Loan Security Price", "write", throw=True)

	if isinstance(data, str):
		data = json.loads(data)

	for loan_security, price_details in data.items():
		frappe.db.set_value("Loan Security Price", {"loan_security": loan_security}, {
			"loan_security_price": price_details.get("loan_security_price"),
			"valid_from": price_details.get("valid_from"),
			"valid_upto": price_details.get("valid_upto")
		})

	create_process_loan_security_shortfall()
	frappe.response["message"] = _("Loan Security Prices updated successfully")

@frappe.whitelist()
def get_due_details(loan: str, as_on_date: str, loan_disbursement: str | None = None) -> dict:
	"""
	API to get due details for a given loan account as on a specific date
	"""

	from lending.loan_management.doctype.loan_repayment.loan_repayment import calculate_amounts

	amounts = calculate_amounts(loan, as_on_date, loan_disbursement=loan_disbursement)

	frappe.response["message"] = {
		"overdue_penalty_amount": amounts.get("penalty_amount"),
		"overdue_interest_amount": amounts.get("interest_amount"),
		"overdue_principal_amount": amounts.get("payable_principal_amount"),
		"principal_outstanding": amounts.get("pending_principal_amount"),
		"overdue_total_amount": amounts.get("payable_amount"),
		"applicable_future_interest": amounts.get("unaccrued_interest"),
		"unbooked_interest": amounts.get("unbooked_interest"),
		"applicable_future_penalty": amounts.get("unbooked_penalty"),
		"oldest_due_date": amounts.get("due_date"),
		"overdue_charges": amounts.get("total_charges_payable"),
		"available_security_deposit": amounts.get("available_security_deposit"),
		"written_off_amount": amounts.get("written_off_amount"),
		"excess_amount_paid": amounts.get("excess_amount_paid")
	}

@frappe.whitelist()
def apply_charge(loan: str, charge_type: str, based_on: str, percentage: float | None = None, amount: float | None = None, charge_applicable_date: str | None = None):
	from lending.loan_management.doctype.loan_demand.loan_demand import create_loan_demand
	from lending.loan_management.doctype.loan_disbursement.loan_disbursement import (
		make_sales_invoice_for_charge,
	)
	from lending.loan_management.doctype.loan_repayment.loan_repayment import (
		calculate_amounts,
		get_pending_principal_amount,
	)
	from lending.loan_management.utils import create_charge_master, loan_accounting_enabled

	create_charge_master(charge_type)

	if based_on == "On Outstanding Principal":
		loan_doc = frappe.get_doc("Loan", loan)
		pending_principal_amount = get_pending_principal_amount(loan_doc)
		charge_amount = (pending_principal_amount * percentage) / 100
	elif based_on == "On Total Payable Amount":
		payable_amount = calculate_amounts(loan, getdate(), payment_type="Loan Closure").get("payable_amount")
		charge_amount = (payable_amount * percentage) / 100
	elif based_on == "Flat":
		charge_amount = amount

	loan_details = frappe.db.get_value("Loan", loan, ["company", "applicant", "applicant_type"], as_dict=1)

	if loan_accounting_enabled(loan_details.company):
		charges = [
			{
				"charge": charge_type,
				"amount": charge_amount,
			}
		]
		make_sales_invoice_for_charge(loan, None, None, charge_type, charge_amount, charge_applicable_date, loan_details.company, charges)
	else:
		create_loan_demand(
			loan=loan,
			demand_date=getdate(charge_applicable_date),
			demand_type="Charges",
			demand_subtype=charge_type,
			amount=charge_amount,
		)

	frappe.response["message"] = _("Charge applied successfully for amount {0}").format(charge_amount)


def normalize_phone(phone_str):
	if not phone_str:
		return ""
	p = str(phone_str).strip().replace(" ", "").replace("-", "")
	if p.startswith("0"):
		return "+254" + p[1:]
	elif p.startswith("254"):
		return "+" + p
	elif not p.startswith("+"):
		return "+254" + p
	return p


@frappe.whitelist(allow_guest=True)
def check_borrower_status(identifier: str = None) -> dict:
	"""
	Check if a borrower (phone, email, or ID) is an existing customer with verified KYC.
	"""
	if not identifier:
		identifier = (frappe.form_dict.get("identifier") or (frappe.session.user if frappe.session.user != "Guest" else "") or "").strip()

	if not identifier:
		return {"exists": False}

	norm_phone = normalize_phone(identifier)

	apps = frappe.get_all(
		"Loan Application",
		or_filters=[
			{"applicant_phone_number": norm_phone} if norm_phone else {"name": ""},
			{"applicant_email_address": identifier.lower()},
			{"national_id_or_passport": identifier},
			{"kra_pin": identifier.upper()},
			{"owner": identifier}
		],
		fields=[
			"name", "applicant_name", "applicant_phone_number", "applicant_email_address",
			"national_id_or_passport", "kra_pin", "disbursal_method", "disbursal_mpesa_number",
			"disbursal_bank_name", "disbursal_account_number", "employer_or_business_name",
			"monthly_net_income", "status", "creation", "address_line_1", "state"
		],
		order_by="creation desc",
		limit=1
	)

	if apps:
		app = apps[0]
		raw_id = app.national_id_or_passport or ""
		masked_id = raw_id[:2] + "****" + raw_id[-2:] if len(raw_id) >= 4 else "****"
		raw_phone = app.applicant_phone_number or ""
		masked_phone = raw_phone[:4] + "***" + raw_phone[-3:] if len(raw_phone) >= 7 else "***"
		return {
			"exists": True,
			"applicant_name": app.applicant_name,
			"masked_id": masked_id,
			"masked_phone": masked_phone,
			"previous_application": app.name,
			"disbursal_method": app.disbursal_method or "M-Pesa",
			"disbursal_mpesa_number": app.disbursal_mpesa_number or "",
			"disbursal_bank_name": app.disbursal_bank_name or "",
			"disbursal_account_number": app.disbursal_account_number or "",
			"employer_or_business_name": app.employer_or_business_name or "",
			"monthly_net_income": flt(app.monthly_net_income),
			"address": app.address_line_1 or "",
			"county": app.state or "Nairobi",
			"status": app.status
		}

	return {"exists": False}


@frappe.whitelist(allow_guest=True)
def submit_loan_application(payload: str = None) -> dict:
	"""
	Public API to submit a loan application from the web form (both First-Time and Subsequent Loans).
	"""
	if not payload:
		payload = frappe.form_dict.get("payload") or frappe.local.form_dict

	if isinstance(payload, str):
		try:
			data = json.loads(payload)
		except Exception:
			data = frappe.form_dict
	elif isinstance(payload, dict):
		data = payload
	else:
		data = frappe.form_dict

	is_subsequent = int(data.get("is_subsequent_loan") or 0)
	prev_app_name = data.get("previous_loan_application")

	# If subsequent loan, attempt to populate KYC from previous application if omitted
	prev_app_doc = None
	if is_subsequent or prev_app_name or (frappe.session.user != "Guest"):
		user_identifier = frappe.session.user if frappe.session.user != "Guest" else (data.get("applicant_email_address") or data.get("applicant_phone_number"))
		if prev_app_name and frappe.db.exists("Loan Application", prev_app_name):
			prev_app_doc = frappe.get_doc("Loan Application", prev_app_name)
		elif user_identifier:
			norm_p = normalize_phone(data.get("applicant_phone_number"))
			prev_records = frappe.get_all(
				"Loan Application",
				or_filters=[
					{"owner": user_identifier},
					{"applicant_email_address": user_identifier},
					{"applicant_phone_number": norm_p} if norm_p else {"name": ""}
				],
				order_by="creation desc",
				limit=1
			)
			if prev_records:
				prev_app_doc = frappe.get_doc("Loan Application", prev_records[0].name)
				is_subsequent = 1
				prev_app_name = prev_app_doc.name

	# Normalize phone numbers
	applicant_phone = normalize_phone(data.get("applicant_phone_number") or (prev_app_doc.applicant_phone_number if prev_app_doc else ""))
	alt_phone = normalize_phone(data.get("alternative_phone_number") or (prev_app_doc.alternative_phone_number if prev_app_doc else ""))
	nok_phone = normalize_phone(data.get("next_of_kin_phone") or (prev_app_doc.next_of_kin_phone if prev_app_doc else ""))
	disb_phone = normalize_phone(data.get("disbursal_mpesa_number") or (prev_app_doc.disbursal_mpesa_number if prev_app_doc else "")) or applicant_phone
	guar_phone = normalize_phone(data.get("guarantor_phone") or (prev_app_doc.guarantor_phone if prev_app_doc else ""))
	work_phone = normalize_phone(data.get("work_phone") or (prev_app_doc.work_phone if prev_app_doc else ""))

	applicant_name = data.get("applicant_name") or (prev_app_doc.applicant_name if prev_app_doc else "")
	national_id = data.get("national_id_or_passport") or (prev_app_doc.national_id_or_passport if prev_app_doc else "")
	kra_pin = data.get("kra_pin") or (prev_app_doc.kra_pin if prev_app_doc else "")

	# Mandatory checks
	if not data.get("loan_product"):
		frappe.throw(_("Please select a Loan Product"))
	if not data.get("loan_amount") or flt(data.get("loan_amount")) <= 0:
		frappe.throw(_("Please enter a valid Loan Amount"))

	if not is_subsequent:
		required_fields = {
			"applicant_name": applicant_name,
			"national_id_or_passport": national_id,
			"kra_pin": kra_pin,
			"applicant_phone_number": applicant_phone
		}
		for field_k, field_v in required_fields.items():
			if not field_v:
				frappe.throw(_("Missing required field: {0}").format(frappe.unscrub(field_k)))
	else:
		if not applicant_name or not applicant_phone:
			frappe.throw(_("Missing borrower profile identification for subsequent loan"))

	company = frappe.db.get_single_value("Global Defaults", "default_company") or "Oryx Fund"

	# Find or Create Customer
	customer_name = None
	if prev_app_doc and prev_app_doc.applicant:
		customer_name = prev_app_doc.applicant

	if not customer_name:
		existing_customer = frappe.db.get_value("Customer", {"mobile_no": applicant_phone}, "name")
		if not existing_customer and kra_pin:
			existing_customer = frappe.db.get_value("Customer", {"tax_id": kra_pin}, "name")

		if existing_customer:
			customer_name = existing_customer
		else:
			cust_doc = frappe.new_doc("Customer")
			cust_doc.customer_name = applicant_name
			cust_doc.customer_type = "Individual"
			cust_doc.mobile_no = applicant_phone
			cust_doc.email_id = data.get("applicant_email_address") or (prev_app_doc.applicant_email_address if prev_app_doc else "")
			cust_doc.tax_id = kra_pin
			cust_doc.flags.ignore_mandatory = True
			cust_doc.save(ignore_permissions=True)
			customer_name = cust_doc.name

	# Create Loan Application
	app = frappe.new_doc("Loan Application")
	app.applicant_type = "Customer"
	app.applicant = customer_name
	app.applicant_name = applicant_name
	app.national_id_or_passport = national_id
	app.kra_pin = kra_pin
	app.date_of_birth = data.get("date_of_birth") or (prev_app_doc.date_of_birth if prev_app_doc else None)
	app.gender = data.get("gender") or (prev_app_doc.gender if prev_app_doc else "")
	app.residence_status = data.get("residence_status") or (prev_app_doc.residence_status if prev_app_doc else "Rented")
	app.company = company
	app.posting_date = getdate()

	app.applicant_email_address = data.get("applicant_email_address") or (prev_app_doc.applicant_email_address if prev_app_doc else "")
	app.applicant_phone_number = applicant_phone
	app.alternative_phone_number = alt_phone
	app.address_line_1 = data.get("address_line_1") or (prev_app_doc.address_line_1 if prev_app_doc else "")
	app.address_line_2 = data.get("address_line_2") or (prev_app_doc.address_line_2 if prev_app_doc else "")
	app.city = data.get("city") or (prev_app_doc.city if prev_app_doc else "")
	app.state = data.get("state") or (prev_app_doc.state if prev_app_doc else "")
	app.country = "Kenya"

	# Next of Kin
	app.next_of_kin_name = data.get("next_of_kin_name") or (prev_app_doc.next_of_kin_name if prev_app_doc else "")
	app.next_of_kin_relation = data.get("next_of_kin_relation") or (prev_app_doc.next_of_kin_relation if prev_app_doc else "")
	app.next_of_kin_phone = nok_phone

	# Disbursal
	app.disbursal_method = data.get("disbursal_method") or (prev_app_doc.disbursal_method if prev_app_doc else "M-Pesa")
	app.disbursal_mpesa_number = disb_phone
	app.disbursal_bank_name = data.get("disbursal_bank_name") or (prev_app_doc.disbursal_bank_name if prev_app_doc else "")
	app.disbursal_bank_branch = data.get("disbursal_bank_branch") or (prev_app_doc.disbursal_bank_branch if prev_app_doc else "")
	app.disbursal_account_number = data.get("disbursal_account_number") or (prev_app_doc.disbursal_account_number if prev_app_doc else "")
	app.disbursal_account_name = data.get("disbursal_account_name") or applicant_name

	# Employment & Income
	app.employment_status = data.get("employment_status") or (prev_app_doc.employment_status if prev_app_doc else "Permanent / Salaried")
	app.employer_or_business_name = data.get("employer_or_business_name") or (prev_app_doc.employer_or_business_name if prev_app_doc else "")
	app.job_title_or_nature_of_business = data.get("job_title_or_nature_of_business") or (prev_app_doc.job_title_or_nature_of_business if prev_app_doc else "")
	app.work_physical_address = data.get("work_physical_address") or (prev_app_doc.work_physical_address if prev_app_doc else "")
	app.work_phone = work_phone
	app.monthly_net_income = flt(data.get("monthly_net_income") or (prev_app_doc.monthly_net_income if prev_app_doc else 0))
	app.monthly_debt_obligations = flt(data.get("monthly_debt_obligations") or (prev_app_doc.monthly_debt_obligations if prev_app_doc else 0))
	app.monthly_fixed_expenses = flt(data.get("monthly_fixed_expenses") or (prev_app_doc.monthly_fixed_expenses if prev_app_doc else 0))
	app.net_disposable_income = max(0, app.monthly_net_income - (app.monthly_debt_obligations + app.monthly_fixed_expenses))

	# Guarantor
	app.guarantor_full_name = data.get("guarantor_full_name") or (prev_app_doc.guarantor_full_name if prev_app_doc else "")
	app.guarantor_national_id = data.get("guarantor_national_id") or (prev_app_doc.guarantor_national_id if prev_app_doc else "")
	app.guarantor_kra_pin = data.get("guarantor_kra_pin") or (prev_app_doc.guarantor_kra_pin if prev_app_doc else "")
	app.guarantor_phone = guar_phone
	app.guarantor_employer_or_business = data.get("guarantor_employer_or_business") or (prev_app_doc.guarantor_employer_or_business if prev_app_doc else "")
	app.guarantor_monthly_income = flt(data.get("guarantor_monthly_income") or (prev_app_doc.guarantor_monthly_income if prev_app_doc else 0))

	# Loan Specs
	app.loan_product = data.get("loan_product")
	app.loan_amount = flt(data.get("loan_amount"))
	app.repayment_periods = int(data.get("repayment_periods") or 1)
	app.loan_purpose = data.get("loan_purpose") or None

	# Subsequent Loan Tracking
	if is_subsequent:
		app.is_subsequent_loan = 1
		if prev_app_name:
			app.previous_loan_application = prev_app_name

	# Consent
	app.data_protection_consent = 1
	app.crb_authorization_consent = 1
	app.status = "Open"

	app.flags.ignore_permissions = True
	app.save(ignore_permissions=True)
	frappe.db.commit()

	success_msg = _("Express Subsequent Loan Application {0} submitted successfully! As a returning borrower, your application is fast-tracked.").format(app.name) if is_subsequent else _("Loan Application {0} submitted successfully! Our team will contact you shortly.").format(app.name)

	return {
		"status": "success",
		"name": app.name,
		"is_subsequent_loan": bool(is_subsequent),
		"applicant_name": app.applicant_name,
		"loan_amount": app.loan_amount,
		"loan_product": app.loan_product,
		"message": success_msg
	}


@frappe.whitelist(allow_guest=True)
def register_user(email: str, full_name: str, password: str = None, redirect_to: str = None):
	"""
	Direct production-ready borrower self-registration API.
	Creates user, sets credentials securely, and automatically establishes user session.
	"""
	email = (email or "").strip().lower()
	full_name = (full_name or "").strip()
	
	if not email or not frappe.utils.validate_email_address(email):
		frappe.throw(_("Please enter a valid email address."))
		
	if not full_name:
		frappe.throw(_("Full legal name is required."))
		
	if not password or len(password) < 6:
		frappe.throw(_("Password must be at least 6 characters long."))
		
	if frappe.db.exists("User", email):
		# Check if already active
		if frappe.db.get_value("User", email, "enabled"):
			frappe.throw(_("An account with {0} already exists. Please sign in.").format(email))
		else:
			frappe.throw(_("Your account is registered but currently inactive. Please contact support."))

	user = frappe.get_doc({
		"doctype": "User",
		"email": email,
		"first_name": full_name,
		"enabled": 1,
		"user_type": "Website User",
		"send_welcome_email": 0
	})
	user.flags.ignore_permissions = True
	user.flags.ignore_password_policy = True
	user.insert()

	# Set password securely
	from frappe.utils.password import update_password
	update_password(user=email, pwd=password)

	# Assign portal roles
	default_role = frappe.get_single_value("Portal Settings", "default_role") or "Customer"
	user.add_roles(default_role)

	# Log the user in directly
	frappe.local.login_manager.login_as(email)

	target = redirect_to or "/apply"
	return {
		"status": "success",
		"message": _("Account registered successfully! Redirecting..."),
		"redirect_to": target
	}


@frappe.whitelist()
def update_user_profile(payload):
	"""
	Whitelisted API for borrowers to update their profile and contact information.
	"""
	if frappe.session.user == "Guest":
		frappe.throw(_("Please log in to update your profile."))

	import json
	data = json.loads(payload) if isinstance(payload, str) else payload

	user_email = frappe.session.user
	user = frappe.get_doc("User", user_email)

	full_name = (data.get("full_name") or "").strip()
	if full_name:
		parts = full_name.split(" ", 1)
		user.first_name = parts[0]
		user.last_name = parts[1] if len(parts) > 1 else ""

	phone = (data.get("phone") or "").strip()
	if phone:
		user.phone = phone
		user.mobile_no = phone

	user.save(ignore_permissions=True)

	# Update Customer record if linked
	customer_name = frappe.db.get_value("Customer", {"email_id": user_email}, "name")
	if not customer_name:
		customer_name = frappe.db.get_value("Customer", {"customer_name": frappe.utils.get_fullname(user_email)}, "name")

	if customer_name:
		customer = frappe.get_doc("Customer", customer_name)
		if full_name:
			customer.customer_name = full_name
		if phone:
			customer.mobile_no = phone
		customer.save(ignore_permissions=True)

	# If there's a latest Loan Application submitted by this user, store custom contact / disbursal updates if necessary
	latest_app = frappe.get_all("Loan Application", filters={"owner": user_email}, order_by="creation desc", limit=1)
	if latest_app:
		app = frappe.get_doc("Loan Application", latest_app[0].name)
		if full_name:
			app.applicant_name = full_name
		app.save(ignore_permissions=True)

	return {
		"status": "success",
		"message": _("Profile details updated successfully!")
	}


@frappe.whitelist()
def update_user_password(old_password, new_password):
	"""
	Whitelisted API to allow borrowers to safely update their account password.
	"""
	if frappe.session.user == "Guest":
		frappe.throw(_("Please log in to change password."))

	if not new_password or len(new_password) < 6:
		frappe.throw(_("New password must be at least 6 characters long."))

	user_email = frappe.session.user

	# Verify old password
	from frappe.utils.password import check_password, update_password
	try:
		check_password(user_email, old_password)
	except Exception:
		frappe.throw(_("The current password entered is incorrect."))

	# Update password
	update_password(user=user_email, pwd=new_password)

	return {
		"status": "success",
		"message": _("Password changed successfully!")
	}
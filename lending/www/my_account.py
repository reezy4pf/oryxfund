import frappe
from frappe import _

def get_context(context):
    context.no_cache = 1
    context.title = "My Account — Oryx Fund"
    
    if frappe.session.user == "Guest":
        frappe.local.flags.redirect_location = "/login?redirect-to=/my_account"
        raise frappe.Redirect
        
    user_email = frappe.session.user
    user = frappe.get_doc("User", user_email)
    user_fullname = frappe.utils.get_fullname(user_email) or user.first_name or user_email
    
    context.user_email = user_email
    context.user_fullname = user_fullname
    context.user_phone = user.phone or user.mobile_no or ""
    context.creation_date = frappe.utils.format_date(user.creation)
    context.is_logged_in = True
    context.active_page = "account"
    
    first_name = "Account"
    if user.first_name:
        first_name = user.first_name.strip().capitalize()
    elif user_fullname and user_fullname != user_email:
        first_name = user_fullname.strip().split()[0].capitalize()
    context.first_name = first_name
    
    # Check customer details
    customer = frappe.db.get_value("Customer", {"email_id": user_email}, ["name", "mobile_no", "tax_id"], as_dict=True)
    if not customer:
        customer = frappe.db.get_value("Customer", {"customer_name": user_fullname}, ["name", "mobile_no", "tax_id"], as_dict=True)
        
    context.customer = customer
    
    # Check latest loan application KYC details
    latest_app = frappe.get_all(
        "Loan Application",
        or_filters=[{"owner": user_email}, {"applicant": customer.name if customer else user_email}],
        fields=["name", "applicant_name", "applicant_phone_number", "national_id_or_passport", "kra_pin", "address_line_1", "state", "gender", "date_of_birth", "employment_status", "employer_or_business_name", "disbursal_method", "disbursal_mpesa_number", "disbursal_bank_name", "disbursal_account_number"],
        order_by="creation desc",
        limit=1
    )
    
    kyc = {}
    if latest_app:
        kyc = latest_app[0]
        
    context.kyc = kyc
    context.national_id = kyc.get("national_id_or_passport") or ""
    context.kra_pin = kyc.get("kra_pin") or (customer.tax_id if customer else "") or ""
    context.phone = user.phone or user.mobile_no or kyc.get("applicant_phone_number") or ""
    context.address = kyc.get("address_line_1") or ""
    context.county = kyc.get("state") or "Nairobi"
    context.gender = kyc.get("gender") or "Not Specified"
    context.employment = kyc.get("employment_status") or "Not Specified"
    context.employer = kyc.get("employer_or_business_name") or ""
    context.disbursal_method = kyc.get("disbursal_method") or "M-Pesa Direct"
    context.disbursal_mpesa = kyc.get("disbursal_mpesa_number") or context.phone
    context.disbursal_bank = kyc.get("disbursal_bank_name") or ""
    context.disbursal_account = kyc.get("disbursal_account_number") or ""

    return context

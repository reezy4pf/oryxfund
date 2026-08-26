import frappe
from frappe.utils import flt

def get_context(context):
    context.no_cache = 1
    context.title = "Apply for a Loan — Oryx Fund"
    user_email = frappe.session.user
    context.is_logged_in = (user_email != "Guest")
    context.active_page = "apply"
    context.user_fullname = frappe.utils.get_fullname(user_email) if context.is_logged_in else ""
    context.user_email = user_email if context.is_logged_in else ""
    
    first_name = "Account"
    if context.is_logged_in:
        if context.user_fullname and context.user_fullname != user_email:
            first_name = context.user_fullname.strip().split()[0].capitalize()
        else:
            u_fn = frappe.db.get_value("User", user_email, "first_name")
            if u_fn:
                first_name = u_fn.strip().capitalize()
    context.first_name = first_name

    # Flow parameter: 'express' (default for returning), 'standard' (full form)
    flow_param = (frappe.form_dict.get("flow") or "").strip().lower()

    has_previous_application = False
    previous_app = None
    customer = None
    loan_count = 0

    if context.is_logged_in:
        # Check customer record
        customer_doc = frappe.db.get_value(
            "Customer",
            {"email_id": user_email},
            ["name", "customer_name", "mobile_no", "tax_id"],
            as_dict=True
        )
        if not customer_doc and context.user_fullname:
            customer_doc = frappe.db.get_value(
                "Customer",
                {"customer_name": context.user_fullname},
                ["name", "customer_name", "mobile_no", "tax_id"],
                as_dict=True
            )
        
        customer = customer_doc

        or_filters = [{"owner": user_email}]
        if customer_doc:
            or_filters.append({"applicant": customer_doc.name})

        # Query all historical loan applications
        previous_apps = frappe.get_all(
            "Loan Application",
            or_filters=or_filters,
            fields=[
                "name", "applicant", "applicant_name", "national_id_or_passport", "kra_pin",
                "applicant_email_address", "applicant_phone_number", "alternative_phone_number",
                "address_line_1", "address_line_2", "city", "state", "gender", "date_of_birth",
                "residence_status", "next_of_kin_name", "next_of_kin_relation", "next_of_kin_phone",
                "disbursal_method", "disbursal_mpesa_number", "disbursal_bank_name", "disbursal_bank_branch",
                "disbursal_account_number", "disbursal_account_name", "employment_status",
                "employer_or_business_name", "job_title_or_nature_of_business", "work_physical_address",
                "work_phone", "monthly_net_income", "monthly_debt_obligations", "monthly_fixed_expenses",
                "guarantor_full_name", "guarantor_national_id", "guarantor_kra_pin", "guarantor_phone",
                "guarantor_employer_or_business", "guarantor_monthly_income", "status", "creation",
                "loan_product", "loan_amount"
            ],
            order_by="creation desc",
            limit=1
        )

        if previous_apps:
            has_previous_application = True
            previous_app = previous_apps[0]
            
            # Count past loans/applications
            loan_count = len(frappe.get_all("Loan Application", or_filters=or_filters, pluck="name"))

    # Determine if express repeat loan UI should be active
    context.has_previous_application = has_previous_application
    context.previous_app = previous_app or {}
    context.customer = customer or {}
    context.loan_count = loan_count
    
    # If user has past applications and didn't explicitly request standard flow, use express flow
    if has_previous_application and flow_param != "standard":
        context.is_express_flow = True
    else:
        context.is_express_flow = False

    context.flow_param = flow_param

    # Masked ID and Phone for display
    if previous_app:
        raw_id = previous_app.get("national_id_or_passport") or ""
        context.masked_id = raw_id[:2] + "****" + raw_id[-2:] if len(raw_id) >= 4 else "****"
        raw_phone = previous_app.get("applicant_phone_number") or ""
        context.masked_phone = raw_phone[:4] + "***" + raw_phone[-3:] if len(raw_phone) >= 7 else "***"
    else:
        context.masked_id = ""
        context.masked_phone = ""

    # Available Loan Products & Purposes
    context.products = frappe.get_all(
        "Loan Product",
        filters={"disabled": 0},
        fields=["name", "product_name", "rate_of_interest", "maximum_loan_amount", "is_term_loan"]
    )
    context.purposes = frappe.get_all(
        "Loan Purpose",
        fields=["name", "loan_purpose"]
    )
    context.company = frappe.db.get_single_value("Global Defaults", "default_company") or "Oryx Fund"
    
    return context

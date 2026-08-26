import frappe
from frappe import _
from frappe.utils import flt

def get_context(context):
    context.no_cache = 1
    context.title = "My Portal — Oryx Fund"
    
    if frappe.session.user == "Guest":
        frappe.local.flags.redirect_location = "/login?redirect-to=/my_loans"
        raise frappe.Redirect
        
    user = frappe.session.user
    user_fullname = frappe.utils.get_fullname(user) or user
    context.user_fullname = user_fullname
    context.user_email = user
    context.is_logged_in = True
    context.active_page = "portal"
    
    first_name = "Account"
    if user_fullname and user_fullname != user:
        first_name = user_fullname.strip().split()[0].capitalize()
    else:
        u_fn = frappe.db.get_value("User", user, "first_name")
        if u_fn:
            first_name = u_fn.strip().capitalize()
    context.first_name = first_name
    
    customer = frappe.db.get_value("Customer", {"email_id": user}, "name")
    if not customer:
        customer = frappe.db.get_value("Customer", {"customer_name": user_fullname}, "name")
        
    context.customer = customer
    
    # Retrieve all applications for this user
    or_filters = [{"owner": user}]
    if customer:
        or_filters.append({"applicant": customer})

    applications = frappe.get_all(
        "Loan Application",
        or_filters=or_filters,
        fields=["name", "applicant_name", "loan_product", "loan_amount", "status", "posting_date", "repayment_periods"],
        order_by="creation desc"
    )
    context.applications = applications
    
    # Query approved/active loans
    loans = []
    if customer:
        loans = frappe.get_all(
            "Loan",
            filters={"applicant": customer, "docstatus": ["!=", 2]},
            fields=["name", "loan_product", "loan_amount", "status", "disbursement_date", "total_payment", "total_principal_paid", "total_interest_payable"],
            order_by="creation desc"
        )
    
    total_principal = 0.0
    total_outstanding = 0.0
    
    for l in loans:
        balance = frappe.db.get_value("Loan Repayment", {"loan": l.name, "docstatus": 1}, "sum(principal_paid)") or 0
        l.outstanding_principal = max(0, flt(l.loan_amount) - flt(balance))
        l.paybill_number = "400200"
        l.paybill_account = l.name
        total_principal += flt(l.loan_amount)
        total_outstanding += flt(l.outstanding_principal)
        
    context.loans = loans
    context.total_principal = total_principal
    context.total_outstanding = total_outstanding
    context.total_applications = len(applications)

    return context

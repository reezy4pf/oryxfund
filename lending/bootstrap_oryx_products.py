import frappe
from frappe.utils import flt

def setup():
    print("--- Bootstrapping Oryx Fund Setup ---")
    company_name = "Oryx Fund"
    
    # 1. Company Setup
    if not frappe.db.exists("Company", company_name):
        company = frappe.get_doc({
            "doctype": "Company",
            "company_name": company_name,
            "default_currency": "KES",
            "country": "Kenya"
        }).insert(ignore_permissions=True)
        print(f"Created Company: {company_name}")
    else:
        company = frappe.get_doc("Company", company_name)
        print(f"Found Company: {company_name}")
        
    frappe.db.set_single_value("Global Defaults", "default_company", company_name)
    frappe.db.set_single_value("Global Defaults", "default_currency", "KES")
    frappe.db.set_single_value("Global Defaults", "country", "Kenya")
    
    abbr = company.abbr
    
    # Helper to get or create Account
    def get_or_create_account(account_name, parent_account, root_type, account_type=None):
        full_name = f"{account_name} - {abbr}"
        if frappe.db.exists("Account", full_name):
            return full_name
        
        parent = f"{parent_account} - {abbr}" if not parent_account.endswith(f"- {abbr}") else parent_account
        if not frappe.db.exists("Account", parent):
            roots = frappe.get_all("Account", filters={"company": company_name, "root_type": root_type, "is_group": 1})
            parent = roots[0].name if roots else None
            
        if not parent:
            return None
            
        doc = frappe.get_doc({
            "doctype": "Account",
            "account_name": account_name,
            "company": company_name,
            "parent_account": parent,
            "root_type": root_type,
            "account_type": account_type or "",
            "account_currency": "KES"
        }).insert(ignore_permissions=True)
        print(f"Created Account: {doc.name}")
        return doc.name

    # 2. Key Accounts
    current_assets = frappe.db.get_value("Account", {"company": company_name, "account_name": "Current Assets", "is_group": 1}) or "Current Assets"
    bank_accounts = frappe.db.get_value("Account", {"company": company_name, "account_type": "Bank", "is_group": 1}) or current_assets
    income_group = frappe.db.get_value("Account", {"company": company_name, "account_name": "Direct Income", "is_group": 1}) or "Income"
    
    loan_asset_acc = get_or_create_account("Loans & Advances to Customers", current_assets, "Asset")
    mpesa_float_acc = get_or_create_account("M-Pesa Paybill Float", bank_accounts, "Asset", "Bank")
    interest_income_acc = get_or_create_account("Interest on Loans Income", income_group, "Income")
    fee_income_acc = get_or_create_account("Loan Processing Fees Income", income_group, "Income")
    penalty_income_acc = get_or_create_account("Late Payment Penalty Income", income_group, "Income")
    
    # 3. Modes of Payment
    for mop_name in ["M-Pesa", "Bank Transfer", "Cash"]:
        if not frappe.db.exists("Mode of Payment", mop_name):
            mop = frappe.get_doc({
                "doctype": "Mode of Payment",
                "mode_of_payment": mop_name,
                "type": "Bank" if mop_name != "Cash" else "Cash"
            }).insert(ignore_permissions=True)
            print(f"Created Mode of Payment: {mop_name}")
            
        mop_doc = frappe.get_doc("Mode of Payment", mop_name)
        has_company = any(row.company == company_name for row in mop_doc.accounts)
        if not has_company and mpesa_float_acc:
            mop_doc.append("accounts", {
                "company": company_name,
                "default_account": mpesa_float_acc
            })
            mop_doc.save(ignore_permissions=True)

    # 4. Loan Demand Offset Orders
    offset_order_name = "Standard Recovery Order"
    if not frappe.db.exists("Loan Demand Offset Order", offset_order_name):
        offset_doc = frappe.get_doc({
            "doctype": "Loan Demand Offset Order",
            "title": offset_order_name,
            "components": [
                {"demand_type": "Penalty"},
                {"demand_type": "Charges"},
                {"demand_type": "Interest"},
                {"demand_type": "Principal"}
            ]
        }).insert(ignore_permissions=True)
        print(f"Created Loan Demand Offset Order: {offset_order_name}")
    else:
        offset_doc = frappe.get_doc("Loan Demand Offset Order", offset_order_name)

    # Set offset on Company
    company_doc = frappe.get_doc("Company", company_name)
    company_doc.collection_offset_sequence_for_standard_asset = offset_order_name
    company_doc.collection_offset_sequence_for_sub_standard_asset = offset_order_name
    company_doc.save(ignore_permissions=True)

    # 5. Loan Purposes
    purposes = ["Working Capital", "Business Expansion", "Emergency Medical", "School Fees", "Asset Financing", "Personal Needs"]
    for p in purposes:
        if not frappe.db.exists("Loan Purpose", p):
            frappe.get_doc({"doctype": "Loan Purpose", "loan_purpose": p}).insert(ignore_permissions=True)
            print(f"Created Loan Purpose: {p}")

    # 6. Loan Products
    # Product 1: Oryx Short-Term Advance
    st_code = "Oryx Short-Term Advance"
    if not frappe.db.exists("Loan Product", st_code):
        st_prod = frappe.get_doc({
            "doctype": "Loan Product",
            "product_code": st_code,
            "product_name": st_code,
            "company": company_name,
            "is_term_loan": 0,
            "rate_of_interest": 12.0,
            "maximum_loan_amount": 500000.0,
            "penalty_interest_rate": 1.0,
            "grace_period_in_days": 3,
            "collection_offset_sequence_for_standard_asset": offset_order_name,
            "collection_offset_sequence_for_sub_standard_asset": offset_order_name,
            "disbursement_account": mpesa_float_acc,
            "payment_account": mpesa_float_acc,
            "loan_account": loan_asset_acc,
            "interest_income_account": interest_income_acc,
            "penalty_income_account": penalty_income_acc
        }).insert(ignore_permissions=True)
        print(f"Created Loan Product: {st_code}")

    # Product 2: Oryx Long-Term Term Loan
    lt_code = "Oryx Long-Term Term Loan"
    if not frappe.db.exists("Loan Product", lt_code):
        lt_prod = frappe.get_doc({
            "doctype": "Loan Product",
            "product_code": lt_code,
            "product_name": lt_code,
            "company": company_name,
            "is_term_loan": 1,
            "rate_of_interest": 18.0,
            "maximum_loan_amount": 5000000.0,
            "repayment_schedule_type": "Monthly as per repayment start date",
            "penalty_interest_rate": 0.5,
            "grace_period_in_days": 5,
            "collection_offset_sequence_for_standard_asset": offset_order_name,
            "collection_offset_sequence_for_sub_standard_asset": offset_order_name,
            "disbursement_account": mpesa_float_acc,
            "payment_account": mpesa_float_acc,
            "loan_account": loan_asset_acc,
            "interest_income_account": interest_income_acc,
            "penalty_income_account": penalty_income_acc
        }).insert(ignore_permissions=True)
        print(f"Created Loan Product: {lt_code}")

    frappe.db.commit()
    print("--- Bootstrapping Completed Successfully! ---")

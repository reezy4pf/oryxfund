import frappe

frappe.init(site="oryx.localhost", sites_path="sites")
frappe.connect()
frappe.set_user("Administrator")

# 1. Update Global Defaults
frappe.db.set_single_value("Global Defaults", "default_company", "Oryx Fund")
frappe.db.set_single_value("Global Defaults", "default_currency", "KES")
frappe.db.set_single_value("Global Defaults", "country", "Kenya")
frappe.db.sql("DELETE FROM `tabSingles` WHERE field LIKE '%demo_company%' OR value = 'Oryx Fund (Demo)'")

# 2. Clean User Permission and Company
frappe.db.sql("DELETE FROM `tabUser Permission` WHERE `for_value` = 'Oryx Fund (Demo)'")
frappe.db.sql("DELETE FROM `tabCompany` WHERE name = 'Oryx Fund (Demo)'")

frappe.db.commit()
print("Global Defaults updated & committed successfully.")

print("\n=== VERIFYING REMAINING COMPANIES ===")
for c in frappe.get_all("Company", fields=["name", "company_name", "default_currency"]):
    print(c)

print("\n=== VERIFYING REMAINING LOAN PRODUCTS ===")
for lp in frappe.get_all("Loan Product", fields=["name", "maximum_loan_amount", "rate_of_interest"]):
    print(lp)

print("\n=== VERIFYING REMAINING LOANS & APPLICATIONS ===")
print("Applications:", frappe.get_all("Loan Application", fields=["name", "applicant_name", "loan_amount", "status"]))
print("Loans:", frappe.get_all("Loan", fields=["name", "applicant", "loan_amount", "status"]))

print("\n=== VERIFYING REMAINING CUSTOMERS ===")
print("Customers:", frappe.get_all("Customer", fields=["name", "customer_name", "customer_type"]))

print("\n=== TOTAL TRANSACTION RECORDS (SHOULD BE CLEAN) ===")
for dt in ["Sales Invoice", "Purchase Invoice", "Sales Order", "Purchase Order", "Item", "Supplier"]:
    print(f"{dt}: {frappe.db.count(dt)}")

frappe.destroy()

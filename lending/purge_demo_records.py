import frappe

frappe.init(site="oryx.localhost", sites_path="sites")
frappe.connect()
frappe.set_user("Administrator")

print("Starting complete purge of remaining demo transactions...")

# 1. Delete all demo transactions
doctypes = [
    "Sales Invoice",
    "Purchase Invoice",
    "Sales Order",
    "Purchase Order",
    "Payment Entry",
    "Delivery Note",
    "Purchase Receipt",
    "Stock Entry",
    "Journal Entry",
    "Bank Transaction",
    "Payment Ledger Entry",
    "Stock Ledger Entry"
]

for dt in doctypes:
    if frappe.db.exists("DocType", dt):
        docs = frappe.get_all(dt, pluck="name")
        for d in docs:
            try:
                doc = frappe.get_doc(dt, d)
                if doc.docstatus == 1:
                    doc.cancel()
                doc.delete(ignore_permissions=True, force=True)
            except Exception:
                frappe.db.sql(f"DELETE FROM `tab{dt}` WHERE name = %s", d)
        count = frappe.db.count(dt)
        print(f"Purged {dt} -> Remaining: {count}")

# 2. Purge demo items
for i in range(1, 11):
    sku = f"SKU{i:03d}"
    if frappe.db.exists("Item", sku):
        try:
            frappe.delete_doc("Item", sku, force=True, ignore_permissions=True)
        except Exception:
            frappe.db.sql("DELETE FROM `tabItem` WHERE name = %s", sku)
print("Purged demo items -> Remaining Items:", frappe.db.count("Item"))

# 3. Purge demo suppliers
demo_suppliers = ["MA Inc.", "Summit Traders Ltd.", "Zuckerman Security Ltd."]
for sup in demo_suppliers:
    if frappe.db.exists("Supplier", sup):
        try:
            frappe.delete_doc("Supplier", sup, force=True, ignore_permissions=True)
        except Exception:
            frappe.db.sql("DELETE FROM `tabSupplier` WHERE name = %s", sup)
print("Purged demo suppliers -> Remaining Suppliers:", frappe.db.count("Supplier"))

# 4. Purge demo customers (keep only real borrower customers)
demo_customers = ["Palmer Productions Ltd.", "West View Software Ltd.", "Grant Plastics Ltd."]
for cust in demo_customers:
    if frappe.db.exists("Customer", cust):
        try:
            frappe.delete_doc("Customer", cust, force=True, ignore_permissions=True)
        except Exception:
            frappe.db.sql("DELETE FROM `tabCustomer` WHERE name = %s", cust)
print("Purged demo customers -> Remaining Customers:")
for c in frappe.get_all("Customer", fields=["name", "customer_name", "customer_type"]):
    print(" ", c)

# 5. Clean GL Entries (keep only Oryx Fund entries if any)
frappe.db.sql("DELETE FROM `tabGL Entry` WHERE company != 'Oryx Fund' OR voucher_type IN ('Sales Invoice', 'Purchase Invoice', 'Payment Entry')")
print("Remaining GL Entries:", frappe.db.count("GL Entry"))

frappe.db.commit()
print("All demo data purged and committed successfully!")

print("\n=== FINAL VERIFICATION ===")
print("Companies:", frappe.get_all("Company", fields=["name", "default_currency"]))
print("Loan Products:", frappe.get_all("Loan Product", fields=["name", "maximum_loan_amount", "rate_of_interest"]))
print("Loan Applications:", frappe.get_all("Loan Application", fields=["name", "applicant_name", "loan_amount", "status"]))
print("Loans:", frappe.get_all("Loan", fields=["name", "applicant", "loan_amount", "status"]))

frappe.destroy()

import frappe

frappe.init(site="oryx.localhost", sites_path="sites")
frappe.connect()
frappe.set_user("Administrator")

print("Starting Phase 3: Single Admin Account & Security Hardening...")

admin_email = "admin@oryxfund.co.ke"

# 1. Create or Update Oryx Fund Management Admin User
if frappe.db.exists("User", admin_email):
    admin_user = frappe.get_doc("User", admin_email)
    print(f"Updating existing Admin user: {admin_email}")
else:
    admin_user = frappe.new_doc("User")
    admin_user.email = admin_email
    admin_user.first_name = "Oryx Fund"
    admin_user.last_name = "Admin"
    print(f"Creating new Admin user: {admin_email}")

admin_user.user_type = "System User"
admin_user.enabled = 1
admin_user.send_welcome_email = 0
admin_user.module_profile = "Oryx Lending Management"

# Required roles for full Lending + Financial Management
management_roles = [
    "System Manager",
    "Desk User",
    "Loan Manager",
    "Loan Officer",
    "Loan Underwriter",
    "Loan Appraiser",
    "Loan Processor",
    "Loan LOS User",
    "Accounts Manager",
    "Accounts User",
    "Workspace Manager"
]

admin_user.roles = []
for r in management_roles:
    if frappe.db.exists("Role", r):
        admin_user.append("roles", {"role": r})

admin_user.save(ignore_permissions=True)

# Set password for admin@oryxfund.co.ke
from frappe.utils.password import update_password
update_password(admin_email, "OryxFundAdmin2026!")
print(f"Configured Admin: {admin_email} with full Management roles and password.")

# 2. Clean up obsolete test users
test_users_to_remove = ["reezyhoops2@gmail.com"]
for u in test_users_to_remove:
    if frappe.db.exists("User", u):
        try:
            frappe.delete_doc("User", u, force=True, ignore_permissions=True)
            print(f"Removed unused test account: {u}")
        except Exception as e:
            print(f"Could not remove {u}: {e}")

# 3. Ensure Borrower users have strict Website User / Customer roles
borrower_emails = ["reezy_trooper_test@oryxfund.co.ke", "reezyhoops@gmail.com"]
for b_email in borrower_emails:
    if frappe.db.exists("User", b_email):
        b_user = frappe.get_doc("User", b_email)
        b_user.user_type = "Website User"
        b_user.roles = []
        b_user.append("roles", {"role": "Customer"})
        b_user.save(ignore_permissions=True)
        print(f"Enforced Website User (Customer) role on borrower: {b_email}")

frappe.db.commit()
print("Phase 3 User Architecture & Security Hardening committed successfully!")

print("\n=== ACTIVE SYSTEM & WEBSITE USERS ===")
users = frappe.get_all("User", fields=["name", "email", "full_name", "user_type", "enabled"], filters={"enabled": 1})
for u in users:
    roles = [r.role for r in frappe.get_doc("User", u.name).roles]
    print(f"{u.user_type:15} | {u.email:35} | Roles: {roles}")

frappe.destroy()

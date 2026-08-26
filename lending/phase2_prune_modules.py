import frappe

frappe.init(site="oryx.localhost", sites_path="sites")
frappe.connect()
frappe.set_user("Administrator")

print("Starting Phase 2: Module Pruning & Desk Simplification...")

# 1. Create or Update Module Profile 'Oryx Lending Management'
profile_name = "Oryx Lending Management"
blocked_modules = [
    "Stock",
    "Manufacturing",
    "Buying",
    "Selling",
    "CRM",
    "Support",
    "Projects",
    "Quality Management",
    "Assets",
    "Subcontracting",
    "Maintenance",
    "Telephony",
    "EDI",
    "Bulk Transaction",
    "Regional",
    "Portal"
]

if frappe.db.exists("Module Profile", profile_name):
    mod_profile = frappe.get_doc("Module Profile", profile_name)
    mod_profile.block_modules = []
else:
    mod_profile = frappe.new_doc("Module Profile")
    mod_profile.module_profile_name = profile_name

for m in blocked_modules:
    mod_profile.append("block_modules", {"module": m})

mod_profile.save(ignore_permissions=True)
print(f"Created/Updated Module Profile: '{profile_name}' with {len(blocked_modules)} blocked modules.")

# 2. Hide all non-lending workspaces
workspaces_to_hide = [
    "Assets",
    "Buying",
    "CRM",
    "Manufacturing",
    "Projects",
    "Quality",
    "Selling",
    "Stock",
    "Subcontracting",
    "Support",
    "Welcome Workspace",
    "Build",
    "Home",
    "ERPNext Settings"
]

for ws_name in workspaces_to_hide:
    if frappe.db.exists("Workspace", ws_name):
        frappe.db.set_value("Workspace", ws_name, "is_hidden", 1)
        frappe.db.set_value("Workspace", ws_name, "public", 0)
        print(f"Hidden Workspace: {ws_name}")

# 3. Ensure Lending, Invoicing/Accounts, Users, Website, Integrations are visible & public
workspaces_to_keep = {
    "Lending": {"sequence_id": 1, "is_hidden": 0, "public": 1},
    "Invoicing": {"sequence_id": 2, "is_hidden": 0, "public": 1, "title": "Accounting & M-Pesa"},
    "Financial Reports": {"sequence_id": 3, "is_hidden": 0, "public": 1, "title": "Financial Ledgers"},
    "Users": {"sequence_id": 4, "is_hidden": 0, "public": 1, "title": "Users & Permissions"},
    "Website": {"sequence_id": 5, "is_hidden": 0, "public": 1, "title": "Website Portal"},
    "Integrations": {"sequence_id": 6, "is_hidden": 0, "public": 1, "title": "Integrations & APIs"}
}

for ws_name, conf in workspaces_to_keep.items():
    if frappe.db.exists("Workspace", ws_name):
        for k, v in conf.items():
            frappe.db.set_value("Workspace", ws_name, k, v)
        print(f"Configured Visible Workspace: {ws_name} -> {conf.get('title', ws_name)}")

# 4. Set Lending as default workspace in Website/Desk Settings if available
if frappe.db.exists("DocType", "Desk Settings"):
    frappe.db.set_single_value("Desk Settings", "default_workspace", "Lending")

frappe.db.commit()
print("Phase 2 Module Pruning & Desk Simplification committed successfully!")

print("\n=== VERIFYING ACTIVE PUBLIC WORKSPACES ===")
active_ws = frappe.get_all("Workspace", filters={"is_hidden": 0, "public": 1}, fields=["name", "title", "module", "sequence_id"], order_by="sequence_id asc")
for aws in active_ws:
    print(aws)

frappe.destroy()

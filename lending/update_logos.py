import frappe

def update_logos():
    print("--- Updating Global Logos in Frappe ---")
    
    # 1. Website Settings
    if frappe.db.exists("DocType", "Website Settings"):
        ws = frappe.get_doc("Website Settings")
        ws.app_logo = "/files/oryx_logo_light.png"
        ws.banner_html = ""
        ws.brand_html = '<img src="/files/oryx_logo_light.png" alt="Oryx Fund" class="oryx-nav-logo" style="height: 42px; max-height: 46px; width: auto; object-fit: contain;">'
        ws.splash_image = "/files/oryx_logo_dark.png"
        ws.favicon = "/files/oryx_logo_dark.png"
        ws.app_name = "Oryx Fund"
        ws.copyright = "© Oryx Fund Limited"
        ws.save(ignore_permissions=True)
        print("Updated Website Settings")

    # 2. Navbar Settings
    if frappe.db.exists("DocType", "Navbar Settings"):
        ns = frappe.get_doc("Navbar Settings")
        ns.app_logo = "/files/oryx_logo_dark.png"
        ns.save(ignore_permissions=True)
        print("Updated Navbar Settings")

    # 3. System Settings
    frappe.db.set_single_value("System Settings", "app_name", "Oryx Fund")
    
    # 4. Company Logo
    if frappe.db.exists("Company", "Oryx Fund"):
        comp = frappe.get_doc("Company", "Oryx Fund")
        comp.company_logo = "/files/oryx_logo_light.png"
        comp.save(ignore_permissions=True)
        print("Updated Company Oryx Fund Logo")

    frappe.db.commit()
    print("--- Global Logo Update Finished! ---")

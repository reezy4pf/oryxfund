import frappe
import json

def update_workspace():
    print("--- Updating Lending Workspace ---")
    if not frappe.db.exists("Workspace", "Lending"):
        print("Workspace Lending not found")
        return
        
    ws = frappe.get_doc("Workspace", "Lending")
    
    # Reset shortcuts
    ws.set("shortcuts", [])
    
    shortcuts_data = [
        {
            "label": "Open Applications",
            "type": "DocType",
            "link_to": "Loan Application",
            "color": "Green",
            "format": "{} Open",
            "stats_filter": json.dumps({"status": "Open"}),
            "doc_view": "List"
        },
        {
            "label": "Approved (Pending Loan)",
            "type": "DocType",
            "link_to": "Loan Application",
            "color": "Yellow",
            "format": "{} Approved",
            "stats_filter": json.dumps({"status": "Approved"}),
            "doc_view": "List"
        },
        {
            "label": "Active Loans",
            "type": "DocType",
            "link_to": "Loan",
            "color": "Green",
            "format": "{} Loans",
            "stats_filter": json.dumps({"status": ["!=", "Closed"]}),
            "doc_view": "List"
        },
        {
            "label": "Disbursements",
            "type": "DocType",
            "link_to": "Loan Disbursement",
            "color": "Grey",
            "doc_view": "List"
        },
        {
            "label": "Record Repayment",
            "type": "DocType",
            "link_to": "Loan Repayment",
            "color": "Green",
            "doc_view": "List"
        },
        {
            "label": "Borrowers (Customers)",
            "type": "DocType",
            "link_to": "Customer",
            "color": "Grey",
            "doc_view": "List"
        }
    ]
    
    for s in shortcuts_data:
        ws.append("shortcuts", s)
    
    # Clean up content JSON
    content_blocks = [
        {"id": "header_shortcuts", "type": "header", "data": {"text": "<span class=\"h4\"><b>Lending Operations Pipeline</b></span>", "col": 12}},
        {"id": "sc_open", "type": "shortcut", "data": {"shortcut_name": "Open Applications", "col": 4}},
        {"id": "sc_approved", "type": "shortcut", "data": {"shortcut_name": "Approved (Pending Loan)", "col": 4}},
        {"id": "sc_active", "type": "shortcut", "data": {"shortcut_name": "Active Loans", "col": 4}},
        {"id": "sc_disb", "type": "shortcut", "data": {"shortcut_name": "Disbursements", "col": 4}},
        {"id": "sc_repay", "type": "shortcut", "data": {"shortcut_name": "Record Repayment", "col": 4}},
        {"id": "sc_cust", "type": "shortcut", "data": {"shortcut_name": "Borrowers (Customers)", "col": 4}},
        {"id": "spacer_1", "type": "spacer", "data": {"col": 12}},
        {"id": "header_masters", "type": "header", "data": {"text": "<span class=\"h4\"><b>Core Masters & Reports</b></span>", "col": 12}},
        {"id": "card_loans", "type": "card", "data": {"card_name": "Loan", "col": 4}},
        {"id": "card_disb_repay", "type": "card", "data": {"card_name": "Disbursement and Repayment", "col": 4}},
        {"id": "card_reports", "type": "card", "data": {"card_name": "Reports", "col": 4}}
    ]
    
    ws.content = json.dumps(content_blocks)
    ws.save(ignore_permissions=True)
    frappe.db.commit()
    print("--- Workspace Lending updated successfully! ---")

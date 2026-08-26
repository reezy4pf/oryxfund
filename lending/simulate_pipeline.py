import frappe
import json
from frappe.utils import flt, getdate
import lending.api as api

def simulate_pipeline():
    print("==================================================")
    print("   STARTING ORYX FUND END-TO-END PIPELINE TEST    ")
    print("==================================================")

    # 1. Simulate Web Form Submission
    test_payload = {
        "applicant_name": "James Mwangi Kariuki",
        "national_id_or_passport": "31849201",
        "kra_pin": "A019283746Z",
        "date_of_birth": "1990-05-14",
        "gender": "Male",
        "applicant_phone_number": "0712345678",
        "applicant_email_address": "james.mwangi@example.com",
        "address_line_1": "Kilimani, Argwings Kodhek Rd",
        "address_line_2": "House 4B, Green Court",
        "state": "Nairobi",
        "residence_status": "Rented",
        "next_of_kin_name": "Mary Wanjiku Mwangi",
        "next_of_kin_relation": "Spouse",
        "next_of_kin_phone": "0722334455",
        "loan_product": "Oryx Short-Term Advance",
        "loan_amount": 50000.0,
        "repayment_periods": 3,
        "loan_purpose": "Working Capital",
        "disbursal_method": "M-Pesa",
        "disbursal_mpesa_number": "0712345678",
        "employment_status": "Permanent / Salaried",
        "employer_or_business_name": "Safaricom PLC",
        "job_title_or_nature_of_business": "Senior Systems Engineer",
        "work_physical_address": "HQ2, Waiyaki Way, Nairobi",
        "work_phone": "0204600000",
        "monthly_net_income": 85000.0,
        "monthly_debt_obligations": 10000.0,
        "monthly_fixed_expenses": 35000.0,
        "guarantor_full_name": "Peter Kamau Njoroge",
        "guarantor_national_id": "24859102",
        "guarantor_kra_pin": "A098765432X",
        "guarantor_phone": "0733112233",
        "guarantor_employer_or_business": "Kenya Airways",
        "guarantor_monthly_income": 95000.0
    }

    res = api.submit_loan_application(json.dumps(test_payload))
    app_id = res.get("name")
    print(f"Step 1: Public Submission Successful -> Application ID: {app_id}")

    # 2. Verify Application and Auto-Calculations
    app_doc = frappe.get_doc("Loan Application", app_id)
    print(f"Step 2: Applicant Name: {app_doc.applicant_name}")
    print(f"        Linked Customer: {app_doc.applicant}")
    print(f"        Monthly Net Income: KES {app_doc.monthly_net_income:,.2f}")
    print(f"        Monthly Fixed Expenses: KES {app_doc.monthly_fixed_expenses:,.2f}")
    print(f"        Net Disposable Income: KES {app_doc.net_disposable_income:,.2f}")
    assert flt(app_doc.net_disposable_income) == 40000.0, f"Expected 40,000, got {app_doc.net_disposable_income}"

    # 3. Manager Appraisal & Sanction
    app_doc.status = "Approved"
    app_doc.crb_status = "Clean / High Score"
    app_doc.crb_score_notes = "Metropol Score: 742/900. Affordability ratio well within 45% ceiling. Approved for full limit."
    app_doc.save(ignore_permissions=True)
    print(f"Step 3: Manager Appraisal Complete -> Status: {app_doc.status}, CRB: {app_doc.crb_status}")

    # 4. Generate Loan Record
    loan_doc = frappe.new_doc("Loan")
    loan_doc.applicant_type = "Customer"
    loan_doc.applicant = app_doc.applicant
    loan_doc.loan_application = app_doc.name
    loan_doc.loan_product = app_doc.loan_product
    loan_doc.loan_amount = app_doc.loan_amount
    loan_doc.rate_of_interest = app_doc.rate_of_interest
    loan_doc.repayment_periods = app_doc.repayment_periods
    loan_doc.repayment_method = "Repay Over Number of Periods"
    loan_doc.repayment_frequency = "Monthly"
    loan_doc.repayment_start_date = getdate()
    loan_doc.posting_date = getdate()
    loan_doc.company = app_doc.company
    loan_doc.save(ignore_permissions=True)
    print(f"Step 4: Loan Record Created -> Loan ID: {loan_doc.name}")

    # 5. Verify Print Formats Rendering
    html_agreement = frappe.get_print("Loan", loan_doc.name, print_format="Oryx Loan Agreement")
    print(f"Step 5a: Rendered 'Oryx Loan Agreement' ({len(html_agreement)} bytes)")
    assert "LOAN FACILITY AGREEMENT" in html_agreement, "Oryx Loan Agreement missing header"
    assert "James Mwangi Kariuki" in html_agreement, "Borrower name missing in agreement"

    html_appraisal = frappe.get_print("Loan Application", app_doc.name, print_format="Oryx Loan Appraisal Summary")
    print(f"Step 5b: Rendered 'Oryx Loan Appraisal Summary' ({len(html_appraisal)} bytes)")
    assert "APPLICANT IDENTIFICATION" in html_appraisal, "Appraisal sheet missing header"
    assert "742/900" in html_appraisal, "Underwriting notes missing in appraisal sheet"

    frappe.db.commit()
    print("==================================================")
    print("   ALL 5 SIMULATION STAGES PASSED FLAWLESSLY!    ")
    print("==================================================")

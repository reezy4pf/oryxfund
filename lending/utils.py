from datetime import date, timedelta

import frappe
from frappe.utils.user import is_website_user


def check_app_permission():
	if frappe.session.user == "Administrator":
		return True

	if is_website_user():
		return False

	return True


def get_home_page(user=None):
	if not user:
		user = frappe.session.user
	if not user or user == "Guest":
		return "/login"
	user_type = frappe.db.get_value("User", user, "user_type")
	if user_type == "System User":
		return "desk/dashboard-view/Loan Dashboard"
	return "my_loans"


def daterange(start_date: date, end_date: date):
	days = int((end_date - start_date).days)
	for n in range(days + 1):
		yield start_date + timedelta(n)


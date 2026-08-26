import os

file_path = "/workspace/frappe_docker/development/frappe-bench/apps/frappe/frappe/templates/includes/login/login.js"

with open(file_path, "r") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'var targetUrl = frappe.utils.sanitise_redirect(frappe.utils.get_url_arg("redirect-to")) || "/my_loans";' in line:
        new_lines.append('\t\t\tvar requestedRedirect = frappe.utils.sanitise_redirect(frappe.utils.get_url_arg("redirect-to"));\n')
        new_lines.append('\t\t\tvar targetUrl = requestedRedirect || data.home_page || "/my_loans";\n')
    elif 'window.location.href = targetUrl;' in line and 'Logged In' in ''.join(lines[max(0, len(new_lines)-10):len(new_lines)]):
        new_lines.append('\t\t\t\twindow.location.href = requestedRedirect || data.home_page || "/desk/dashboard-view/Loan Dashboard";\n')
    else:
        new_lines.append(line)

with open(file_path, "w") as f:
    f.writelines(new_lines)

print("Updated login.js successfully.")

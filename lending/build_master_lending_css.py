import os

def extract_style_block(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    if '<style>' in content and '</style>' in content:
        return content.split('<style>')[1].split('</style>')[0].strip()
    return ""

my_loans_css = extract_style_block('/home/reezy/.gemini/antigravity-ide/scratch/oryx_fund/lending/www/my_loans.html')
apply_css = extract_style_block('/home/reezy/.gemini/antigravity-ide/scratch/oryx_fund/lending/www/apply.html')
my_account_css = extract_style_block('/home/reezy/.gemini/antigravity-ide/scratch/oryx_fund/lending/www/my_account.html')

base_theme_and_tokens = """/* ==========================================================================
   Oryx Fund Design System & Global Theme
   Primary: #1F3224 (Deep Forest Green)
   Light Base: #EAE0D8 (Warm Sand Parchment)
   Dark Base: #0A0A0A (Obsidian Pitch Black)
   Dark Surface: #121A14 (Refined Emerald Obsidian)
   Secondary Accent: Sage #6E9B78
   Gold / Amber Accent: #FBBF24 / #C9A84C
   ========================================================================== */

/* ==========================================================================
   1. Light Mode Tokens & Variables
   ========================================================================== */
:root,
[data-theme="light"],
[data-theme-mode="light"],
html:not([data-theme="dark"]) body:not([data-theme="dark"]) {
  /* Global Background & Surfaces */
  --bg-color: #EAE0D8 !important;
  --bg-surface: #EAE0D8 !important;
  --body-bg: #EAE0D8 !important;
  --page-bg: #EAE0D8 !important;
  --neutral: #EAE0D8 !important;
  --subtle-accent: #e2d6cc !important;
  --subtle-fg: #d9ccbf !important;
  --navbar-bg: #EAE0D8 !important;
  --control-bg: #F5EFEA !important;
  --control-bg-on-gray: #e6dad0 !important;
  --sidebar-select-color: #ded1c5 !important;
  --border-color: #D1C5BA !important;
  --dark-border-color: #BDAEA1 !important;
  --table-border-color: #D8CCC1 !important;

  /* Card & Content Surfaces */
  --fg-color: #FFFFFF !important;
  --card-bg: #FFFFFF !important;
  --modal-bg: #FFFFFF !important;
  --popover-bg: #FFFFFF !important;
  --awesomebar-focus-bg: #FFFFFF !important;

  /* Brand Colors */
  --primary-color: #1F3224 !important;
  --primary: #1F3224 !important;
  --brand-primary: #1F3224 !important;
  --btn-primary: #1F3224 !important;
  --accent-color: #2F4D36 !important;
  --brand-secondary: #2F4D36 !important;
  --text-color: #121A14 !important;
  --heading-color: #1F3224 !important;
}

/* ==========================================================================
   2. Dark Mode Tokens & Variables
   ========================================================================== */
[data-theme="dark"],
[data-theme-mode="dark"],
html[data-theme="dark"],
body[data-theme="dark"],
html.dark,
body.dark,
[data-theme="dark"] body {
  /* Obsidian Forest Palette */
  --bg-color: #0A0A0A !important;
  --bg-surface: #0A0A0A !important;
  --body-bg: #0A0A0A !important;
  --page-bg: #0A0A0A !important;
  --neutral: #0A0A0A !important;
  --neutral-black: #050505 !important;
  --gray-900: #0A0A0A !important;
  --gray-800: #111412 !important;
  --gray-700: #1A221C !important;
  --gray-600: #223026 !important;
  --gray-500: #3E5A44 !important;
  --gray-400: #6E8B75 !important;
  --gray-300: #8BA291 !important;
  --gray-200: #B7C9BC !important;
  --gray-100: #E1EBE3 !important;
  --gray-50: #FAF8F5 !important;

  /* Surfaces & Containers */
  --fg-color: #121A14 !important;
  --fg-hover-color: #16241B !important;
  --card-bg: #121A14 !important;
  --surface-cards: #121A14 !important;
  --surface-menu-bar: #0A0A0A !important;
  --surface-modal: #121A14 !important;
  --surface-selected: #182C1E !important;
  --subtle-accent: #152219 !important;
  --subtle-fg: #1B2A20 !important;
  --modal-bg: #121A14 !important;
  --toast-bg: #121A14 !important;
  --popover-bg: #121A14 !important;
  --control-bg: #0E1410 !important;
  --control-bg-on-gray: #121A14 !important;
  --disabled-control-bg: #090B0A !important;
  --awesomebar-focus-bg: #0E1410 !important;
  --awesomplete-hover-bg: #16241B !important;

  /* Blue Variable Overrides (Prevent blue flashes) */
  --blue-50: #0E1A12 !important;
  --blue-100: #14281A !important;
  --blue-200: #1C3B26 !important;
  --blue-300: #264E33 !important;
  --blue-400: #326341 !important;
  --blue-500: #1F3224 !important;
  --blue-600: #182C1E !important;
  --blue-700: #122417 !important;
  --blue-800: #0D1C12 !important;
  --blue-900: #08120B !important;

  /* Borders */
  --border-color: #1E3023 !important;
  --dark-border-color: #2D4C35 !important;
  --table-border-color: #1C2B20 !important;
  --border-primary: #2D4C35 !important;
  --sidebar-border-color: #1A281E !important;
  --divider-color: #1C2B20 !important;
  --outline-gray-1: #1A281E !important;
  --outline-gray-2: #223628 !important;
  --outline-gray-3: #2E4A37 !important;

  /* Typography */
  --text-color: #FAF8F5 !important;
  --heading-color: #FFFFFF !important;
  --text-neutral: #FAF8F5 !important;
  --text-dark: #FFFFFF !important;
  --text-muted: #8FA693 !important;
  --text-light: #A8BDB0 !important;
  --disabled-text-color: #556B5C !important;
  --ink-gray-9: #FFFFFF !important;
  --ink-gray-8: #FAF8F5 !important;
  --ink-gray-7: #D6DFD8 !important;
  --ink-gray-6: #A8BDB0 !important;
  --ink-gray-5: #8FA693 !important;
  --ink-gray-4: #6B7C6E !important;
  --ink-gray-3: #4B5A4E !important;
  --ink-gray-2: #243228 !important;
  --ink-gray-1: #1A221C !important;

  /* Brand Accents */
  --primary-color: #1F3224 !important;
  --primary: #1F3224 !important;
  --brand-primary: #1F3224 !important;
  --btn-primary: #1F3224 !important;
  --accent-color: #2E5A36 !important;
  --brand-secondary: #2E5A36 !important;
}

/* ==========================================================================
   3. Global Authentication Page Styles
   ========================================================================== */
.for-login,
.for-signup,
.for-forgot,
.for-email-link {
  min-height: auto !important;
  padding: 0 !important;
}

.login-content.page-card,
.page-card {
  max-width: 440px !important;
  margin: 40px auto !important;
  padding: 32px 28px !important;
  border-radius: 16px !important;
  border: 1px solid #D1C5BA !important;
  background: #FFFFFF !important;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08) !important;
}

[data-theme="dark"] .login-content.page-card,
[data-theme="dark"] .page-card {
  background: #121A14 !important;
  border-color: #1E3023 !important;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6), 0 0 12px rgba(16, 185, 129, 0.06) !important;
}

.login-content .page-card-head {
  text-align: center !important;
  margin-bottom: 24px !important;
}

.login-content .app-logo {
  max-height: 48px !important;
  width: auto !important;
  margin-bottom: 12px !important;
}

.btn-login,
.login-content .btn-primary {
  background: #1F3224 !important;
  border: 1px solid #2E5A36 !important;
  color: #FAF8F5 !important;
  border-radius: 8px !important;
  font-weight: 600 !important;
  padding: 10px 16px !important;
  width: 100% !important;
  transition: all 0.18s ease !important;
}

.btn-login:hover,
.login-content .btn-primary:hover {
  background: #284431 !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25) !important;
}

/* Autofill Overrides */
input:-webkit-autofill,
input:-webkit-autofill:hover, 
input:-webkit-autofill:focus {
  -webkit-text-fill-color: #121A14 !important;
  -webkit-box-shadow: 0 0 0px 1000px #F5EFEA inset !important;
  transition: background-color 5000s ease-in-out 0s !important;
}

[data-theme="dark"] input:-webkit-autofill,
[data-theme="dark"] input:-webkit-autofill:hover, 
[data-theme="dark"] input:-webkit-autofill:focus {
  -webkit-text-fill-color: #FAF8F5 !important;
  -webkit-box-shadow: 0 0 0px 1000px #0E1410 inset !important;
}

/* ==========================================================================
   4. Universal 1080px Layout Wrappers
   ========================================================================== */
.oryx-portal-wrapper,
.oryx-apply-wrapper,
.oryx-account-wrapper {
  max-width: 1080px !important;
  margin: 20px auto 60px auto !important;
  padding: 0 16px !important;
  width: 100% !important;
  box-sizing: border-box !important;
}

/* Skeleton Preloaders */
.oryx-skeleton-wrapper {
  max-width: 1080px;
  margin: 20px auto;
  padding: 0 16px;
}

.oryx-skeleton-card {
  background: linear-gradient(90deg, #E2D7CD 25%, #EFE7E0 50%, #E2D7CD 75%);
  background-size: 200% 100%;
  animation: oryx-shimmer 1.5s infinite;
  border-radius: 12px;
}

[data-theme="dark"] .oryx-skeleton-card {
  background: linear-gradient(90deg, #121A14 25%, #18241C 50%, #121A14 75%);
  background-size: 200% 100%;
  animation: oryx-shimmer 1.5s infinite;
}

@keyframes oryx-shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

/* Stepper & Wizard Steps */
.form-step {
  display: none;
}

.form-step.active {
  display: block;
  animation: oryx-fadeIn 0.2s ease-out;
}

@keyframes oryx-fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

/* 2-Column Account Layout */
.account-grid {
  display: grid;
  grid-template-columns: 2fr 1.2fr;
  gap: 24px;
}

.form-grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

@media (max-width: 768px) {
  .account-grid {
    grid-template-columns: 1fr !important;
  }
  .form-grid-2 {
    grid-template-columns: 1fr !important;
    gap: 12px !important;
  }
}
"""

admin_desk_lux_css = """/* ==========================================================================
   5. Admin Desk Luxury Dark Mode & Customizations (Oryx Obsidian Forest)
   ========================================================================== */

/* Disable Onboarding popups, guides, and tours */
.onboarding-widget-box,
.desk-onboarding,
.onboarding-dialog,
.driver-popover,
[data-tour-id],
.desk-sidebar .sidebar-item-container:has(a[href*="getting-started"]),
.desk-sidebar a[href*="getting-started"] {
  display: none !important;
  visibility: hidden !important;
  pointer-events: none !important;
  opacity: 0 !important;
  height: 0 !important;
  max-height: 0 !important;
}

.desk-header {
  border-bottom: 1px solid #D8CCC1 !important;
}

[data-theme="dark"] .desk-header {
  border-bottom: 1px solid #1E2E22 !important;
}

/* Base Body & Main Section */
[data-theme="dark"],
[data-theme-mode="dark"],
html[data-theme="dark"],
body[data-theme="dark"] {
  background-color: #0A0A0A !important;
  color: #FAF8F5 !important;
}

[data-theme="dark"] .layout-main-section,
[data-theme="dark"] .page-container,
[data-theme="dark"] .desk-page,
[data-theme="dark"] .page-body,
[data-theme="dark"] .main-section {
  background-color: #0A0A0A !important;
}

/* ==========================================================================
   Page Head & Desk Navbar Architecture (Oryx Fund Luxury Admin)
   ========================================================================== */
.page-head {
  height: 52px !important;
  min-height: 52px !important;
  padding: 0 20px !important;
  display: flex !important;
  align-items: center !important;
  background-color: #0A0A0A !important;
  border-bottom: 1px solid #1E2E22 !important;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4) !important;
  z-index: 100 !important;
  transition: background-color 0.2s ease, border-color 0.2s ease !important;
}

[data-theme="light"] .page-head {
  background-color: #EAE0D8 !important;
  border-bottom: 1px solid #D8CCC1 !important;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04) !important;
}

.page-head .container,
.page-head .container-fluid,
.page-head .page-head-content {
  height: 100% !important;
  align-items: center !important;
  max-width: 100% !important;
  padding-left: 0 !important;
  padding-right: 0 !important;
  margin-left: 0 !important;
  margin-right: 0 !important;
}

.page-head .row.page-head-content,
.page-head .page-head-content {
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  width: 100% !important;
  margin-left: 0 !important;
  margin-right: 0 !important;
}

/* Page Title & Left Brand Section */
.page-title {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  margin: 0 !important;
  padding: 0 !important;
  flex: 1 !important;
  min-width: 0 !important;
}

.title-area {
  display: flex !important;
  align-items: center !important;
  flex: 1 !important;
  min-width: 0 !important;
}

/* Sidebar Toggle Icon / Hamburger Button */
.sidebar-toggle-btn {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 32px !important;
  height: 32px !important;
  min-width: 32px !important;
  border-radius: 8px !important;
  color: #8FA693 !important;
  background: transparent !important;
  border: 1px solid transparent !important;
  transition: all 0.15s ease !important;
  cursor: pointer !important;
  padding: 0 !important;
  margin-right: 6px !important;
  flex-shrink: 0 !important;
}

.sidebar-toggle-btn:hover {
  background: #142017 !important;
  border-color: #1E3023 !important;
  color: #34D399 !important;
}

[data-theme="light"] .sidebar-toggle-btn:hover {
  background: #DFD3C7 !important;
  border-color: #CFC1B4 !important;
  color: #1F3224 !important;
}

/* Breadcrumbs Styling */
.navbar-breadcrumbs {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  list-style: none !important;
  margin: 0 !important;
  padding: 0 !important;
  border: none !important;
  flex-wrap: nowrap !important;
  max-width: none !important;
}

.navbar-breadcrumbs li {
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
  font-size: 13.5px !important;
  letter-spacing: -0.01em !important;
  white-space: nowrap !important;
  margin: 0 !important;
  padding: 0 !important;
  max-width: none !important;
}

/* Reset default Frappe pseudo elements */
.navbar-breadcrumbs li::before,
.navbar-breadcrumbs li + li::before {
  display: none !important;
  content: "" !important;
}

/* Home icon link */
.navbar-breadcrumbs li:first-child a {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  color: #8FA693 !important;
  padding: 4px 6px !important;
  border-radius: 6px !important;
}

.navbar-breadcrumbs li:first-child a:hover {
  color: #34D399 !important;
  background: rgba(52, 211, 153, 0.1) !important;
}

/* Clean slash separator between items */
.navbar-breadcrumbs li:not(:last-child)::after {
  content: "/" !important;
  display: inline-block !important;
  color: #3E5A44 !important;
  font-size: 12px !important;
  font-weight: 400 !important;
  margin-left: 8px !important;
}

[data-theme="light"] .navbar-breadcrumbs li:not(:last-child)::after {
  color: #BDAEA1 !important;
}

.navbar-breadcrumbs a,
.navbar-breadcrumbs li a {
  color: #8FA693 !important;
  text-decoration: none !important;
  font-weight: 500 !important;
  transition: color 0.15s ease !important;
  padding: 2px 4px !important;
  border-radius: 4px !important;
  max-width: none !important;
}

.navbar-breadcrumbs li a:hover {
  color: #34D399 !important;
  background: rgba(52, 211, 153, 0.08) !important;
}

[data-theme="light"] .navbar-breadcrumbs li a {
  color: #557262 !important;
}

[data-theme="light"] .navbar-breadcrumbs li a:hover {
  color: #1F3224 !important;
  background: rgba(31, 50, 36, 0.06) !important;
}

.navbar-breadcrumbs li:last-child a,
.navbar-breadcrumbs li:last-child span,
.navbar-breadcrumbs li:last-child,
.navbar-breadcrumbs li.active a {
  color: #FAF8F5 !important;
  font-weight: 600 !important;
  pointer-events: auto !important;
}

[data-theme="light"] .navbar-breadcrumbs li:last-child a,
[data-theme="light"] .navbar-breadcrumbs li:last-child span,
[data-theme="light"] .navbar-breadcrumbs li:last-child,
[data-theme="light"] .navbar-breadcrumbs li.active a {
  color: #1F3224 !important;
}

/* Breadcrumb Home Icon */
.navbar-breadcrumbs li a svg,
.navbar-breadcrumbs li svg.icon-home {
  width: 14px !important;
  height: 14px !important;
  stroke: currentColor !important;
  fill: none !important;
}

/* Sidebar Header Brand (Top of Left Sidebar & App Switcher) */
.sidebar-header {
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  padding: 8px 12px !important;
  height: 52px !important;
  border-bottom: 1px solid #1A281E !important;
  text-decoration: none !important;
  background: transparent !important;
  border-radius: 10px !important;
  margin: 4px 6px !important;
  transition: all 0.15s ease !important;
}

[data-theme="light"] .sidebar-header {
  border-bottom: 1px solid #D8CCC1 !important;
}

.sidebar-header:hover,
.sidebar-header.hover,
.sidebar-header.active-sidebar {
  background-color: #121C15 !important;
}

[data-theme="light"] .sidebar-header:hover,
[data-theme="light"] .sidebar-header.hover,
[data-theme="light"] .sidebar-header.active-sidebar {
  background-color: #EFE8E1 !important;
}

/* Force removal of old green/gray background from Frappe sidebar item icon */
.sidebar-header .sidebar-item-icon,
.sidebar-header .sidebar-item-icon[style*="background-color"] {
  width: 34px !important;
  height: 34px !important;
  min-width: 34px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  border-radius: 8px !important;
  background-color: #121A14 !important;
  border: 1px solid #1E3023 !important;
  padding: 3px !important;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3) !important;
  transition: all 0.15s ease !important;
}

[data-theme="light"] .sidebar-header .sidebar-item-icon,
[data-theme="light"] .sidebar-header .sidebar-item-icon[style*="background-color"] {
  background-color: #FAF8F5 !important;
  border-color: #D8CCC1 !important;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05) !important;
}

.sidebar-header .header-logo {
  width: 26px !important;
  height: 26px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
}

.sidebar-header .header-logo svg,
.sidebar-header .sidebar-item-icon > svg {
  display: none !important;
}

.sidebar-header .header-logo img,
.sidebar-header img {
  height: 26px !important;
  width: 26px !important;
  max-width: 100% !important;
  object-fit: contain !important;
  border-radius: 4px !important;
}

.sidebar-header .title-container {
  display: flex !important;
  flex-direction: column !important;
  justify-content: center !important;
  line-height: 1.25 !important;
  flex: 1 !important;
  min-width: 0 !important;
}

.sidebar-header .header-title {
  font-size: 13.5px !important;
  font-weight: 700 !important;
  color: #FAF8F5 !important;
  letter-spacing: -0.01em !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
}

[data-theme="light"] .sidebar-header .header-title {
  color: #1F3224 !important;
}

.sidebar-header .header-subtitle {
  font-size: 11px !important;
  font-weight: 500 !important;
  color: #8FA693 !important;
  letter-spacing: 0.02em !important;
  white-space: nowrap !important;
  overflow: hidden !important;
  text-overflow: ellipsis !important;
}

[data-theme="light"] .sidebar-header .header-subtitle {
  color: #6B8573 !important;
}

.sidebar-header .drop-icon {
  color: #8FA693 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 0 !important;
  margin-left: auto !important;
  background: transparent !important;
  border: none !important;
  transition: transform 0.15s ease, color 0.15s ease !important;
}

.sidebar-header:hover .drop-icon {
  color: #34D399 !important;
}

[data-theme="light"] .sidebar-header .drop-icon {
  color: #557262 !important;
}

[data-theme="light"] .sidebar-header:hover .drop-icon {
  color: #1F3224 !important;
}

/* App Switcher Dropdown Menu */
.sidebar-header-menu,
.dropdown-menu.sidebar-header-menu {
  background-color: #0E1611 !important;
  border: 1px solid #1E3023 !important;
  border-radius: 12px !important;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6) !important;
  padding: 6px !important;
  backdrop-filter: blur(12px) !important;
}

[data-theme="light"] .sidebar-header-menu {
  background-color: #FAF8F5 !important;
  border-color: #D8CCC1 !important;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.08) !important;
}

.sidebar-header-menu .dropdown-menu-item a,
.sidebar-header-menu .dropdown-item {
  color: #FAF8F5 !important;
  border-radius: 8px !important;
  padding: 8px 12px !important;
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  transition: all 0.15s ease !important;
}

.sidebar-header-menu .dropdown-menu-item a:hover,
.sidebar-header-menu .dropdown-item:hover {
  background-color: #16241B !important;
  color: #34D399 !important;
}

[data-theme="light"] .sidebar-header-menu .dropdown-menu-item a,
[data-theme="light"] .sidebar-header-menu .dropdown-item {
  color: #1F3224 !important;
}

[data-theme="light"] .sidebar-header-menu .dropdown-menu-item a:hover,
[data-theme="light"] .sidebar-header-menu .dropdown-item:hover {
  background-color: #EFE8E1 !important;
  color: #1F3224 !important;
}

.sidebar-header-menu .sidebar-item-icon {
  background-color: #121A14 !important;
  border: 1px solid #1E3023 !important;
  border-radius: 6px !important;
  width: 28px !important;
  height: 28px !important;
  min-width: 28px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 2px !important;
}

.sidebar-header-menu .sidebar-item-icon img {
  height: 22px !important;
  width: 22px !important;
  object-fit: contain !important;
}

/* Collapsed Sidebar State (50px width) */
.body-sidebar:not(.expanded):not([style*="width: 220px"]):not([style*="width: 240px"]) .sidebar-header,
.desk-sidebar.collapsed:not(.expanded) .sidebar-header {
  padding: 8px !important;
  margin: 4px 2px !important;
  justify-content: center !important;
}

.body-sidebar:not(.expanded):not([style*="width: 220px"]):not([style*="width: 240px"]) .sidebar-header .title-container,
.desk-sidebar.collapsed:not(.expanded) .sidebar-header .title-container,
.body-sidebar:not(.expanded):not([style*="width: 220px"]):not([style*="width: 240px"]) .sidebar-header .drop-icon,
.desk-sidebar.collapsed:not(.expanded) .sidebar-header .drop-icon {
  display: none !important;
}

/* Expanded Sidebar State */
.body-sidebar.expanded .sidebar-header .title-container,
.body-sidebar.expanded .sidebar-header .drop-icon {
  display: flex !important;
}

.body-sidebar.expanded .sidebar-header .title-container {
  display: flex !important;
  flex-direction: column !important;
}

/* Right Header Actions Section */
.page-actions,
.standard-items-section,
.standard-actions {
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  flex: 0 0 auto !important;
  width: auto !important;
  flex-shrink: 0 !important;
}

/* Theme Toggle Button & More Menu Button */
.desk-theme-toggle,
.menu-more-button,
.page-head .btn.menu-more-button,
.page-head .btn.icon-btn,
.search-bar .navbar-modal-search-mobile {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 34px !important;
  height: 34px !important;
  min-width: 34px !important;
  border-radius: 8px !important;
  background: #142017 !important;
  border: 1px solid #223628 !important;
  color: #8FA693 !important;
  cursor: pointer !important;
  padding: 0 !important;
  margin: 0 !important;
  transition: all 0.18s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.25) !important;
  flex-shrink: 0 !important;
}

.desk-theme-toggle {
  color: #FBBF24 !important;
}

.desk-theme-toggle:hover {
  background: #1B2B20 !important;
  border-color: #34D399 !important;
  transform: translateY(-1px) scale(1.04) !important;
  box-shadow: 0 0 12px rgba(251, 191, 36, 0.25) !important;
}

.menu-more-button:hover,
.page-head .btn.menu-more-button:hover,
.page-head .btn.icon-btn:hover {
  background: #1B2B20 !important;
  border-color: #2D4C35 !important;
  color: #FAF8F5 !important;
  transform: translateY(-1px) !important;
}

[data-theme="light"] .desk-theme-toggle,
[data-theme="light"] .menu-more-button,
[data-theme="light"] .page-head .btn.menu-more-button,
[data-theme="light"] .page-head .btn.icon-btn,
[data-theme="light"] .search-bar .navbar-modal-search-mobile {
  background: #DFD3C7 !important;
  border: 1px solid #CFC1B4 !important;
  color: #1F3224 !important;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
}

[data-theme="light"] .desk-theme-toggle:hover,
[data-theme="light"] .menu-more-button:hover,
[data-theme="light"] .page-head .btn.menu-more-button:hover {
  background: #D3C5B7 !important;
  border-color: #BBAA9B !important;
  transform: translateY(-1px) scale(1.04) !important;
}

.search-bar {
  display: inline-flex !important;
  align-items: center !important;
}

/* Responsive Header Breakpoints */
@media (max-width: 1024px) {
  .page-head {
    padding: 0 16px !important;
  }
}

@media (max-width: 768px) {
  .page-head {
    height: 48px !important;
    min-height: 48px !important;
    padding: 0 12px !important;
  }

  .navbar-breadcrumbs li:not(:last-child) {
    display: none !important;
  }

  .navbar-breadcrumbs li:last-child {
    font-size: 13.5px !important;
    font-weight: 700 !important;
    border-left: none !important;
    margin-left: 0 !important;
    padding-left: 0 !important;
  }

  .navbar-breadcrumbs li::before,
  .navbar-breadcrumbs li::after {
    display: none !important;
    content: "" !important;
  }

  .page-actions {
    gap: 6px !important;
  }

  .desk-theme-toggle,
  .menu-more-button,
  .search-bar .navbar-modal-search-mobile {
    width: 32px !important;
    height: 32px !important;
    min-width: 32px !important;
    border-radius: 8px !important;
  }
}

@media (max-width: 480px) {
  .page-head {
    padding: 0 10px !important;
  }

  .page-title {
    gap: 6px !important;
  }

  .sidebar-toggle-btn {
    width: 28px !important;
    height: 28px !important;
    min-width: 28px !important;
    margin-right: 4px !important;
  }

  .navbar-breadcrumbs li:last-child {
    font-size: 13px !important;
  }

  .page-actions {
    gap: 4px !important;
  }

  .desk-theme-toggle,
  .menu-more-button,
  .search-bar .navbar-modal-search-mobile {
    width: 28px !important;
    height: 28px !important;
    min-width: 28px !important;
    border-radius: 6px !important;
  }

  .desk-theme-toggle svg,
  .menu-more-button svg,
  .search-bar svg {
    width: 15px !important;
    height: 15px !important;
  }
}

/* Desk Sidebar Base */
[data-theme="dark"] .desk-sidebar,
[data-theme="dark"] .layout-side-section,
[data-theme="dark"] .body-sidebar {
  background-color: #0B100D !important;
  border-right: 1px solid #1A281E !important;
}

[data-theme="dark"] .desk-sidebar .sidebar-section-header,
[data-theme="dark"] .desk-sidebar .standard-sidebar-section .section-header {
  color: #6E8B75 !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.08em !important;
  padding: 10px 14px 6px !important;
}

[data-theme="dark"] .standard-sidebar-item {
  color: #A3B8A7 !important;
  border-radius: 10px !important;
  transition: all 0.15s ease !important;
  margin: 2px 8px !important;
}

[data-theme="dark"] .standard-sidebar-item:hover {
  background-color: #142017 !important;
  color: #FAF8F5 !important;
  transform: translateX(2px) !important;
}

[data-theme="dark"] .standard-sidebar-item.selected,
[data-theme="dark"] .standard-sidebar-item.active,
[data-theme="dark"] .sidebar-item-container.active .standard-sidebar-item {
  background: linear-gradient(135deg, #182C1E 0%, #112015 100%) !important;
  border: 1px solid #2D4C35 !important;
  color: #FAF8F5 !important;
  font-weight: 600 !important;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.05) !important;
}

/* Dashboard Widgets & Number Cards */
[data-theme="dark"] .widget,
[data-theme="dark"] .dashboard-widget-box,
[data-theme="dark"] .number-card-widget,
[data-theme="dark"] .chart-widget-box {
  background: #121A14 !important;
  border: 1px solid #1E3023 !important;
  border-radius: 14px !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.04) !important;
  transition: transform 0.18s cubic-bezier(0.25, 0.46, 0.45, 0.94), border-color 0.18s ease, box-shadow 0.18s ease !important;
}

[data-theme="dark"] .widget:hover,
[data-theme="dark"] .dashboard-widget-box:hover {
  border-color: #2D4C35 !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 8px 28px rgba(0, 0, 0, 0.7), 0 0 14px rgba(16, 185, 129, 0.08) !important;
}

/* Ensure Dashboard Graph & Widget Group Body are Transparent */
.dashboard-graph,
.widget-group,
.widget-group-body,
.widget-group-body.grid-col-3,
.widget-group-body.grid-col-2,
[data-theme="dark"] .dashboard-graph,
[data-theme="dark"] .widget-group,
[data-theme="dark"] .widget-group-body,
[data-theme="dark"] .widget-group-body.grid-col-3,
[data-theme="dark"] .widget-group-body.grid-col-2 {
  background: transparent !important;
  background-color: transparent !important;
  border: none !important;
  box-shadow: none !important;
}

/* Mobile Breakpoint: Remove container background, padding, and borders for clean card stacks */
@media (max-width: 991px) {
  .widget-group-body.grid-col-3,
  .widget-group-body.grid-col-2,
  .widget-group-body,
  .widget-group,
  .dashboard-graph,
  [data-theme="dark"] .widget-group-body.grid-col-3,
  [data-theme="dark"] .widget-group-body.grid-col-2,
  [data-theme="dark"] .widget-group-body,
  [data-theme="dark"] .widget-group,
  [data-theme="dark"] .dashboard-graph {
    background: transparent !important;
    background-color: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
  }

  .widget.number-card-widget,
  [data-theme="dark"] .widget.number-card-widget {
    margin-bottom: 12px !important;
  }
}

[data-theme="dark"] .widget-head,
[data-theme="dark"] .widget-title,
[data-theme="dark"] .widget-title a {
  color: #8FA693 !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  letter-spacing: 0.02em !important;
}

[data-theme="dark"] .widget-body .number,
[data-theme="dark"] .widget-body .widget-number,
[data-theme="dark"] .number-card-widget .widget-number {
  color: #FAF8F5 !important;
  font-weight: 700 !important;
  font-family: inherit !important;
  font-variant-numeric: tabular-nums !important;
}

[data-theme="dark"] .widget-control .btn,
[data-theme="dark"] .widget-subtitle {
  color: #8FA693 !important;
}

/* List Views & Tables */
[data-theme="dark"] .list-row-container,
[data-theme="dark"] .result-list {
  background: #0E1410 !important;
  border: 1px solid #1C2B20 !important;
  border-radius: 12px !important;
  overflow: hidden !important;
}

[data-theme="dark"] .list-row-head {
  background: #141E17 !important;
  border-bottom: 1px solid #1F3324 !important;
  color: #8FA693 !important;
  font-size: 11px !important;
  font-weight: 700 !important;
  text-transform: uppercase !important;
  letter-spacing: 0.05em !important;
}

[data-theme="dark"] .list-row {
  background: #0E1410 !important;
  border-bottom: 1px solid #18241C !important;
  color: #FAF8F5 !important;
  transition: background-color 0.12s ease !important;
}

[data-theme="dark"] .list-row:hover {
  background: #16221A !important;
}

[data-theme="dark"] .list-row:last-child {
  border-bottom: none !important;
}

[data-theme="dark"] .list-item,
[data-theme="dark"] .list-row a {
  color: #FAF8F5 !important;
}

[data-theme="dark"] .list-item__content--muted {
  color: #8FA693 !important;
}

/* Form Views & Cards */
[data-theme="dark"] .form-card,
[data-theme="dark"] .form-page,
[data-theme="dark"] .form-section {
  background: #121A14 !important;
  border: 1px solid #1E3023 !important;
  border-radius: 12px !important;
}

[data-theme="dark"] .section-head {
  color: #8FA693 !important;
  font-weight: 700 !important;
  border-bottom: 1px solid #1C2B20 !important;
}

[data-theme="dark"] .frappe-control .form-control,
[data-theme="dark"] input.form-control,
[data-theme="dark"] select.form-control,
[data-theme="dark"] textarea.form-control {
  background-color: #0E1410 !important;
  border: 1px solid #223527 !important;
  color: #FAF8F5 !important;
  border-radius: 8px !important;
  transition: all 0.15s ease !important;
}

[data-theme="dark"] .frappe-control .form-control:focus,
[data-theme="dark"] input.form-control:focus,
[data-theme="dark"] select.form-control:focus,
[data-theme="dark"] textarea.form-control:focus {
  border-color: #34D399 !important;
  box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.18) !important;
  background-color: #121C15 !important;
}

[data-theme="dark"] .control-label,
[data-theme="dark"] .frappe-control label {
  color: #8FA693 !important;
  font-size: 12px !important;
  font-weight: 600 !important;
}

/* Form Message Banner & Alerts (High Specificity Overrides) */
[data-theme="dark"] .form-message,
[data-theme="dark"] .form-message.blue,
[data-theme="dark"] div.form-message.blue,
[data-theme="dark"] .form-message-container .form-message.blue,
[data-theme="dark"] .alert-info {
  background-color: #14281A !important;
  border-bottom: 1px solid #24462E !important;
  color: #34D399 !important;
  font-weight: 500 !important;
}

[data-theme="dark"] .form-message.yellow,
[data-theme="dark"] .form-message.orange,
[data-theme="dark"] div.form-message.yellow,
[data-theme="dark"] .alert-warning {
  background-color: #241E12 !important;
  border-bottom: 1px solid #3B2E1E !important;
  color: #FBBF24 !important;
}

[data-theme="dark"] .form-message.red,
[data-theme="dark"] div.form-message.red,
[data-theme="dark"] .alert-danger {
  background-color: #241212 !important;
  border-bottom: 1px solid #3B1E1E !important;
  color: #F87171 !important;
}

[data-theme="dark"] .form-message.green,
[data-theme="dark"] div.form-message.green,
[data-theme="dark"] .alert-success {
  background-color: #14281A !important;
  border-bottom: 1px solid #24462E !important;
  color: #34D399 !important;
}

/* Form Tabs & Headings */
[data-theme="dark"] .form-tabs-list .nav-link,
[data-theme="dark"] .form-tabs .nav-link {
  color: #8FA693 !important;
  border: none !important;
  transition: color 0.15s ease !important;
}

[data-theme="dark"] .form-tabs-list .nav-link.active,
[data-theme="dark"] .form-tabs .nav-link.active {
  color: #34D399 !important;
  border-bottom: 2px solid #34D399 !important;
  background: transparent !important;
  font-weight: 600 !important;
}

/* Form Sidebar (Meta / Timeline / Attachments) */
[data-theme="dark"] .form-sidebar,
[data-theme="dark"] .layout-side-section,
[data-theme="dark"] .form-sidebar-items {
  background-color: #0B100D !important;
  border-left: 1px solid #1A281E !important;
  color: #8FA693 !important;
}

[data-theme="dark"] .form-sidebar a,
[data-theme="dark"] .form-sidebar .sidebar-label,
[data-theme="dark"] .sidebar-action-btn {
  color: #8FA693 !important;
}

[data-theme="dark"] .form-sidebar a:hover,
[data-theme="dark"] .sidebar-action-btn:hover {
  color: #34D399 !important;
}

[data-theme="dark"] .form-sidebar .modified-by {
  color: #6E8B75 !important;
}

/* Primary Action Buttons (e.g. Submit, Save) */
[data-theme="dark"] .btn-primary,
[data-theme="dark"] .primary-action,
[data-theme="dark"] .btn-primary-dark,
[data-theme="dark"] button[data-label="Save"],
[data-theme="dark"] button[data-label="Submit"] {
  background: #1F3224 !important;
  border: 1px solid #2E5A36 !important;
  color: #FAF8F5 !important;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.05) !important;
}

[data-theme="dark"] .btn-primary:hover,
[data-theme="dark"] .primary-action:hover,
[data-theme="dark"] button[data-label="Save"]:hover,
[data-theme="dark"] button[data-label="Submit"]:hover {
  background: #284431 !important;
  border-color: #3B7246 !important;
  transform: translateY(-1px) !important;
}

[data-theme="dark"] .btn-default,
[data-theme="dark"] .btn-secondary {
  background: #141F17 !important;
  border: 1px solid #223628 !important;
  color: #FAF8F5 !important;
}

[data-theme="dark"] .btn-default:hover,
[data-theme="dark"] .btn-secondary:hover {
  background: #1A281E !important;
  border-color: #2E4C38 !important;
  color: #FFFFFF !important;
}

/* Modals & Dialogs */
[data-theme="dark"] .modal-content,
[data-theme="dark"] .msgprint-dialog .modal-content,
[data-theme="dark"] .frappe-control .form-control.awesomplete-dropdown {
  background-color: #121A14 !important;
  border: 1px solid #1E3324 !important;
  border-radius: 14px !important;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.8), 0 0 15px rgba(16, 185, 129, 0.08) !important;
}

[data-theme="dark"] .modal-header {
  border-bottom: 1px solid #1C2E21 !important;
}

[data-theme="dark"] .modal-footer {
  border-top: 1px solid #1C2E21 !important;
}

[data-theme="dark"] .modal-title {
  color: #FAF8F5 !important;
  font-weight: 700 !important;
}

/* Dropdown Menus & Popovers */
[data-theme="dark"] .dropdown-menu {
  background: #121A14 !important;
  border: 1px solid #223628 !important;
  border-radius: 10px !important;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7) !important;
}

[data-theme="dark"] .dropdown-item {
  color: #A3B8A7 !important;
}

[data-theme="dark"] .dropdown-item:hover,
[data-theme="dark"] .dropdown-item:focus {
  background: #18261D !important;
  color: #FAF8F5 !important;
}

/* Status Badges & Pills */
[data-theme="dark"] .indicator.green,
[data-theme="dark"] .indicator-pill.green {
  background: rgba(16, 185, 129, 0.15) !important;
  color: #34D399 !important;
  border: 1px solid rgba(16, 185, 129, 0.3) !important;
}

[data-theme="dark"] .indicator.orange,
[data-theme="dark"] .indicator-pill.orange,
[data-theme="dark"] .indicator.yellow {
  background: rgba(245, 158, 11, 0.15) !important;
  color: #FBBF24 !important;
  border: 1px solid rgba(245, 158, 11, 0.3) !important;
}

[data-theme="dark"] .indicator.red,
[data-theme="dark"] .indicator-pill.red {
  background: rgba(239, 68, 68, 0.15) !important;
  color: #F87171 !important;
  border: 1px solid rgba(239, 68, 68, 0.3) !important;
}

/* Desk Theme Switcher Button */
.desk-theme-toggle {
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  width: 34px !important;
  height: 34px !important;
  border-radius: 8px !important;
  background: #EAE0D8 !important;
  border: 1px solid #D1C5BA !important;
  color: #1F3224 !important;
  cursor: pointer !important;
  transition: all 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
  margin-right: 8px !important;
}

.desk-theme-toggle:hover {
  background: #D8CCC1 !important;
  transform: scale(1.05) !important;
}

[data-theme="dark"] .desk-theme-toggle {
  background: #16241B !important;
  border-color: #2D4C35 !important;
  color: #FBBF24 !important;
  box-shadow: 0 0 10px rgba(251, 191, 36, 0.15) !important;
}

[data-theme="dark"] .desk-theme-toggle:hover {
  background: #1F3324 !important;
  border-color: #3E6647 !important;
  box-shadow: 0 0 14px rgba(251, 191, 36, 0.25) !important;
}
"""

master_css = f"""{base_theme_and_tokens}

/* ==========================================================================
   PORTAL COMPONENT STYLES (/my_loans)
   ========================================================================== */
{my_loans_css}

/* ==========================================================================
   LOAN APPLICATION COMPONENT STYLES (/apply)
   ========================================================================== */
{apply_css}

/* ==========================================================================
   ACCOUNT MANAGEMENT COMPONENT STYLES (/my_account)
   ========================================================================== */
{my_account_css}

{admin_desk_lux_css}
"""

with open('/home/reezy/.gemini/antigravity-ide/scratch/oryx_fund/lending/public/css/lending.css', 'w') as f:
    f.write(master_css)

print(f"Master lending.css written successfully! Total size: {len(master_css)} bytes, {len(master_css.splitlines())} lines.")

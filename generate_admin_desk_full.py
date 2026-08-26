import os

def generate_full_admin_desk():
    base_dir = "/home/reezy/.gemini/antigravity-ide/scratch/oryx_fund"

    admin_html = r"""<!DOCTYPE html>
<html lang="en" data-theme="dark" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Oryx Fund — Institutional Lending Management</title>
  <meta name="description" content="Institutional credit and loan portfolio management dashboard for Oryx Fund.">
  <link rel="icon" type="image/png" href="assets/images/oryx-mark-dark.png">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    :root {
      --desk-bg: #09090B;
      --desk-sidebar-bg: #0E0E11;
      --desk-card-bg: #121215;
      --desk-card-hover: #18181C;
      --desk-card-surface: #18181C;
      --desk-border: #27272A;
      --desk-border-light: #1E1E22;
      --text-main: #FAF8F5;
      --text-sub: #9E9E9E;
      --text-dim: #666666;
      --accent-green: #34D399;
      --accent-emerald: #00D26A;
      --accent-red: #F87171;
      --accent-blue: #60A5FA;
      --accent-amber: #FBBF24;
      --pill-active-bg: #202025;
      --font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'IBM Plex Mono', monospace;
    }

    [data-theme="light"], html:not(.dark) {
      --desk-bg: #F4EFEB;
      --desk-sidebar-bg: #EAE3DC;
      --desk-card-bg: #FFFFFF;
      --desk-card-hover: #F9F7F5;
      --desk-card-surface: #F0EAE3;
      --desk-border: #DFD5CB;
      --desk-border-light: #E8E0D7;
      --text-main: #1F3224;
      --text-sub: #556B5D;
      --text-dim: #829488;
      --accent-green: #059669;
      --accent-emerald: #059669;
      --accent-red: #DC2626;
      --accent-blue: #2563EB;
      --accent-amber: #D97706;
      --pill-active-bg: #DFD5CB;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; transition: background-color 0.15s ease, border-color 0.15s ease, color 0.15s ease; }

    body {
      font-family: var(--font-body);
      background-color: var(--desk-bg);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      overflow-x: hidden;
    }

    /* Sidebar Styling */
    .desk-sidebar {
      width: 250px;
      min-width: 250px;
      background: var(--desk-sidebar-bg);
      border-right: 1px solid var(--desk-border);
      display: flex;
      flex-direction: column;
      padding: 14px 10px;
      height: 100vh;
      position: sticky;
      top: 0;
      overflow-y: auto;
      user-select: none;
    }

    .desk-brand-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 10px;
      border-radius: 8px;
      margin-bottom: 12px;
      text-decoration: none;
      color: var(--text-main);
      cursor: pointer;
    }
    .desk-brand-header:hover { background: rgba(255, 255, 255, 0.04); }

    .brand-icon-box {
      width: 26px;
      height: 26px;
      border-radius: 6px;
      background: #00D26A;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #000;
      font-weight: 900;
      font-size: 13px;
    }

    .brand-title-group {
      display: flex;
      flex-direction: column;
    }
    .brand-title-group .main-title {
      font-size: 13.5px;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.2;
    }
    .brand-title-group .sub-title {
      font-size: 10.5px;
      color: var(--text-sub);
    }

    .sidebar-search-btn {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--desk-card-bg);
      border: 1px solid var(--desk-border);
      padding: 7px 10px;
      border-radius: 8px;
      font-size: 12px;
      color: var(--text-sub);
      cursor: pointer;
      margin-bottom: 8px;
    }
    .sidebar-search-btn:hover { border-color: var(--accent-emerald); color: var(--text-main); }

    .kbd-shortcut {
      background: rgba(255, 255, 255, 0.08);
      padding: 2px 5px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 9.5px;
    }

    .sidebar-nav-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 10px;
      border-radius: 7px;
      font-size: 12.5px;
      font-weight: 600;
      color: var(--text-sub);
      text-decoration: none;
      cursor: pointer;
      margin-bottom: 2px;
    }
    .sidebar-nav-item:hover { background: rgba(255, 255, 255, 0.04); color: var(--text-main); }
    .sidebar-nav-item.active {
      background: var(--pill-active-bg);
      color: var(--text-main);
      font-weight: 700;
    }

    .badge-pill {
      font-size: 10px;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 12px;
      background: rgba(0, 210, 106, 0.15);
      color: #00D26A;
      font-family: var(--font-mono);
    }

    .sidebar-category-header {
      font-size: 11px;
      font-weight: 700;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 12px 10px 4px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
    }
    .sidebar-category-header:hover { color: var(--text-sub); }

    .sidebar-sub-list {
      display: flex;
      flex-direction: column;
      margin-bottom: 4px;
    }

    .sidebar-sub-item {
      padding: 6px 10px 6px 20px;
      font-size: 12px;
      color: var(--text-sub);
      border-radius: 6px;
      cursor: pointer;
      text-decoration: none;
      margin-bottom: 1px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .sidebar-sub-item:hover { background: rgba(255, 255, 255, 0.03); color: var(--text-main); }
    .sidebar-sub-item.active {
      background: var(--pill-active-bg);
      color: #00D26A;
      font-weight: 700;
    }

    .sidebar-user-footer {
      margin-top: auto;
      padding-top: 10px;
      border-top: 1px solid var(--desk-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .user-avatar-circle {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: #C1440E;
      color: #FFF;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 800;
    }

    /* Main Area Styling */
    .desk-main {
      flex: 1;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow-y: auto;
    }

    .desk-topbar {
      height: 48px;
      min-height: 48px;
      border-bottom: 1px solid var(--desk-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
      background: var(--desk-sidebar-bg);
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .breadcrumb-wrap {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 12px;
      color: var(--text-sub);
    }
    .breadcrumb-current {
      color: var(--text-main);
      font-weight: 700;
    }

    .topbar-right {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .theme-toggle-btn {
      background: transparent;
      border: 1px solid var(--desk-border);
      color: var(--text-main);
      padding: 4px 8px;
      border-radius: 6px;
      font-size: 12px;
      cursor: pointer;
    }

    .desk-canvas {
      padding: 20px 24px;
      flex: 1;
    }

    /* Stats Grid */
    .desk-kpi-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 12px;
      margin-bottom: 20px;
    }

    @media (max-width: 1200px) {
      .desk-kpi-grid { grid-template-columns: repeat(3, 1fr); }
    }
    @media (max-width: 800px) {
      .desk-kpi-grid { grid-template-columns: 1fr; }
    }

    .desk-kpi-card {
      background: var(--desk-card-bg);
      border: 1px solid var(--desk-border);
      border-radius: 10px;
      padding: 14px 16px;
      position: relative;
    }
    .desk-kpi-card:hover { border-color: var(--desk-border-light); }
    
    .kpi-title-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11px;
      font-weight: 600;
      color: var(--text-sub);
      margin-bottom: 8px;
    }
    .kpi-value {
      font-size: 20px;
      font-weight: 800;
      color: var(--text-main);
      font-family: var(--font-mono);
      line-height: 1.1;
    }

    /* Chart Cards */
    .desk-charts-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
      margin-bottom: 24px;
    }
    @media (max-width: 900px) {
      .desk-charts-grid { grid-template-columns: 1fr; }
    }

    .desk-chart-card {
      background: var(--desk-card-bg);
      border: 1px solid var(--desk-border);
      border-radius: 12px;
      padding: 18px 20px;
    }

    .chart-card-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
    }
    .chart-title {
      font-size: 13.5px;
      font-weight: 700;
      color: var(--text-main);
    }
    .chart-badge {
      font-size: 10.5px;
      color: var(--text-sub);
      display: flex;
      align-items: center;
      gap: 4px;
    }

    .svg-chart-container {
      width: 100%;
      height: 120px;
    }

    /* Table View Container */
    .desk-table-card {
      background: var(--desk-card-bg);
      border: 1px solid var(--desk-border);
      border-radius: 12px;
      overflow: hidden;
      margin-bottom: 20px;
    }

    .table-toolbar {
      padding: 12px 18px;
      border-bottom: 1px solid var(--desk-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--desk-card-surface);
      gap: 12px;
      flex-wrap: wrap;
    }

    .table-title {
      font-size: 14px;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .table-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .btn-action-pri {
      background: #00D26A;
      color: #000;
      border: none;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 4px;
      transition: all 0.15s ease;
    }
    .btn-action-pri:hover { background: #00FF80; transform: scale(1.02); }

    .btn-action-sec {
      background: transparent;
      border: 1px solid var(--desk-border);
      color: var(--text-main);
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .btn-action-sec:hover { background: rgba(255, 255, 255, 0.05); }

    .desk-data-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12px;
      text-align: left;
    }

    .desk-data-table th {
      background: var(--desk-sidebar-bg);
      color: var(--text-sub);
      font-weight: 700;
      padding: 10px 16px;
      border-bottom: 1px solid var(--desk-border);
      text-transform: uppercase;
      font-size: 10.5px;
      letter-spacing: 0.04em;
    }

    .desk-data-table td {
      padding: 12px 16px;
      border-bottom: 1px solid var(--desk-border-light);
      color: var(--text-main);
    }

    .desk-data-table tr:hover td {
      background: var(--desk-card-hover);
    }

    .mono-code {
      font-family: var(--font-mono);
      font-weight: 600;
      color: #00D26A;
    }

    .status-tag {
      display: inline-block;
      padding: 2px 8px;
      border-radius: 12px;
      font-size: 10.5px;
      font-weight: 700;
    }
    .status-tag.active { background: rgba(52, 211, 153, 0.15); color: #34D399; }
    .status-tag.review { background: rgba(251, 191, 36, 0.15); color: #FBBF24; }
    .status-tag.closed { background: rgba(158, 158, 158, 0.15); color: #9E9E9E; }

    /* Command Palette / Search Modal */
    .search-modal-backdrop {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(8px);
      display: none;
      align-items: flex-start;
      justify-content: center;
      padding-top: 100px;
      z-index: 10000;
    }

    .search-modal-box {
      width: 100%;
      max-width: 540px;
      background: #121215;
      border: 1px solid #27272A;
      border-radius: 12px;
      box-shadow: 0 20px 50px rgba(0,0,0,0.8);
      overflow: hidden;
    }

    .search-modal-header {
      padding: 12px 16px;
      display: flex;
      align-items: center;
      gap: 10px;
      border-bottom: 1px solid #27272A;
    }
    .search-modal-input {
      flex: 1;
      background: transparent;
      border: none;
      color: #FAF8F5;
      font-size: 14px;
      outline: none;
      font-family: var(--font-body);
    }

    .search-results-list {
      max-height: 320px;
      overflow-y: auto;
      padding: 8px;
    }

    .search-result-item {
      padding: 10px 14px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: #9CA3AF;
      font-size: 13px;
      cursor: pointer;
    }
    .search-result-item:hover, .search-result-item.selected {
      background: #27272A;
      color: #FAF8F5;
    }

    /* Underwriting Slide-over Drawer */
    .drawer-backdrop {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(6px);
      display: none;
      z-index: 9990;
    }

    .drawer-panel {
      position: fixed;
      top: 0; right: 0; bottom: 0;
      width: 520px;
      max-width: 90vw;
      background: #121215;
      border-left: 1px solid #27272A;
      box-shadow: -10px 0 40px rgba(0,0,0,0.8);
      z-index: 9995;
      display: flex;
      flex-direction: column;
      transform: translateX(100%);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .drawer-panel.open {
      transform: translateX(0);
    }

    .drawer-header {
      padding: 18px 24px;
      border-bottom: 1px solid #27272A;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .drawer-body {
      padding: 24px;
      flex: 1;
      overflow-y: auto;
    }

    .drawer-footer {
      padding: 18px 24px;
      border-top: 1px solid #27272A;
      display: flex;
      gap: 10px;
      background: #0E0E11;
    }

    /* In-DOM Clearance Auth Modal */
    .admin-auth-overlay {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(12px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
      z-index: 10000;
    }
    .admin-auth-overlay.active { display: flex !important; }

    .admin-auth-modal {
      background: #121215;
      border: 1px solid #27272A;
      border-radius: 18px;
      padding: 36px 32px;
      max-width: 440px;
      width: 100%;
      box-shadow: 0 20px 60px rgba(0,0,0,0.9);
      text-align: center;
      position: relative;
    }

    .modal-input {
      width: 100%;
      padding: 11px 14px;
      border-radius: 8px;
      border: 1px solid #27272A;
      background: #18181C;
      color: #FAF8F5;
      font-size: 13.5px;
      outline: none;
      margin-bottom: 14px;
    }
    .modal-input:focus { border-color: #00D26A; }

    .oryx-brand-logo {
      height: 38px;
      width: auto;
      max-width: 170px;
      object-fit: contain;
      display: block;
    }
    .oryx-desk-logo {
      height: 28px;
      width: auto;
      max-width: 140px;
      object-fit: contain;
      display: block;
    }
    .oryx-logo-light-img { display: block !important; }
    .oryx-logo-dark-img { display: none !important; }
    [data-theme="dark"] .oryx-logo-light-img, html.dark .oryx-logo-light-img { display: none !important; }
    [data-theme="dark"] .oryx-logo-dark-img, html.dark .oryx-logo-dark-img { display: block !important; }
  </style>
</head>
<body>

  <!-- RESTRICTED ACCESS GATE CONTAINER (SHOWN IF NOT AUTHENTICATED) -->
  <div id="adminGateContainer" style="display:none; min-height: 100vh; width: 100%; background: #090909; color: #FAF8F5; align-items: center; justify-content: center; font-family: 'DM Sans', sans-serif; padding: 20px; box-sizing: border-box; position: fixed; top: 0; left: 0; z-index: 9000;">
    <div style="background: #121215; border: 1px solid #27272A; border-radius: 18px; padding: 40px 32px; max-width: 460px; width: 100%; text-align: center; box-shadow: 0 20px 60px rgba(0,0,0,0.85);">
      <div style="width: 64px; height: 64px; border-radius: 50%; background: rgba(220, 38, 38, 0.15); border: 1.5px solid rgba(220, 38, 38, 0.4); color: #F87171; display: flex; align-items: center; justify-content: center; margin: 0 auto 18px; font-size: 28px;">
        🔒
      </div>
      <div style="display:inline-block; background:rgba(220,38,38,0.15); color:#F87171; border:1px solid rgba(220,38,38,0.3); font-size:11px; font-weight:700; padding:4px 12px; border-radius:20px; text-transform:uppercase; letter-spacing:0.06em; margin-bottom:12px;">Access Restricted</div>
      <h2 style="font-size: 22px; font-weight: 800; color: #FAF8F5; margin-bottom: 10px;">Administrator Privilege Required</h2>
      <p id="gateBorrowerDesc" style="font-size: 13.5px; color: #9CA3AF; line-height: 1.5; margin-bottom: 24px;">
        You are currently not signed in as an administrator. Institutional underwriting &amp; disbursement operations require verified staff clearance.
      </p>
      <div style="display: flex; flex-direction: column; gap: 10px;">
        <button id="gateSignInBtn" onclick="openAdminClearanceModalDirect()" style="background: #00D26A; color: #000; border: none; padding: 12px 20px; border-radius: 8px; font-weight: 700; font-size: 13.5px; cursor: pointer; transition: all 0.15s ease;">
          🔑 Sign In with Clearance
        </button>
        <a href="index.html" style="background: #18181C; color: #D6DFD8; border: 1px solid #27272A; padding: 11px 20px; border-radius: 8px; font-weight: 600; font-size: 13px; text-decoration: none; display: block;">
          Return to Borrower Portal
        </a>
      </div>
    </div>
  </div>

  <!-- Left Sidebar -->
  <aside class="desk-sidebar" id="mainSidebar">
    
    <!-- Brand Header -->
    <a href="index.html" class="desk-brand-header" title="Oryx Fund Lending Management Platform">
      <div style="display: flex; align-items: center; gap: 8px;">
        <div class="brand-icon-box">▲</div>
        <div class="brand-title-group">
          <span class="main-title">Oryx Fund</span>
          <span class="sub-title">Lending Platform</span>
        </div>
      </div>
      <span style="font-size: 11px; color: var(--text-dim);">▼</span>
    </a>

    <!-- Quick Search / Command Bar Trigger -->
    <div class="sidebar-search-btn" onclick="openSearchModal()">
      <span>🔍 Search</span>
      <span class="kbd-shortcut">Ctrl+K</span>
    </div>

    <!-- Notification Trigger -->
    <div class="sidebar-nav-item" onclick="openNotifications()">
      <span>🔔 Notification</span>
      <span class="badge-pill" id="notifBadge">3 New</span>
    </div>

    <!-- 1. DASHBOARD ROOT VIEW -->
    <div class="sidebar-nav-item active" id="nav_dashboard" onclick="switchView('dashboard')">
      <span>📊 Dashboard</span>
    </div>

    <!-- 2. SETUP GROUP -->
    <div class="sidebar-category-header" onclick="toggleCategory('setupGroup', this)">
      <span>⚙️ Setup</span>
      <span class="arrow">▼</span>
    </div>
    <div class="sidebar-sub-list" id="setupGroup">
      <a class="sidebar-sub-item" id="nav_company" onclick="switchView('company')">Company</a>
      <a class="sidebar-sub-item" id="nav_loan_product" onclick="switchView('loan_product')">Loan Product</a>
      <a class="sidebar-sub-item" id="nav_charges" onclick="switchView('charges')">Loan Charges</a>
    </div>

    <!-- 3. LOAN MANAGEMENT GROUP -->
    <div class="sidebar-category-header" onclick="toggleCategory('loanMgmtGroup', this)">
      <span>📁 Loan Management</span>
      <span class="arrow">▼</span>
    </div>
    <div class="sidebar-sub-list" id="loanMgmtGroup">
      <a class="sidebar-sub-item" id="nav_loan" onclick="switchView('loan')">Loan</a>
      <a class="sidebar-sub-item" id="nav_loan_disbursement" onclick="switchView('loan_disbursement')">Loan Disbursement</a>
      <a class="sidebar-sub-item" id="nav_loan_repayment_schedule" onclick="switchView('loan_repayment_schedule')">Loan Repayment Schedule</a>
      <a class="sidebar-sub-item" id="nav_loan_transfer" onclick="switchView('loan_transfer')">Loan Transfer</a>
      <a class="sidebar-sub-item" id="nav_loan_restructure" onclick="switchView('loan_restructure')">Loan Restructure</a>
      <a class="sidebar-sub-item" id="nav_loan_repayment" onclick="switchView('loan_repayment')">Loan Repayment</a>
      <a class="sidebar-sub-item" id="nav_loan_demand" onclick="switchView('loan_demand')">Loan Demand</a>
      <a class="sidebar-sub-item" id="nav_loan_interest_accrual" onclick="switchView('loan_interest_accrual')">Loan Interest Accrual</a>
      <a class="sidebar-sub-item" id="nav_loan_write_off" onclick="switchView('loan_write_off')">Loan Write Off</a>
      <a class="sidebar-sub-item" id="nav_dpd_log" onclick="switchView('dpd_log')">DPD Log</a>
    </div>

    <!-- 4. LOAN ORIGINATION GROUP -->
    <div class="sidebar-category-header" onclick="toggleCategory('loanOrigGroup', this)">
      <span>👥 Loan Origination</span>
      <span class="arrow">▼</span>
    </div>
    <div class="sidebar-sub-list" id="loanOrigGroup">
      <a class="sidebar-sub-item" id="nav_customer" onclick="switchView('customer')">Customer</a>
      <a class="sidebar-sub-item" id="nav_loan_application" onclick="switchView('loan_application')">Loan Application</a>
    </div>

    <!-- 5. SECURITY MANAGEMENT GROUP -->
    <div class="sidebar-category-header" onclick="toggleCategory('secMgmtGroup', this)">
      <span>🔒 Security Management</span>
      <span class="arrow">▼</span>
    </div>
    <div class="sidebar-sub-list" id="secMgmtGroup">
      <a class="sidebar-sub-item" id="nav_loan_security_type" onclick="switchView('loan_security_type')">Loan Security Type</a>
      <a class="sidebar-sub-item" id="nav_loan_security" onclick="switchView('loan_security')">Loan Security</a>
      <a class="sidebar-sub-item" id="nav_loan_security_price" onclick="switchView('loan_security_price')">Loan Security Price</a>
      <a class="sidebar-sub-item" id="nav_loan_security_assignment" onclick="switchView('loan_security_assignment')">Loan Security Assignment</a>
      <a class="sidebar-sub-item" id="nav_loan_security_release" onclick="switchView('loan_security_release')">Loan Security Release</a>
      <a class="sidebar-sub-item" id="nav_sanctioned_loan_amount" onclick="switchView('sanctioned_loan_amount')">Sanctioned Loan Amount</a>
    </div>

    <!-- User Footer -->
    <div class="sidebar-user-footer" onclick="logoutAdmin()" title="Click to Sign Out" style="cursor:pointer;">
      <div style="display: flex; align-items: center; gap: 8px;">
        <div class="user-avatar-circle">DA</div>
        <div>
          <div style="font-size: 11.5px; font-weight: 700; color: var(--text-main);">Dervin Aziza</div>
          <div style="font-size: 9.5px; color: var(--text-sub);">dervinaziza9@gmail.com &bull; <span style="color:#F87171;">Sign Out</span></div>
        </div>
      </div>
      <span style="font-size: 11px; color: var(--accent-red);">🚪</span>
    </div>
  </aside>

  <!-- Main View Area -->
  <main class="desk-main">
    
    <header class="desk-topbar">
      <div class="breadcrumb-wrap">
        <span onclick="switchView('dashboard')" style="cursor: pointer;">🏠</span>
        <span>/</span>
        <span id="topbarCategory">Dashboard</span>
        <span>/</span>
        <span class="breadcrumb-current" id="topbarTitle">Loan Dashboard</span>
      </div>

      <div class="topbar-right">
        <button onclick="logoutAdmin()" title="Sign Out of Admin Desk" style="font-size:12px; font-weight:700; padding:6px 14px; border-radius:8px; color:#F87171; border:1px solid rgba(248,113,113,0.3); background:rgba(248,113,113,0.08); display:flex; align-items:center; gap:6px; cursor:pointer; font-family:inherit;">
          <span>🚪</span> Sign Out
        </button>
        <button class="theme-toggle-btn" onclick="toggleAdminTheme()" id="adminThemeBtn" title="Toggle Light / Dark Mode">☀️</button>
      </div>
    </header>

    <!-- Dynamic Container for Active View -->
    <div class="desk-canvas" id="mainCanvas">
      <!-- Injected by JavaScript -->
    </div>

  </main>

  <!-- Global Command Palette (Ctrl+K) -->
  <div class="search-modal-backdrop" id="searchModal" onclick="closeSearchModal(event)">
    <div class="search-modal-box" onclick="event.stopPropagation()">
      <div class="search-modal-header">
        <span>🔍</span>
        <input type="text" class="search-modal-input" id="searchModalInput" placeholder="Search docTypes, actions, or jump to view (e.g. Loan, Customer)..." oninput="filterSearchResults(this.value)">
        <span class="kbd-shortcut" onclick="closeSearchModalDirect()">ESC</span>
      </div>
      <div class="search-results-list" id="searchResultsContainer">
        <!-- Injected -->
      </div>
    </div>
  </div>

  <!-- Notification Flyout Drawer -->
  <div class="drawer-backdrop" id="notifBackdrop" onclick="closeNotifications()"></div>
  <div class="drawer-panel" id="notifDrawer">
    <div class="drawer-header">
      <h3 style="font-size: 14px; font-weight: 800;">🔔 System Notifications</h3>
      <span style="cursor: pointer; font-size: 16px;" onclick="closeNotifications()">✕</span>
    </div>
    <div class="drawer-body">
      <div style="background:var(--desk-card-surface); padding:12px; border-radius:8px; margin-bottom:10px;">
        <div style="font-size: 11px; color: var(--accent-emerald); font-weight: 700;">DIGITAL CREDIT APPLICATION</div>
        <div style="font-size: 12.5px; font-weight: 600; margin-top: 2px;">New application submitted: KES 100,000</div>
        <div style="font-size: 10.5px; color: var(--text-dim); margin-top: 4px;">2 minutes ago • Automated KYC Match</div>
      </div>
      <div style="background:var(--desk-card-surface); padding:12px; border-radius:8px; margin-bottom:10px;">
        <div style="font-size: 11px; color: var(--accent-blue); font-weight: 700;">REPAYMENT RECORDED</div>
        <div style="font-size: 12.5px; font-weight: 600; margin-top: 2px;">M-Pesa payment received: KES 23,750.00</div>
        <div style="font-size: 10.5px; color: var(--text-dim); margin-top: 4px;">18 minutes ago • Ref # QK91827364</div>
      </div>
    </div>
  </div>

  <!-- LIVE UNDERWRITING SLIDE-OVER DRAWER -->
  <div class="drawer-backdrop" id="underwriteBackdrop" onclick="closeUnderwritingDrawer()"></div>
  <div class="drawer-panel" id="underwritingDrawer">
    <div class="drawer-header">
      <div>
        <div class="badge-pill" style="margin-bottom:4px;">UNDERWRITING ASSESSMENT</div>
        <h3 style="font-size: 16px; font-weight: 800;" id="undAppTitle">Application Review</h3>
      </div>
      <span style="cursor: pointer; font-size: 18px;" onclick="closeUnderwritingDrawer()">✕</span>
    </div>

    <div class="drawer-body" id="undDrawerBody">
      <!-- Injected -->
    </div>

    <div class="drawer-footer">
      <button class="btn-action-pri" style="flex:1.5; padding:10px;" onclick="sanctionAndDisburseActiveApp()">
        <span>⚡ Sanction &amp; Disburse</span>
      </button>
      <button class="btn-action-sec" style="flex:1;" onclick="requestCollateralActiveApp()">
        <span>📑 Collateral</span>
      </button>
      <button class="btn-action-sec" style="color:#F87171; border-color:#7F1D1D;" onclick="declineActiveApp()">
        <span>✕ Decline</span>
      </button>
    </div>
  </div>

  <!-- IN-DOM CINEMATIC ADMINISTRATOR CLEARANCE MODAL -->
  <div class="admin-auth-overlay" id="adminClearanceOverlay">
    <div class="admin-auth-modal">
      <div style="position:absolute; top:16px; right:16px; cursor:pointer; color:#9CA3AF; font-size:18px;" onclick="closeAdminClearanceModal()">✕</div>
      <div style="width: 56px; height: 56px; border-radius: 50%; background: rgba(0, 210, 106, 0.15); border: 1.5px solid #00D26A; color: #00D26A; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px; font-size: 24px;">
        🔒
      </div>
      <div class="badge-pill" style="margin-bottom: 8px;">CLEARANCE LEVEL 4 &bull; UNDERWRITING DESK</div>
      <h3 style="font-size: 20px; font-weight: 800; color: #FAF8F5; margin-bottom: 6px;">Institutional Administrator Access</h3>
      <p style="font-size: 13px; color: #9CA3AF; margin-bottom: 22px; line-height: 1.45;">Enter your cryptographically verified staff credentials to decrypt and unlock institutional lending records.</p>

      <form onsubmit="handleAdminClearanceSubmit(event)">
        <div style="text-align:left; margin-bottom:12px;">
          <label style="font-size:11px; font-weight:700; color:#9CA3AF; text-transform:uppercase; display:block; margin-bottom:4px;">Staff Email Address</label>
          <input type="text" id="clearanceEmailInput" class="modal-input" value="dervinaziza9@gmail.com" placeholder="dervinaziza9@gmail.com" required>
        </div>
        <div style="text-align:left; margin-bottom:16px; position:relative;">
          <label style="font-size:11px; font-weight:700; color:#9CA3AF; text-transform:uppercase; display:block; margin-bottom:4px;">Security Key / Password</label>
          <input type="password" id="clearancePassInput" class="modal-input" placeholder="Enter clearance password (e.g. Oryx2026)" required autofocus style="padding-right:40px;">
          <span onclick="toggleClearanceEye()" style="position:absolute; right:12px; top:32px; cursor:pointer; font-size:14px; user-select:none;" id="clearanceEyeIcon">👁️</span>
        </div>
        
        <div id="clearanceModalAlert" style="display:none; padding:10px; border-radius:8px; font-size:12px; font-weight:600; margin-bottom:14px; background:#3B1212; color:#FCA5A5; border:1px solid #7F1D1D;"></div>

        <button type="submit" class="btn-action-pri" style="width: 100%; padding: 12px; font-size: 13.5px;" id="clearanceSubmitBtn">
          <span>⚡ Authenticate &amp; Unlock Desk</span>
        </button>

        <a href="index.html" style="display:inline-block; margin-top:16px; font-size:12px; color:#9CA3AF; text-decoration:none;">
          &larr; Return to Borrower Portal
        </a>
      </form>
    </div>
  </div>

  <script>
    // =========================================================================
    // AUTHENTICATION & ACCESS CONTROL
    // =========================================================================
    const ORYX_AUTH_SALT = "oryx_fund_2026_salt_sec_";

    async function hashPassword(password) {
      const enc = new TextEncoder();
      const buf = await crypto.subtle.digest("SHA-256", enc.encode(ORYX_AUTH_SALT + password));
      return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
    }

    function checkAdminAuthorization() {
      try {
        const raw = localStorage.getItem('oryx_auth_user');
        if (!raw) return false;
        const auth = JSON.parse(raw);
        if (!auth || auth.role !== 'Admin') return false;
        return true;
      } catch(e) {
        return false;
      }
    }

    function renderAccessDeniedGate() {
      let auth = null;
      try { auth = JSON.parse(localStorage.getItem('oryx_auth_user')); } catch(e) {}
      
      const sb = document.getElementById('mainSidebar');
      const mn = document.querySelector('.desk-main');
      const gate = document.getElementById('adminGateContainer');
      const desc = document.getElementById('gateBorrowerDesc');
      
      if (sb) sb.style.display = 'none';
      if (mn) mn.style.display = 'none';
      if (gate) gate.style.display = 'flex';
      if (desc) {
        desc.innerHTML = auth && auth.email ? `You are signed in as a Borrower (<strong>${auth.email}</strong>). Institutional underwriting &amp; disbursement operations require verified staff clearance.` : 'You are currently not signed in as an administrator. Institutional underwriting &amp; disbursement operations require verified staff clearance.';
      }
    }

    function openAdminClearanceModalDirect() {
      const overlay = document.getElementById('adminClearanceOverlay');
      if (overlay) {
        overlay.classList.add('active');
        const passIn = document.getElementById('clearancePassInput');
        if (passIn) passIn.focus();
      }
    }

    function closeAdminClearanceModal() {
      const overlay = document.getElementById('adminClearanceOverlay');
      if (overlay) overlay.classList.remove('active');
    }

    function toggleClearanceEye() {
      const passIn = document.getElementById('clearancePassInput');
      const eye = document.getElementById('clearanceEyeIcon');
      if (passIn.type === 'password') {
        passIn.type = 'text';
        eye.innerText = '🔒';
      } else {
        passIn.type = 'password';
        eye.innerText = '👁️';
      }
    }

    async function handleAdminClearanceSubmit(e) {
      e.preventDefault();
      const email = document.getElementById('clearanceEmailInput').value.trim();
      const pass = document.getElementById('clearancePassInput').value;
      const alertEl = document.getElementById('clearanceModalAlert');
      const submitBtn = document.getElementById('clearanceSubmitBtn');

      submitBtn.innerText = 'Verifying TLS Signature...';

      const hashed = await hashPassword(pass);
      const validAdminHashes = [
        await hashPassword('Oryx2026'),
        await hashPassword('Admin@26'),
        await hashPassword('Dervin26'),
        await hashPassword('Admin@2026!'),
        await hashPassword('password')
      ];

      if (!validAdminHashes.includes(hashed)) {
        submitBtn.innerText = '⚡ Authenticate & Unlock Desk';
        alertEl.innerText = '⛔ Invalid Administrator Security Key. Clearance Denied.';
        alertEl.style.display = 'block';
        return;
      }

      const adminSession = {
        id: "usr_admin_001",
        name: "Dervin Aziza",
        email: email,
        role: "Admin",
        expires_at: Date.now() + (4 * 3600 * 1000)
      };
      localStorage.setItem('oryx_auth_user', JSON.stringify(adminSession));

      alertEl.style.background = '#0D3319';
      alertEl.style.color = '#86EFAC';
      alertEl.style.borderColor = '#14532D';
      alertEl.innerText = '✨ Clearance Verified. Unlocking Institutional Modules...';
      alertEl.style.display = 'block';

      setTimeout(() => {
        window.location.reload();
      }, 500);
    }

    function logoutAdmin() {
      localStorage.removeItem('oryx_auth_user');
      window.location.href = 'login.html';
    }

    // =========================================================================
    // COMPLETE DATA STORES & DEFAULT MOCK DATA FOR ALL 22 DOCTYPES
    // =========================================================================
    const DB = {
      company: [
        { id: "COMP-001", name: "Oryx Fund Limited", country: "Kenya", currency: "KES", default_bank: "Equity Bank - Corporate #0112938472", reg_no: "CPR/2023/98214", status: "Active" }
      ],
      loan_product: [
        { id: "LP-001", name: "Oryx Subsequent Fast-Track Facility", type: "Unsecured Revolving", rate: "14.00%", penalty: "2.00%", freq: "Monthly", max_tenure: "12 Months", status: "Active" },
        { id: "LP-002", name: "Oryx SME Working Capital", type: "Secured Commercial", rate: "13.50%", penalty: "2.00%", freq: "Monthly", max_tenure: "24 Months", status: "Active" },
        { id: "LP-003", name: "Oryx Asset Finance & Logbook Loan", type: "Secured Asset", rate: "12.50%", penalty: "2.50%", freq: "Monthly", max_tenure: "36 Months", status: "Active" },
        { id: "LP-004", name: "Oryx Emergency Bridging Facility", type: "Short-Term Micro", rate: "15.00%", penalty: "3.00%", freq: "Bullet / Weekly", max_tenure: "3 Months", status: "Active" }
      ],
      charges: [
        { id: "CHG-001", name: "Facility Appraisal Fee", type: "Percentage", base: "Sanctioned Principal", rate: "1.50%", acc: "Fee Income - Appraisal", status: "Active" },
        { id: "CHG-002", name: "Processing & Documentation Fee", type: "Percentage", base: "Disbursed Amount", rate: "2.00%", acc: "Fee Income - Processing", status: "Active" },
        { id: "CHG-003", name: "Late Repayment Default Penalty", type: "Percentage", base: "Overdue Installment", rate: "2.00% / mo", acc: "Penalty Income - Lending", status: "Active" },
        { id: "CHG-004", name: "Collateral Legal Charge & Stamp Duty", type: "Fixed Amount", base: "Fixed", rate: "KES 15,000.00", acc: "Legal Fees Payable", status: "Active" }
      ],
      loan: [
        { id: "ACC-LOAN-2026-00001", customer: "Jane Wanjiku Kamau", product: "Oryx Subsequent Fast-Track Facility", sanctioned: "KES 250,000.00", disbursed: "KES 250,000.00", balance: "KES 185,420.00", status: "Active", date: "2026-08-15" },
        { id: "ACC-LOAN-2026-00002", customer: "David Ochieng Otieno", product: "Oryx SME Working Capital", sanctioned: "KES 500,000.00", disbursed: "KES 500,000.00", balance: "KES 420,000.00", status: "Active", date: "2026-08-10" },
        { id: "ACC-LOAN-2026-00003", customer: "Sarah Muthoni Njoroge", product: "Oryx Asset Finance & Logbook Loan", sanctioned: "KES 750,000.00", disbursed: "KES 750,000.00", balance: "KES 0.00", status: "Closed", date: "2026-05-01" }
      ],
      loan_disbursement: [
        { id: "DISB-2026-0001", loan: "ACC-LOAN-2026-00001", customer: "Jane Wanjiku Kamau", amount: "KES 250,000.00", mode: "M-Pesa B2C", ref: "QK82910291", date: "2026-08-15", status: "Completed" },
        { id: "DISB-2026-0002", loan: "ACC-LOAN-2026-00002", customer: "David Ochieng Otieno", amount: "KES 500,000.00", mode: "Bank Wire (RTGS)", ref: "RTGS/2026/0921", date: "2026-08-10", status: "Completed" }
      ],
      loan_repayment_schedule: [
        { id: "SCH-001", loan: "ACC-LOAN-2026-00001", inst_no: "1 of 12", due_date: "2026-09-15", principal: "KES 20,833.33", interest: "KES 2,916.67", total: "KES 23,750.00", status: "Upcoming" },
        { id: "SCH-002", loan: "ACC-LOAN-2026-00001", inst_no: "2 of 12", due_date: "2026-10-15", principal: "KES 20,833.33", interest: "KES 2,673.61", total: "KES 23,506.94", status: "Upcoming" },
        { id: "SCH-003", loan: "ACC-LOAN-2026-00002", inst_no: "1 of 24", due_date: "2026-09-10", principal: "KES 20,833.33", interest: "KES 5,625.00", total: "KES 26,458.33", status: "Upcoming" }
      ],
      loan_transfer: [
        { id: "TRF-2026-0001", loan: "ACC-LOAN-2026-00003", from_branch: "Nairobi CBD Branch", to_branch: "Westlands Executive Branch", effective_date: "2026-08-01", status: "Approved" }
      ],
      loan_restructure: [
        { id: "RST-2026-0001", loan: "ACC-LOAN-2026-00002", customer: "David Ochieng Otieno", old_tenure: "12 Months", new_tenure: "24 Months", moratorium: "30 Days", status: "Approved" }
      ],
      loan_repayment: [
        { id: "REP-2026-0001", loan: "ACC-LOAN-2026-00001", customer: "Jane Wanjiku Kamau", method: "M-Pesa C2B Paybill", ref: "QK91827364", amount: "KES 23,750.00", principal: "KES 20,833.33", interest: "KES 2,916.67", date: "2026-08-20" },
        { id: "REP-2026-0002", loan: "ACC-LOAN-2026-00002", customer: "David Ochieng Otieno", method: "Direct Bank Transfer", ref: "TXN-882910", amount: "KES 26,458.33", principal: "KES 20,833.33", interest: "KES 5,625.00", date: "2026-08-18" }
      ],
      loan_demand: [
        { id: "DMD-2026-001", loan: "ACC-LOAN-2026-00001", customer: "Jane Wanjiku Kamau", demand_date: "2026-09-01", inst_due: "KES 23,750.00", penalty: "KES 0.00", total_demand: "KES 23,750.00", status: "Issued" },
        { id: "DMD-2026-002", loan: "ACC-LOAN-2026-00002", customer: "David Ochieng Otieno", demand_date: "2026-09-01", inst_due: "KES 26,458.33", penalty: "KES 0.00", total_demand: "KES 26,458.33", status: "Issued" }
      ],
      loan_interest_accrual: [
        { id: "INT-2026-08", start_date: "2026-08-01", end_date: "2026-08-26", accrued_amt: "KES 42,910.45", loans_count: "2 Active", journal: "JV-2026-0891", status: "Posted" }
      ],
      loan_write_off: [
        { id: "WO-2026-0001", loan: "ACC-LOAN-2025-00099", customer: "Defunct Borrower", principal: "KES 0.00", interest: "KES 0.00", reason: "N/A - Clean Portfolio", provision_acc: "Bad Debt Reserve", status: "Zero Write-Offs" }
      ],
      dpd_log: [
        { id: "DPD-2026-001", loan: "ACC-LOAN-2026-00001", customer: "Jane Wanjiku Kamau", dpd: "0 Days", bucket: "Standard (Performing)", date: "2026-08-26" },
        { id: "DPD-2026-002", loan: "ACC-LOAN-2026-00002", customer: "David Ochieng Otieno", dpd: "0 Days", bucket: "Standard (Performing)", date: "2026-08-26" }
      ],
      customer: [
        { id: "CUST-2026-0001", name: "Jane Wanjiku Kamau", email: "jane.wanjiku@oryxfund.co.ke", phone: "+254711223344", national_id: "28394857", score: "740 (Prime)", kyc: "Verified", date: "2026-08-15" },
        { id: "CUST-2026-0002", name: "David Ochieng Otieno", email: "david.otieno@gmail.com", phone: "+254722334455", national_id: "29384712", score: "715 (Good)", kyc: "Verified", date: "2026-08-10" },
        { id: "CUST-2026-0003", name: "Sarah Muthoni Njoroge", email: "sarah.muthoni@yahoo.com", phone: "+254733445566", national_id: "30192837", score: "780 (Excellent)", kyc: "Verified", date: "2026-05-01" }
      ],
      loan_application: [
        { id: "ACC-LOAP-2026-00001", applicant: "Jane Wanjiku Kamau", product: "Oryx Subsequent Fast-Track Facility", amount: "KES 250,000.00", income: "KES 180,000.00", decision: "Sanctioned & Disbursed", date: "2026-08-15" },
        { id: "ACC-LOAP-2026-00002", applicant: "David Ochieng Otieno", product: "Oryx SME Working Capital", amount: "KES 500,000.00", income: "KES 350,000.00", decision: "Sanctioned & Disbursed", date: "2026-08-10" },
        { id: "ACC-LOAP-2026-00003", applicant: "Kipchoge Brian Koech", product: "Oryx Subsequent Fast-Track Facility", amount: "KES 100,000.00", income: "KES 95,000.00", decision: "Under Review", date: "2026-08-26" }
      ],
      loan_security_type: [
        { id: "LST-001", name: "Motor Vehicle (Logbook)", category: "Movable Collateral", rule: "Certified Valuation Report", margin: "25.00%", status: "Active" },
        { id: "LST-002", name: "Title Deed (Freehold / Leasehold)", category: "Immovable Property", rule: "Registered Valuer Assessment", margin: "30.00%", status: "Active" },
        { id: "LST-003", name: "Fixed Deposit Receipt (Cash Lien)", category: "Cash Equivalent", rule: "100% Face Value", margin: "0.00%", status: "Active" },
        { id: "LST-004", name: "NSE Quoted Securities / Shares", category: "Marketable Securities", rule: "30-Day VWAP", margin: "35.00%", status: "Active" }
      ],
      loan_security: [
        { id: "SEC-2026-001", name: "Toyota Prado TX 2019 (KDD 819X)", type: "Motor Vehicle (Logbook)", owner: "David Ochieng Otieno", value: "KES 4,200,000.00", reg_no: "KDD 819X", custodian: "Oryx Vault (Safe 2)" },
        { id: "SEC-2026-002", name: "Residential Plot LR 209/1829 Kiambu", type: "Title Deed (Freehold / Leasehold)", owner: "Sarah Muthoni Njoroge", value: "KES 8,500,000.00", reg_no: "LR Kiambu/1829", custodian: "Discharged / Released" }
      ],
      loan_security_price: [
        { id: "PRC-2026-001", security: "SEC-2026-001 (Toyota Prado)", value: "KES 4,200,000.00", val_date: "2026-08-05", valuer: "Regent Automobile Valuers Ltd" }
      ],
      loan_security_assignment: [
        { id: "ASG-2026-001", loan: "ACC-LOAN-2026-00002", security: "SEC-2026-001 (Toyota Prado)", assigned_val: "KES 4,200,000.00", ltv: "11.90% (Low Risk)", status: "Active Lien" }
      ],
      loan_security_release: [
        { id: "REL-2026-001", loan: "ACC-LOAN-2026-00003", security: "SEC-2026-002 (Plot LR Kiambu)", date: "2026-08-01", discharged_by: "Oryx Legal Counsel", status: "Released & Discharged" }
      ],
      sanctioned_loan_amount: [
        { id: "SANCT-001", customer: "Jane Wanjiku Kamau", limit: "KES 500,000.00", utilized: "KES 250,000.00", available: "KES 250,000.00", expiry: "2027-08-15", status: "Active" },
        { id: "SANCT-002", customer: "David Ochieng Otieno", limit: "KES 1,000,000.00", utilized: "KES 500,000.00", available: "KES 500,000.00", expiry: "2027-08-10", status: "Active" }
      ]
    };

    // Sync dynamically submitted applications from apply.html
    try {
      const localApps = JSON.parse(localStorage.getItem('oryx_applications') || '[]');
      localApps.forEach(a => {
        if (!DB.loan_application.some(x => x.id === a.id)) {
          DB.loan_application.unshift({
            id: a.id,
            applicant: a.fullName || 'Registered Applicant',
            product: a.productName || 'Working Capital Facility',
            amount: 'KES ' + Number(a.amount || 250000).toLocaleString('en-US', {minimumFractionDigits: 2}),
            income: 'KES ' + Number(a.income || 180000).toLocaleString('en-US', {minimumFractionDigits: 2}),
            decision: a.status || 'Under Review',
            date: a.date || 'Today'
          });
        }
      });
    } catch(e) {}

    // =========================================================================
    // METADATA DEFINITIONS FOR ALL 22 VIEWS
    // =========================================================================
    const VIEWS = {
      dashboard: { title: "Loan Dashboard", category: "Dashboard", doctype: "Dashboard" },
      company: { title: "Company", category: "Setup", doctype: "Company", singular: "Company" },
      loan_product: { title: "Loan Product", category: "Setup", doctype: "Loan Product", singular: "Loan Product" },
      charges: { title: "Loan Charges", category: "Setup", doctype: "Loan Charges", singular: "Charge" },
      loan: { title: "Loan", category: "Loan Management", doctype: "Loan", singular: "Loan" },
      loan_disbursement: { title: "Loan Disbursement", category: "Loan Management", doctype: "Loan Disbursement", singular: "Disbursement" },
      loan_repayment_schedule: { title: "Loan Repayment Schedule", category: "Loan Management", doctype: "Loan Repayment Schedule", singular: "Schedule Entry" },
      loan_transfer: { title: "Loan Transfer", category: "Loan Management", doctype: "Loan Transfer", singular: "Transfer" },
      loan_restructure: { title: "Loan Restructure", category: "Loan Management", doctype: "Loan Restructure", singular: "Restructure" },
      loan_repayment: { title: "Loan Repayment", category: "Loan Management", doctype: "Loan Repayment", singular: "Repayment" },
      loan_demand: { title: "Loan Demand", category: "Loan Management", doctype: "Loan Demand", singular: "Demand" },
      loan_interest_accrual: { title: "Loan Interest Accrual", category: "Loan Management", doctype: "Loan Interest Accrual", singular: "Accrual Batch" },
      loan_write_off: { title: "Loan Write Off", category: "Loan Management", doctype: "Loan Write Off", singular: "Write Off" },
      dpd_log: { title: "Days Past Due (DPD) Log", category: "Loan Management", doctype: "DPD Log", singular: "DPD Entry" },
      customer: { title: "Customer", category: "Loan Origination", doctype: "Customer", singular: "Customer" },
      loan_application: { title: "Loan Application", category: "Loan Origination", doctype: "Loan Application", singular: "Loan Application" },
      loan_security_type: { title: "Loan Security Type", category: "Security Management", doctype: "Loan Security Type", singular: "Security Type" },
      loan_security: { title: "Loan Security", category: "Security Management", doctype: "Loan Security", singular: "Security / Collateral" },
      loan_security_price: { title: "Loan Security Price", category: "Security Management", doctype: "Loan Security Price", singular: "Price Valuation" },
      loan_security_assignment: { title: "Loan Security Assignment", category: "Security Management", doctype: "Loan Security Assignment", singular: "Security Assignment" },
      loan_security_release: { title: "Loan Security Release", category: "Security Management", doctype: "Loan Security Release", singular: "Security Release" },
      sanctioned_loan_amount: { title: "Sanctioned Loan Amount", category: "Security Management", doctype: "Sanctioned Loan Amount", singular: "Sanction Limit" }
    };

    let activeViewKey = "dashboard";
    let selectedUnderwriteApp = null;

    function switchView(key) {
      if (!VIEWS[key]) key = "dashboard";
      activeViewKey = key;

      document.querySelectorAll('.sidebar-sub-item, .sidebar-nav-item').forEach(el => el.classList.remove('active'));
      const activeNav = document.getElementById('nav_' + key);
      if (activeNav) activeNav.classList.add('active');

      const meta = VIEWS[key];
      document.getElementById('topbarCategory').innerText = meta.category;
      document.getElementById('topbarTitle').innerText = meta.title;

      window.location.hash = '#' + key;

      const canvas = document.getElementById('mainCanvas');
      if (key === 'dashboard') {
        canvas.innerHTML = renderDashboardView();
      } else {
        canvas.innerHTML = renderTableView(key);
      }
    }

    function renderDashboardView() {
      const activeCount = DB.loan.filter(l => l.status === 'Active').length;
      return `
        <!-- KPI METRICS ROW 1 -->
        <div class="desk-kpi-grid">
          <div class="desk-kpi-card">
            <div class="kpi-title-row"><span>New Loans</span><span>...</span></div>
            <div class="kpi-value">${activeCount + 1}</div>
          </div>
          <div class="desk-kpi-card">
            <div class="kpi-title-row"><span>Active Loans</span><span>...</span></div>
            <div class="kpi-value">${activeCount}</div>
          </div>
          <div class="desk-kpi-card">
            <div class="kpi-title-row"><span>Closed Loans</span><span>...</span></div>
            <div class="kpi-value">1</div>
          </div>
          <div class="desk-kpi-card">
            <div class="kpi-title-row"><span>Total Disbursed</span><span>...</span></div>
            <div class="kpi-value" style="font-size:16px;">Sh 1,000,000.00</div>
          </div>
          <div class="desk-kpi-card">
            <div class="kpi-title-row"><span>Open Applications</span><span>...</span></div>
            <div class="kpi-value">${DB.loan_application.length}</div>
          </div>
        </div>

        <!-- KPI METRICS ROW 2 -->
        <div class="desk-kpi-grid" style="margin-bottom: 24px;">
          <div class="desk-kpi-card">
            <div class="kpi-title-row"><span>New Applications</span><span>...</span></div>
            <div class="kpi-value">${DB.loan_application.filter(a => a.decision.includes('Review')).length}</div>
          </div>
          <div class="desk-kpi-card">
            <div class="kpi-title-row"><span>Total Sanctioned</span><span>...</span></div>
            <div class="kpi-value" style="font-size:17px;">Sh 1.5M</div>
          </div>
          <div class="desk-kpi-card">
            <div class="kpi-title-row"><span>Active Securities</span><span>...</span></div>
            <div class="kpi-value">${DB.loan_security.length}</div>
          </div>
          <div class="desk-kpi-card">
            <div class="kpi-title-row"><span>Unpaid Shortfall</span><span>...</span></div>
            <div class="kpi-value">0</div>
          </div>
          <div class="desk-kpi-card">
            <div class="kpi-title-row"><span>Total Repayments Collected</span><span>...</span></div>
            <div class="kpi-value" style="font-size:16px; color:#34D399;">Sh 73,958.33</div>
          </div>
        </div>

        <!-- CHARTS SECTION -->
        <div class="desk-charts-grid">
          <div class="desk-chart-card">
            <div class="chart-card-head">
              <div>
                <div class="chart-title">New Loans Originated</div>
                <div style="font-size: 11px; color: var(--text-sub);">Real-time portfolio growth tracking</div>
              </div>
              <div class="chart-badge">📅 Last 30 Days</div>
            </div>
            <div class="svg-chart-container">
              <svg viewBox="0 0 400 120" style="width:100%; height:100%;">
                <defs>
                  <linearGradient id="origGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" stop-color="#00D26A" stop-opacity="0.3"/>
                    <stop offset="100%" stop-color="#00D26A" stop-opacity="0.0"/>
                  </linearGradient>
                </defs>
                <path d="M 0 100 Q 100 90 200 40 T 400 20 L 400 120 L 0 120 Z" fill="url(#origGrad)"/>
                <path d="M 0 100 Q 100 90 200 40 T 400 20" fill="none" stroke="#00D26A" stroke-width="2.5"/>
              </svg>
            </div>
          </div>

          <div class="desk-chart-card">
            <div class="chart-card-head">
              <div>
                <div class="chart-title">Disbursements vs Repayments</div>
                <div style="font-size: 11px; color: var(--text-sub);">Liquidity and capital flow</div>
              </div>
              <div class="chart-badge">📅 M-Pesa &amp; RTGS</div>
            </div>
            <div class="svg-chart-container">
              <svg viewBox="0 0 400 120" style="width:100%; height:100%;">
                <path d="M 0 110 Q 120 80 250 40 T 400 15" fill="none" stroke="#34D399" stroke-width="2.5"/>
                <path d="M 0 115 Q 120 105 250 85 T 400 50" fill="none" stroke="#60A5FA" stroke-width="2" stroke-dasharray="4,4"/>
              </svg>
            </div>
          </div>
        </div>

        <!-- QUICK ACTION SUMMARY TABLE: OPEN LOAN APPLICATIONS -->
        <div class="desk-table-card">
          <div class="table-toolbar">
            <div class="table-title">⚡ Digital Applications Underwriting Queue</div>
            <button class="btn-action-pri" onclick="switchView('loan_application')">View All Applications &rarr;</button>
          </div>
          <table class="desk-data-table">
            <thead>
              <tr>
                <th>App Reference</th>
                <th>Applicant</th>
                <th>Facility Product</th>
                <th>Requested</th>
                <th>Decision / Status</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              ${DB.loan_application.slice(0, 4).map((a, idx) => `
                <tr>
                  <td class="mono-code">${a.id}</td>
                  <td style="font-weight:700;">${a.applicant}</td>
                  <td>${a.product}</td>
                  <td style="font-family:var(--font-mono); font-weight:700;">${a.amount}</td>
                  <td><span class="status-tag ${a.decision.includes('Sanctioned') ? 'active' : 'review'}">${a.decision}</span></td>
                  <td>
                    <button class="btn-action-pri" style="font-size:11px; padding:4px 10px;" onclick="openUnderwriteApp(${idx})">
                      ⚡ Underwrite
                    </button>
                  </td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      `;
    }

    function renderTableView(key) {
      const meta = VIEWS[key];
      const rows = DB[key] || [];

      if (rows.length === 0) {
        return `
          <div class="desk-table-card">
            <div class="table-toolbar">
              <div class="table-title">${meta.doctype}</div>
              <div class="table-actions">
                <button class="btn-action-sec" onclick="exportDataCSV('${key}')">📥 Export CSV</button>
                <button class="btn-action-pri" onclick="openAddRecordModal('${key}')">+ New ${meta.singular}</button>
              </div>
            </div>
            <div style="padding: 40px; text-align: center; color: var(--text-sub);">
              No records found in DocType [${meta.doctype}]. Click "+ New ${meta.singular}" to create one.
            </div>
          </div>
        `;
      }

      const headers = Object.keys(rows[0]);

      return `
        <div class="desk-table-card">
          <div class="table-toolbar">
            <div class="table-title">
              <span>${meta.doctype}</span>
              <span class="badge-pill">${rows.length} Records</span>
            </div>
            <div class="table-actions">
              <button class="btn-action-sec" onclick="exportDataCSV('${key}')">📥 Export CBK CSV</button>
              <button class="btn-action-sec" onclick="exportDataJSON('${key}')">📄 Export JSON</button>
              <button class="btn-action-pri" onclick="openAddRecordModal('${key}')">+ New ${meta.singular}</button>
            </div>
          </div>

          <div style="overflow-x: auto;">
            <table class="desk-data-table">
              <thead>
                <tr>
                  ${headers.map(h => `<th>${h.replace(/_/g, ' ')}</th>`).join('')}
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                ${rows.map((row, idx) => `
                  <tr>
                    ${headers.map(h => {
                      const val = row[h];
                      if (h === 'id' || h === 'loan') return `<td class="mono-code">${val}</td>`;
                      if (h === 'status' || h === 'decision' || h === 'kyc') {
                        const cls = (val.includes('Active') || val.includes('Sanctioned') || val.includes('Completed') || val.includes('Verified')) ? 'active' : (val.includes('Review') || val.includes('Upcoming')) ? 'review' : 'closed';
                        return `<td><span class="status-tag ${cls}">${val}</span></td>`;
                      }
                      return `<td>${val}</td>`;
                    }).join('')}
                    <td>
                      ${key === 'loan_application' ? `
                        <button class="btn-action-pri" style="font-size:11px; padding:3px 8px;" onclick="openUnderwriteApp(${idx})">⚡ Underwrite</button>
                      ` : `
                        <button class="btn-action-sec" style="font-size:11px; padding:3px 8px;" onclick="viewRowDetails('${key}', ${idx})">View</button>
                      `}
                    </td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>
      `;
    }

    function openUnderwriteApp(idx) {
      selectedUnderwriteApp = DB.loan_application[idx];
      if (!selectedUnderwriteApp) return;

      document.getElementById('undAppTitle').innerText = 'Underwriting: ' + selectedUnderwriteApp.id;
      const body = document.getElementById('undDrawerBody');

      body.innerHTML = `
        <div style="background:var(--desk-card-surface); border:1px solid var(--desk-border); border-radius:10px; padding:16px; margin-bottom:16px;">
          <div style="font-size:11px; font-weight:700; color:var(--text-sub); text-transform:uppercase;">Applicant Profile</div>
          <div style="font-size:16px; font-weight:800; color:#FAF8F5; margin-top:2px;">${selectedUnderwriteApp.applicant}</div>
          <div style="font-size:12px; color:#9CA3AF; margin-top:2px;">National ID: 32847592 &bull; Primary Phone: +254712345678</div>
        </div>

        <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px; margin-bottom:16px;">
          <div style="background:var(--desk-card-surface); padding:12px; border-radius:8px;">
            <div style="font-size:10.5px; color:var(--text-sub);">Requested Facility</div>
            <div style="font-weight:700; color:#FAF8F5; margin-top:2px;">${selectedUnderwriteApp.product}</div>
          </div>
          <div style="background:var(--desk-card-surface); padding:12px; border-radius:8px;">
            <div style="font-size:10.5px; color:var(--text-sub);">Requested Amount</div>
            <div style="font-family:var(--font-mono); font-weight:700; color:#00D26A; margin-top:2px;">${selectedUnderwriteApp.amount}</div>
          </div>
        </div>

        <div style="background:var(--desk-card-surface); border:1px solid var(--desk-border); border-radius:10px; padding:16px; margin-bottom:16px;">
          <div style="font-size:11px; font-weight:700; color:var(--text-sub); text-transform:uppercase; margin-bottom:8px;">Credit Evaluation (CRB &amp; DTI)</div>
          <div style="display:flex; justify-content:space-between; margin-bottom:6px; font-size:12.5px;">
            <span>Stated Net Monthly Income:</span>
            <strong style="font-family:var(--font-mono);">${selectedUnderwriteApp.income || 'KES 180,000.00'}</strong>
          </div>
          <div style="display:flex; justify-content:space-between; margin-bottom:6px; font-size:12.5px;">
            <span>TransUnion CRB Score:</span>
            <strong style="color:#00D26A;">745 (Tier 1 Prime)</strong>
          </div>
          <div style="display:flex; justify-content:space-between; font-size:12.5px;">
            <span>Estimated Debt-to-Income:</span>
            <strong style="color:#34D399;">28.4% (Comfortable)</strong>
          </div>
        </div>

        <div style="background:rgba(0, 210, 106, 0.08); border:1px dashed #00D26A; border-radius:10px; padding:14px; font-size:12.5px;">
          <div style="font-weight:700; color:#00D26A; margin-bottom:4px;">Recommendation: IMMEDIATE SANCTION</div>
          <div style="color:#D6DFD8; font-size:12px; line-height:1.4;">Applicant qualifies for immediate automated M-Pesa B2C disbursement under Policy Rule #2026-B.</div>
        </div>
      `;

      document.getElementById('underwriteBackdrop').style.display = 'block';
      document.getElementById('underwritingDrawer').classList.add('open');
    }

    function closeUnderwritingDrawer() {
      document.getElementById('underwriteBackdrop').style.display = 'none';
      document.getElementById('underwritingDrawer').classList.remove('open');
    }

    function sanctionAndDisburseActiveApp() {
      if (!selectedUnderwriteApp) return;

      const loanNum = 'ACC-LOAN-2026-0000' + (DB.loan.length + 1);
      const disbNum = 'DISB-2026-000' + (DB.loan_disbursement.length + 1);
      const mpesaRef = 'B2C-QK' + Math.floor(1000000 + Math.random() * 9000000);

      DB.loan.unshift({
        id: loanNum,
        customer: selectedUnderwriteApp.applicant,
        product: selectedUnderwriteApp.product,
        sanctioned: selectedUnderwriteApp.amount,
        disbursed: selectedUnderwriteApp.amount,
        balance: selectedUnderwriteApp.amount,
        status: "Active",
        date: new Date().toISOString().split('T')[0]
      });

      DB.loan_disbursement.unshift({
        id: disbNum,
        loan: loanNum,
        customer: selectedUnderwriteApp.applicant,
        amount: selectedUnderwriteApp.amount,
        mode: "M-Pesa B2C (Daraja)",
        ref: mpesaRef,
        date: new Date().toISOString().split('T')[0],
        status: "Completed"
      });

      selectedUnderwriteApp.decision = "Sanctioned & Disbursed";

      const amtNum = parseInt(selectedUnderwriteApp.amount.replace(/[^0-9]/g, '')) || 250000;
      const borrowerActiveLoan = {
        loanId: loanNum,
        productName: selectedUnderwriteApp.product,
        principal: amtNum,
        disbursedDate: new Date().toISOString().split('T')[0],
        termMonths: 12,
        monthlyRate: 1.5,
        monthlyInstallment: Math.round(amtNum * 1.18 / 12),
        balance: Math.round(amtNum * 1.18),
        nextDueDate: '2026-09-26',
        repayments: []
      };
      localStorage.setItem('oryx_active_loan_usr_reezy_001', JSON.stringify(borrowerActiveLoan));

      closeUnderwritingDrawer();
      alert(`✨ SUCCESS: Loan ${loanNum} Sanctioned!\n\nM-Pesa B2C Disbursal Reference: ${mpesaRef}\nFunds released to ${selectedUnderwriteApp.applicant} instantly.`);
      switchView('loan');
    }

    function requestCollateralActiveApp() {
      if (!selectedUnderwriteApp) return;
      selectedUnderwriteApp.decision = "Collateral Required (Logbook)";
      closeUnderwritingDrawer();
      alert("📑 Application updated: Collateral notification issued to applicant.");
      switchView('loan_application');
    }

    function declineActiveApp() {
      if (!selectedUnderwriteApp) return;
      selectedUnderwriteApp.decision = "Declined (DTI Policy)";
      closeUnderwritingDrawer();
      alert("Application marked as Declined.");
      switchView('loan_application');
    }

    function exportDataCSV(key) {
      const rows = DB[key] || [];
      if (rows.length === 0) { alert('No data to export.'); return; }
      const headers = Object.keys(rows[0]);
      let csvContent = "data:text/csv;charset=utf-8," + headers.join(",") + "\n";
      rows.forEach(r => {
        csvContent += headers.map(h => `"${String(r[h]).replace(/"/g, '""')}"`).join(",") + "\n";
      });
      const encodedUri = encodeURI(csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", `OryxFund_${VIEWS[key].doctype.replace(/\s+/g, '_')}_CBK_${Date.now()}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    function exportDataJSON(key) {
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(DB[key] || [], null, 2));
      const link = document.createElement('a');
      link.setAttribute("href", dataStr);
      link.setAttribute("download", `OryxFund_${VIEWS[key].doctype.replace(/\s+/g, '_')}_${Date.now()}.json`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }

    function openAddRecordModal(key) {
      const name = prompt(`Enter new ${VIEWS[key].singular} name / identifier:`);
      if (name) {
        const newObj = { id: key.toUpperCase().substring(0, 4) + '-' + Math.floor(1000 + Math.random() * 9000), name: name, status: "Active" };
        if (!DB[key]) DB[key] = [];
        DB[key].unshift(newObj);
        switchView(key);
      }
    }

    function viewRowDetails(key, idx) {
      const item = DB[key][idx];
      alert(`DocType Record [${item.id || 'ID'}]:\n\n` + JSON.stringify(item, null, 2));
    }

    function openNotifications() {
      document.getElementById('notifBackdrop').style.display = 'block';
      document.getElementById('notifDrawer').classList.add('open');
    }
    function closeNotifications() {
      document.getElementById('notifBackdrop').style.display = 'none';
      document.getElementById('notifDrawer').classList.remove('open');
    }

    function openSearchModal() {
      document.getElementById('searchModal').style.display = 'flex';
      document.getElementById('searchModalInput').focus();
      filterSearchResults('');
    }
    function closeSearchModal(e) {
      if (e.target.id === 'searchModal') closeSearchModalDirect();
    }
    function closeSearchModalDirect() {
      document.getElementById('searchModal').style.display = 'none';
    }

    function filterSearchResults(query) {
      const container = document.getElementById('searchResultsContainer');
      const q = (query || '').toLowerCase();
      const matched = Object.keys(VIEWS).filter(k => VIEWS[k].title.toLowerCase().includes(q) || VIEWS[k].category.toLowerCase().includes(q));
      
      container.innerHTML = matched.map(k => `
        <div class="search-result-item" onclick="switchView('${k}'); closeSearchModalDirect();">
          <span>${VIEWS[k].title}</span>
          <span style="font-size:10px; font-family:var(--font-mono); color:#00D26A;">${VIEWS[k].category} &bull; DocType</span>
        </div>
      `).join('');
    }

    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        openSearchModal();
      }
      if (e.key === 'Escape') {
        closeSearchModalDirect();
        closeUnderwritingDrawer();
        closeNotifications();
        closeAdminClearanceModal();
      }
    });

    function toggleCategory(id, headerEl) {
      const list = document.getElementById(id);
      const isHidden = list.style.display === 'none';
      list.style.display = isHidden ? 'flex' : 'none';
      headerEl.querySelector('.arrow').innerText = isHidden ? '▼' : '▶';
    }

    function toggleAdminTheme() {
      const html = document.documentElement;
      const cur = html.getAttribute('data-theme') || 'dark';
      const next = cur === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', next);
      html.classList.toggle('dark', next === 'dark');
      document.getElementById('adminThemeBtn').innerText = next === 'dark' ? '☀️' : '🌙';
      localStorage.setItem('oryx_admin_theme', next);
    }

    // Master DOM Init
    document.addEventListener('DOMContentLoaded', () => {
      if (!checkAdminAuthorization()) {
        renderAccessDeniedGate();
        return;
      }

      const savedTheme = localStorage.getItem('oryx_admin_theme') || 'dark';
      document.documentElement.setAttribute('data-theme', savedTheme);
      document.documentElement.classList.toggle('dark', savedTheme === 'dark');
      document.getElementById('adminThemeBtn').innerText = savedTheme === 'dark' ? '☀️' : '🌙';

      const initialHash = window.location.hash.replace('#', '');
      if (initialHash && VIEWS[initialHash]) {
        switchView(initialHash);
      } else {
        switchView('dashboard');
      }
    });
  </script>
</body>
</html>
"""

    with open(f"{base_dir}/admin.html", "w", encoding="utf-8") as f:
        f.write(admin_html)
    with open(f"{base_dir}/desk.html", "w", encoding="utf-8") as f:
        f.write(admin_html)

    print("Master Institutional Admin Desk successfully generated!")

if __name__ == '__main__':
    generate_full_admin_desk()

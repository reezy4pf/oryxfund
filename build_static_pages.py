import os

def create_complete_static_site():
    base_dir = "/home/reezy/.gemini/antigravity-ide/scratch/oryx_fund"

    # 1. BORROWER PORTAL (Screenshot 1 Match)
    borrower_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Loans — Oryx Fund</title>
  <meta name="description" content="View your active loans, outstanding balances, and official M-Pesa Paybill payment instructions.">
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg viewBox='0 0 32 32' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Crect width='32' height='32' rx='8' fill='%231F3224'/%3E%3Cpath d='M7 23L14 9H18L25 23H20.5L18.8 19H13.2L11.5 23H7ZM14.3 16.5H17.7L16 12.5L14.3 16.5Z' fill='%2300D26A'/%3E%3C/svg%3E">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800;1,9..40,400&family=IBM+Plex+Mono:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg-page: #EAE0D8;
      --bg-surface: #FFFFFF;
      --bg-surface-alt: #F7F3EE;
      --border-color: #E2D7CC;
      --border-light: #ECE5DC;
      --text-primary: #1F3224;
      --text-secondary: #556B5D;
      --text-muted: #829488;
      --primary: #1F3224;
      --primary-hover: #2D4834;
      --accent-green: #059669;
      --accent-emerald: #00D26A;
      --hero-bg: #1F3224;
      --hero-text: #FAF8F5;
      --card-shadow: 0 2px 12px rgba(31, 50, 36, 0.05);
      --font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'IBM Plex Mono', monospace;
    }

    [data-theme="dark"], html.dark {
      --bg-page: #080D0A;
      --bg-surface: #101712;
      --bg-surface-alt: #152019;
      --border-color: #1E3023;
      --border-light: #17241B;
      --text-primary: #FAF8F5;
      --text-secondary: #9DB4A5;
      --text-muted: #667D6F;
      --primary: #00D26A;
      --primary-hover: #00FF80;
      --accent-green: #00D26A;
      --accent-emerald: #00D26A;
      --hero-bg: #101712;
      --hero-text: #FAF8F5;
      --card-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      transition: background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease;
    }

    body {
      font-family: var(--font-body);
      background-color: var(--bg-page);
      color: var(--text-primary);
      min-height: 100vh;
      line-height: 1.5;
      padding: 0 20px 60px;
    }

    .portal-nav-wrap {
      max-width: 1060px;
      margin: 20px auto 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .brand-logo-cluster {
      display: flex;
      align-items: center;
      gap: 8px;
      text-decoration: none;
      color: var(--text-primary);
    }

    .nav-actions-cluster {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .nav-pill-btn {
      padding: 8px 18px;
      border-radius: 24px;
      font-size: 13px;
      font-weight: 700;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
      cursor: pointer;
    }

    .nav-pill-active {
      background: var(--primary);
      color: #FFFFFF !important;
      border: 1px solid var(--primary);
      box-shadow: 0 2px 8px rgba(31, 50, 36, 0.15);
    }

    [data-theme="dark"] .nav-pill-active {
      background: var(--accent-emerald);
      color: #000000 !important;
      border-color: var(--accent-emerald);
    }

    .nav-pill-light {
      background: var(--bg-surface);
      color: var(--text-primary);
      border: 1px solid var(--border-color);
      box-shadow: var(--card-shadow);
    }

    .theme-icon-btn {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      color: var(--text-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 15px;
      box-shadow: var(--card-shadow);
    }

    .admin-switch-btn {
      background: rgba(0, 0, 0, 0.05);
      border: 1px dashed var(--border-color);
      color: var(--text-secondary);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 700;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .portal-container {
      max-width: 1060px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .portal-hero-card {
      background: var(--hero-bg);
      color: var(--hero-text);
      border-radius: 18px;
      padding: 32px 36px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
      border: 1px solid rgba(255, 255, 255, 0.08);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }

    .hero-pill-tag {
      background: rgba(255, 255, 255, 0.12);
      color: #FAF8F5;
      font-size: 11px;
      font-weight: 800;
      padding: 4px 12px;
      border-radius: 12px;
      display: inline-block;
      letter-spacing: 0.5px;
      margin-bottom: 12px;
    }

    .hero-title {
      font-size: 24px;
      font-weight: 800;
      letter-spacing: -0.3px;
      margin-bottom: 6px;
    }

    .hero-desc {
      font-size: 13.5px;
      color: #B4C6BA;
      max-width: 520px;
      line-height: 1.45;
    }

    .hero-account-badge {
      font-size: 12px;
      color: #9DB4A5;
      margin-bottom: 12px;
      text-align: right;
    }

    .hero-apply-btn {
      background: #FFFFFF !important;
      color: #1F3224 !important;
      font-size: 13.5px;
      font-weight: 800;
      padding: 10px 22px;
      border-radius: 8px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.15);
      transition: all 0.15s ease;
    }

    .stats-kpi-row {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
    }

    .stat-kpi-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 18px 22px;
      display: flex;
      align-items: center;
      gap: 16px;
      box-shadow: var(--card-shadow);
    }

    .stat-icon-capsule {
      width: 44px;
      height: 44px;
      border-radius: 10px;
      background: var(--bg-surface-alt);
      border: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--text-primary);
      font-size: 18px;
    }

    .stat-label {
      font-size: 10.5px;
      font-weight: 800;
      color: var(--text-muted);
      letter-spacing: 0.6px;
      text-transform: uppercase;
    }

    .stat-number {
      font-family: var(--font-mono);
      font-size: 20px;
      font-weight: 700;
      color: var(--text-primary);
      margin-top: 2px;
    }

    .portal-section-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 24px 28px;
      box-shadow: var(--card-shadow);
    }

    .card-head-title {
      font-size: 17px;
      font-weight: 700;
      color: var(--text-primary);
    }

    .card-head-desc {
      font-size: 13px;
      color: var(--text-secondary);
      margin-top: 2px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border-light);
    }

    .empty-state-wrap {
      padding: 48px 20px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }

    .empty-icon-circle {
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: var(--bg-surface-alt);
      border: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 14px;
      color: var(--text-muted);
      font-size: 22px;
    }

    .empty-title {
      font-size: 16px;
      font-weight: 700;
      color: var(--text-primary);
      margin-bottom: 6px;
    }

    .empty-desc {
      font-size: 13px;
      color: var(--text-secondary);
      max-width: 440px;
      margin-bottom: 18px;
      line-height: 1.45;
    }

    .btn-apply-green {
      background: var(--primary) !important;
      color: #FFFFFF !important;
      font-size: 13px;
      font-weight: 700;
      padding: 9px 20px;
      border-radius: 8px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
      box-shadow: 0 2px 8px rgba(31, 50, 36, 0.15);
    }

    [data-theme="dark"] .btn-apply-green {
      background: var(--accent-emerald) !important;
      color: #000000 !important;
    }

    @media (max-width: 768px) {
      .stats-kpi-row { grid-template-columns: 1fr; }
      .portal-hero-card { padding: 24px; }
      .hero-account-badge { text-align: left; }
    }
  </style>
</head>
<body>

  <!-- Header -->
  <header class="portal-nav-wrap">
    <a href="index.html" class="brand-logo-cluster">
      <svg width="28" height="28" viewBox="0 0 32 32" fill="none">
        <rect width="32" height="32" rx="7" fill="#1F3224"/>
        <path d="M7 23L14 9H18L25 23H20.5L18.8 19H13.2L11.5 23H7ZM14.3 16.5H17.7L16 12.5L14.3 16.5Z" fill="#00D26A"/>
      </svg>
      <span style="font-weight: 800; font-size: 17px; letter-spacing: -0.3px;">Oryx <span style="font-size: 11px; font-weight: 700; color: var(--text-muted);">Fund</span></span>
    </a>

    <div class="nav-actions-cluster">
      <a href="index.html" class="nav-pill-btn nav-pill-active">My Portal</a>
      <a href="apply.html" class="nav-pill-btn nav-pill-light">Loan Application</a>
      <a href="my_account.html" class="nav-pill-btn nav-pill-light">👤 Reezy</a>
      <button class="theme-icon-btn" onclick="toggleTheme()" id="themeBtn" title="Toggle Light / Dark Mode">🌙</button>
      <a href="admin.html" class="admin-switch-btn" title="View Admin Desk">🛡️ Admin Link</a>
    </div>
  </header>

  <!-- Main Borrower Portal Content -->
  <main class="portal-container">

    <!-- Hero Card -->
    <div class="portal-hero-card">
      <div>
        <span class="hero-pill-tag">MY PORTAL</span>
        <h1 class="hero-title">My Loans &amp; Repayments</h1>
        <p class="hero-desc">View your active loans, outstanding balances, and official M-Pesa Paybill payment instructions.</p>
      </div>
      <div>
        <div class="hero-account-badge">Account: reezyhoops@gmail.com</div>
        <a href="apply.html" class="hero-apply-btn">+ Apply for a New Loan</a>
      </div>
    </div>

    <!-- 3 KPI Cards -->
    <div class="stats-kpi-row">
      <div class="stat-kpi-card">
        <div class="stat-icon-capsule">💼</div>
        <div>
          <div class="stat-label">Active Loans</div>
          <div class="stat-number">0</div>
        </div>
      </div>
      <div class="stat-kpi-card">
        <div class="stat-icon-capsule">💲</div>
        <div>
          <div class="stat-label">Total Principal Borrowed</div>
          <div class="stat-number">KES 0.00</div>
        </div>
      </div>
      <div class="stat-kpi-card">
        <div class="stat-icon-capsule">⏱️</div>
        <div>
          <div class="stat-label">Outstanding Balance</div>
          <div class="stat-number">KES 0.00</div>
        </div>
      </div>
    </div>

    <!-- Active Loans Card -->
    <section class="portal-section-card">
      <h2 class="card-head-title">Active Loans</h2>
      <p class="card-head-desc">Manage existing loan terms, disbursals, and repayments.</p>
      
      <div class="empty-state-wrap">
        <div class="empty-icon-circle">💼</div>
        <div class="empty-title">No Active Loans</div>
        <p class="empty-desc">You do not currently have any active loans. You can submit a new loan application in under 2 minutes.</p>
        <a href="apply.html" class="btn-apply-green">+ Apply for a Loan</a>
      </div>
    </section>

    <!-- Application History Card -->
    <section class="portal-section-card">
      <h2 class="card-head-title">Application History</h2>
      <p class="card-head-desc">Track status and review records of all submitted loan applications.</p>
      
      <div class="empty-state-wrap">
        <div class="empty-icon-circle">📄</div>
        <div class="empty-title">No Applications Found</div>
        <p class="empty-desc">Your submitted applications will appear here with real-time status updates.</p>
      </div>
    </section>

  </main>

  <script>
    function toggleTheme() {
      const html = document.documentElement;
      const cur = html.getAttribute('data-theme') || 'light';
      const next = cur === 'light' ? 'dark' : 'light';
      html.setAttribute('data-theme', next);
      document.getElementById('themeBtn').innerText = next === 'dark' ? '☀️' : '🌙';
      localStorage.setItem('oryx_theme', next);
    }
    const saved = localStorage.getItem('oryx_theme');
    if (saved) {
      document.documentElement.setAttribute('data-theme', saved);
      document.getElementById('themeBtn').innerText = saved === 'dark' ? '☀️' : '🌙';
    }
  </script>
</body>
</html>
"""

    # 2. LOAN APPLICATION (apply.html)
    apply_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Loan Application — Oryx Fund</title>
  <meta name="description" content="Instant digital loan applications and returning borrower subsequent facility portal.">
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg viewBox='0 0 32 32' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Crect width='32' height='32' rx='8' fill='%231F3224'/%3E%3Cpath d='M7 23L14 9H18L25 23H20.5L18.8 19H13.2L11.5 23H7ZM14.3 16.5H17.7L16 12.5L14.3 16.5Z' fill='%2300D26A'/%3E%3C/svg%3E">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800;1,9..40,400&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg-page: #EAE0D8;
      --bg-surface: #FFFFFF;
      --bg-surface-alt: #F7F3EE;
      --border-color: #E2D7CC;
      --border-light: #ECE5DC;
      --text-primary: #1F3224;
      --text-secondary: #556B5D;
      --text-muted: #829488;
      --primary: #1F3224;
      --accent-green: #059669;
      --accent-emerald: #00D26A;
      --card-shadow: 0 4px 20px rgba(31, 50, 36, 0.06);
      --font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'IBM Plex Mono', monospace;
    }

    [data-theme="dark"], html.dark {
      --bg-page: #080D0A;
      --bg-surface: #101712;
      --bg-surface-alt: #16221A;
      --border-color: #1F3325;
      --border-light: #18281D;
      --text-primary: #FAF8F5;
      --text-secondary: #9DB4A5;
      --text-muted: #667D6F;
      --primary: #00D26A;
      --accent-green: #00D26A;
      --accent-emerald: #00D26A;
      --card-shadow: 0 4px 24px rgba(0, 0, 0, 0.5);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      transition: background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease;
    }

    body {
      font-family: var(--font-body);
      background-color: var(--bg-page);
      color: var(--text-primary);
      min-height: 100vh;
      padding: 0 20px 60px;
    }

    .portal-nav-wrap {
      max-width: 1060px;
      margin: 20px auto 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .brand-logo-cluster {
      display: flex;
      align-items: center;
      gap: 8px;
      text-decoration: none;
      color: var(--text-primary);
    }

    .nav-actions-cluster {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .nav-pill-btn {
      padding: 8px 18px;
      border-radius: 24px;
      font-size: 13px;
      font-weight: 700;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .nav-pill-active {
      background: var(--primary);
      color: #FFFFFF !important;
      box-shadow: 0 2px 8px rgba(31, 50, 36, 0.15);
    }
    [data-theme="dark"] .nav-pill-active {
      background: var(--accent-emerald);
      color: #000000 !important;
    }

    .nav-pill-light {
      background: var(--bg-surface);
      color: var(--text-primary);
      border: 1px solid var(--border-color);
    }

    .theme-icon-btn {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      color: var(--text-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 15px;
    }

    .apply-container {
      max-width: 1060px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .express-hero-bar {
      background: linear-gradient(135deg, #1F3224 0%, #101B13 100%);
      color: #FAF8F5;
      padding: 28px 32px;
      border-radius: 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: var(--card-shadow);
    }
    [data-theme="dark"] .express-hero-bar {
      background: linear-gradient(135deg, #101712 0%, #080D0A 100%);
      border: 1px solid var(--border-color);
    }

    .verified-kyc-banner {
      background: var(--bg-surface);
      border: 1.5px solid #00D26A;
      border-radius: 14px;
      padding: 18px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 14px;
      box-shadow: var(--card-shadow);
    }

    .kyc-val {
      font-size: 14px;
      font-weight: 700;
    }

    .kyc-label {
      font-size: 10.5px;
      color: var(--text-muted);
      text-transform: uppercase;
      font-weight: 800;
    }

    .oryx-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 28px 32px;
      box-shadow: var(--card-shadow);
    }

    .calc-box {
      background: var(--bg-surface-alt);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 24px;
      margin-top: 18px;
    }

    .amount-slider {
      width: 100%;
      height: 8px;
      border-radius: 4px;
      background: var(--border-color);
      outline: none;
      -webkit-appearance: none;
      cursor: pointer;
      margin: 14px 0;
    }

    .amount-slider::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: var(--accent-emerald);
      cursor: pointer;
      border: 3px solid #FFFFFF;
      box-shadow: 0 2px 8px rgba(0,0,0,0.25);
    }

    .preset-pills {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 20px;
    }

    .pill-btn {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      color: var(--text-secondary);
      font-size: 12px;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: 20px;
      cursor: pointer;
    }

    .pill-btn.active {
      border-color: var(--accent-emerald);
      color: var(--text-primary);
      background: rgba(0, 210, 106, 0.1);
    }

    .metrics-live-hud {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 16px 20px;
    }

    .hud-title {
      font-size: 10.5px;
      font-weight: 800;
      color: var(--text-muted);
      text-transform: uppercase;
    }

    .hud-number {
      font-family: var(--font-mono);
      font-size: 17px;
      font-weight: 700;
      color: var(--text-primary);
      margin-top: 4px;
    }

    .oryx-btn-express {
      background: linear-gradient(135deg, #00D26A 0%, #059669 100%) !important;
      color: #000000 !important;
      font-weight: 800 !important;
      font-size: 14px;
      padding: 12px 26px;
      border-radius: 8px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 4px 14px rgba(0, 210, 106, 0.35) !important;
      cursor: pointer;
      border: none;
    }
  </style>
</head>
<body>

  <header class="portal-nav-wrap">
    <a href="index.html" class="brand-logo-cluster">
      <svg width="28" height="28" viewBox="0 0 32 32" fill="none">
        <rect width="32" height="32" rx="7" fill="#1F3224"/>
        <path d="M7 23L14 9H18L25 23H20.5L18.8 19H13.2L11.5 23H7ZM14.3 16.5H17.7L16 12.5L14.3 16.5Z" fill="#00D26A"/>
      </svg>
      <span style="font-weight: 800; font-size: 17px; letter-spacing: -0.3px;">Oryx <span style="font-size: 11px; font-weight: 700; color: var(--text-muted);">Fund</span></span>
    </a>

    <div class="nav-actions-cluster">
      <a href="index.html" class="nav-pill-btn nav-pill-light">My Portal</a>
      <a href="apply.html" class="nav-pill-btn nav-pill-active">Loan Application</a>
      <a href="my_account.html" class="nav-pill-btn nav-pill-light">👤 Reezy</a>
      <button class="theme-icon-btn" onclick="toggleTheme()" id="themeBtn" title="Toggle Light / Dark Mode">🌙</button>
      <a href="admin.html" class="nav-pill-btn nav-pill-light" style="font-size: 11px;">🛡️ Admin Desk</a>
    </div>
  </header>

  <main class="apply-container">

    <div class="express-hero-bar">
      <div>
        <span style="background: rgba(0, 210, 106, 0.15); border: 1px solid #00D26A; color: #00D26A; font-size: 10.5px; font-weight: 800; padding: 4px 10px; border-radius: 12px; display: inline-block; margin-bottom: 6px;">⚡ FAST-TRACK RETURNING BORROWER</span>
        <h1 style="font-size: 24px; font-weight: 800;">Subsequent Facility Application</h1>
        <p style="font-size: 13px; color: #B4C6BA;">Choose your facility terms for priority underwriting and direct disbursal.</p>
      </div>
      <div style="text-align: right;">
        <div style="font-size: 11px; color: #9DB4A5; font-weight: 700; text-transform: uppercase;">Average SLA</div>
        <div style="font-family: var(--font-mono); font-size: 22px; font-weight: 700; color: #00D26A;">15 Minutes</div>
      </div>
    </div>

    <!-- Verified KYC Banner -->
    <div class="verified-kyc-banner">
      <div>
        <div class="kyc-label">Borrower</div>
        <div class="kyc-val">Reezy Mwangi</div>
      </div>
      <div>
        <div class="kyc-label">National ID</div>
        <div class="kyc-val" style="font-family: var(--font-mono);">31****89</div>
      </div>
      <div>
        <div class="kyc-label">Payout Route</div>
        <div class="kyc-val">M-Pesa (+254***678)</div>
      </div>
      <div style="background: rgba(0, 210, 106, 0.12); color: var(--accent-green); font-size: 12px; font-weight: 800; padding: 5px 12px; border-radius: 20px;">
        ✓ Verified KYC on Record
      </div>
    </div>

    <!-- Interactive Facility Specs Card -->
    <section class="oryx-card">
      <h2 style="font-size: 18px; font-weight: 700; margin-bottom: 4px;">1. Facility Specifications</h2>
      <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 16px;">Configure your loan amount and view live monthly repayments.</p>

      <div class="calc-box">
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="font-size: 12px; font-weight: 800; color: var(--text-muted); text-transform: uppercase;">Requested Facility Amount</span>
          <span id="amountDisplay" style="font-family: var(--font-mono); font-size: 28px; font-weight: 700; color: var(--text-primary);">KES 100,000</span>
        </div>

        <input type="range" class="amount-slider" id="loanSlider" min="10000" max="1000000" step="5000" value="100000" oninput="calcLoan(this.value)">

        <div class="preset-pills">
          <button class="pill-btn" onclick="setVal(25000)">KES 25K</button>
          <button class="pill-btn" onclick="setVal(50000)">KES 50K</button>
          <button class="pill-btn active" onclick="setVal(100000)">KES 100K</button>
          <button class="pill-btn" onclick="setVal(250000)">KES 250K</button>
          <button class="pill-btn" onclick="setVal(500000)">KES 500K</button>
        </div>

        <div class="metrics-live-hud">
          <div>
            <div class="hud-title">Principal</div>
            <div class="hud-number" id="hudPrincipal">KES 100,000</div>
          </div>
          <div>
            <div class="hud-title">Est. Interest</div>
            <div class="hud-number" id="hudInterest">KES 7,000</div>
          </div>
          <div>
            <div class="hud-title">Monthly Installment</div>
            <div class="hud-number" style="color: var(--accent-emerald);" id="hudMonthly">KES 17,833 / mo</div>
          </div>
          <div>
            <div class="hud-title">Total Repayment</div>
            <div class="hud-number" id="hudTotal">KES 107,000</div>
          </div>
        </div>
      </div>

      <div style="margin-top: 24px; display: flex; justify-content: flex-end;">
        <button class="oryx-btn-express" onclick="alert('⚡ Subsequent Loan Application Submitted! Disbursal scheduled within 15 minutes to M-Pesa +254***678')">
          ⚡ Submit Subsequent Loan Application
        </button>
      </div>
    </section>

  </main>

  <script>
    function toggleTheme() {
      const html = document.documentElement;
      const cur = html.getAttribute('data-theme') || 'light';
      const next = cur === 'light' ? 'dark' : 'light';
      html.setAttribute('data-theme', next);
      document.getElementById('themeBtn').innerText = next === 'dark' ? '☀️' : '🌙';
      localStorage.setItem('oryx_theme', next);
    }
    const saved = localStorage.getItem('oryx_theme');
    if (saved) {
      document.documentElement.setAttribute('data-theme', saved);
      document.getElementById('themeBtn').innerText = saved === 'dark' ? '☀️' : '🌙';
    }

    function setVal(amt) {
      document.getElementById('loanSlider').value = amt;
      calcLoan(amt);
    }

    function calcLoan(val) {
      const amount = parseInt(val, 10);
      document.getElementById('amountDisplay').innerText = 'KES ' + amount.toLocaleString('en-US');
      const interest = Math.round(amount * 0.14 * (6 / 12));
      const total = amount + interest;
      const monthly = Math.round(total / 6);
      document.getElementById('hudPrincipal').innerText = 'KES ' + amount.toLocaleString('en-US');
      document.getElementById('hudInterest').innerText = 'KES ' + interest.toLocaleString('en-US');
      document.getElementById('hudMonthly').innerText = 'KES ' + monthly.toLocaleString('en-US') + ' / mo';
      document.getElementById('hudTotal').innerText = 'KES ' + total.toLocaleString('en-US');
    }
  </script>
</body>
</html>
"""

    # 3. BORROWER ACCOUNT (my_account.html)
    account_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Account — Oryx Fund</title>
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg viewBox='0 0 32 32' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Crect width='32' height='32' rx='8' fill='%231F3224'/%3E%3Cpath d='M7 23L14 9H18L25 23H20.5L18.8 19H13.2L11.5 23H7ZM14.3 16.5H17.7L16 12.5L14.3 16.5Z' fill='%2300D26A'/%3E%3C/svg%3E">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800;1,9..40,400&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg-page: #EAE0D8;
      --bg-surface: #FFFFFF;
      --bg-surface-alt: #F7F3EE;
      --border-color: #E2D7CC;
      --border-light: #ECE5DC;
      --text-primary: #1F3224;
      --text-secondary: #556B5D;
      --text-muted: #829488;
      --primary: #1F3224;
      --accent-green: #059669;
      --accent-emerald: #00D26A;
      --card-shadow: 0 4px 20px rgba(31, 50, 36, 0.06);
      --font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'IBM Plex Mono', monospace;
    }

    [data-theme="dark"], html.dark {
      --bg-page: #080D0A;
      --bg-surface: #101712;
      --bg-surface-alt: #16221A;
      --border-color: #1F3325;
      --border-light: #18281D;
      --text-primary: #FAF8F5;
      --text-secondary: #9DB4A5;
      --text-muted: #667D6F;
      --primary: #00D26A;
      --accent-green: #00D26A;
      --accent-emerald: #00D26A;
      --card-shadow: 0 4px 24px rgba(0, 0, 0, 0.5);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      transition: background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease;
    }

    body {
      font-family: var(--font-body);
      background-color: var(--bg-page);
      color: var(--text-primary);
      min-height: 100vh;
      padding: 0 20px 60px;
    }

    .portal-nav-wrap {
      max-width: 1060px;
      margin: 20px auto 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .brand-logo-cluster {
      display: flex;
      align-items: center;
      gap: 8px;
      text-decoration: none;
      color: var(--text-primary);
    }

    .nav-actions-cluster {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .nav-pill-btn {
      padding: 8px 18px;
      border-radius: 24px;
      font-size: 13px;
      font-weight: 700;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .nav-pill-active {
      background: var(--primary);
      color: #FFFFFF !important;
    }
    [data-theme="dark"] .nav-pill-active {
      background: var(--accent-emerald);
      color: #000000 !important;
    }

    .nav-pill-light {
      background: var(--bg-surface);
      color: var(--text-primary);
      border: 1px solid var(--border-color);
    }

    .theme-icon-btn {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      color: var(--text-primary);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 15px;
    }

    .account-layout {
      max-width: 1060px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 2fr 1fr;
      gap: 20px;
    }

    .oryx-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 28px;
      box-shadow: var(--card-shadow);
      margin-bottom: 20px;
    }

    .form-group {
      margin-bottom: 16px;
    }

    .form-label {
      font-size: 12px;
      font-weight: 700;
      color: var(--text-muted);
      display: block;
      margin-bottom: 4px;
    }

    .form-control {
      width: 100%;
      padding: 10px 14px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: var(--bg-surface-alt);
      color: var(--text-primary);
      font-size: 13.5px;
      font-family: var(--font-body);
      outline: none;
    }

    .oryx-btn-express {
      background: linear-gradient(135deg, #00D26A 0%, #059669 100%) !important;
      color: #000000 !important;
      font-weight: 800 !important;
      font-size: 13.5px;
      padding: 12px 20px;
      border-radius: 8px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 100%;
      box-shadow: 0 4px 14px rgba(0, 210, 106, 0.35) !important;
    }

    @media (max-width: 768px) {
      .account-layout { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <header class="portal-nav-wrap">
    <a href="index.html" class="brand-logo-cluster">
      <svg width="28" height="28" viewBox="0 0 32 32" fill="none">
        <rect width="32" height="32" rx="7" fill="#1F3224"/>
        <path d="M7 23L14 9H18L25 23H20.5L18.8 19H13.2L11.5 23H7ZM14.3 16.5H17.7L16 12.5L14.3 16.5Z" fill="#00D26A"/>
      </svg>
      <span style="font-weight: 800; font-size: 17px; letter-spacing: -0.3px;">Oryx <span style="font-size: 11px; font-weight: 700; color: var(--text-muted);">Fund</span></span>
    </a>

    <div class="nav-actions-cluster">
      <a href="index.html" class="nav-pill-btn nav-pill-light">My Portal</a>
      <a href="apply.html" class="nav-pill-btn nav-pill-light">Loan Application</a>
      <a href="my_account.html" class="nav-pill-btn nav-pill-active">👤 Reezy</a>
      <button class="theme-icon-btn" onclick="toggleTheme()" id="themeBtn" title="Toggle Light / Dark Mode">🌙</button>
      <a href="admin.html" class="nav-pill-btn nav-pill-light" style="font-size: 11px;">🛡️ Admin Desk</a>
    </div>
  </header>

  <main class="account-layout">
    
    <div>
      <section class="oryx-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
          <div>
            <h2 style="font-size: 18px; font-weight: 700;">Personal &amp; Contact Details</h2>
            <p style="font-size: 12.5px; color: var(--text-secondary);">Keep your legal name and contact details updated for loan verification.</p>
          </div>
          <span style="background: rgba(0, 210, 106, 0.12); color: var(--accent-green); font-size: 12px; font-weight: 800; padding: 4px 12px; border-radius: 20px;">✓ Verified Borrower</span>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
          <div class="form-group">
            <label class="form-label">Full Legal Name</label>
            <input type="text" class="form-control" value="Reezy Mwangi" readonly>
          </div>
          <div class="form-group">
            <label class="form-label">Email Address</label>
            <input type="email" class="form-control" value="reezyhoops@gmail.com" readonly>
          </div>
          <div class="form-group">
            <label class="form-label">Mobile / Phone Number</label>
            <input type="tel" class="form-control" value="+254712345678" readonly>
          </div>
          <div class="form-group">
            <label class="form-label">National ID Number</label>
            <input type="text" class="form-control" value="31456789" readonly>
          </div>
        </div>
      </section>

      <section class="oryx-card">
        <h2 style="font-size: 18px; font-weight: 700; margin-bottom: 4px;">Disbursement &amp; Banking Preferences</h2>
        <p style="font-size: 12.5px; color: var(--text-secondary); margin-bottom: 16px;">Designated payout accounts used for instant loan disbursements.</p>
        
        <div class="form-group">
          <label class="form-label">M-Pesa Disbursal Number</label>
          <input type="text" class="form-control" value="+254712345678" readonly>
        </div>
      </section>
    </div>

    <div>
      <!-- Express Subsequent Loan Card -->
      <div class="oryx-card" style="border: 1.5px solid #00D26A; background: linear-gradient(145deg, rgba(0, 210, 106, 0.08) 0%, transparent 100%);">
        <span style="font-size: 10px; font-weight: 800; color: #00D26A; letter-spacing: 0.8px;">⚡ EXPRESS REPEAT FACILITY</span>
        <h3 style="font-size: 17px; font-weight: 700; margin: 4px 0 6px;">Fast-Track Subsequent Loan</h3>
        <p style="font-size: 12.5px; color: var(--text-secondary); margin-bottom: 16px;">Apply for a new advance using your existing verified profile.</p>
        <a href="apply.html?flow=express" class="oryx-btn-express">⚡ Apply in 60 Seconds ➔</a>
      </div>

      <!-- Security Card -->
      <div class="oryx-card">
        <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 4px;">Security &amp; Password</h3>
        <p style="font-size: 12.5px; color: var(--text-secondary); margin-bottom: 14px;">Update your account login password.</p>
        <div class="form-group">
          <label class="form-label">Current Password</label>
          <input type="password" class="form-control" placeholder="••••••••">
        </div>
        <div class="form-group">
          <label class="form-label">New Password</label>
          <input type="password" class="form-control" placeholder="Min. 6 characters">
        </div>
        <button style="width: 100%; padding: 10px; border-radius: 8px; background: var(--primary); color: #FFF; font-weight: 700; border: none; cursor: pointer;">Update Password</button>
      </div>
    </div>

  </main>

  <script>
    function toggleTheme() {
      const html = document.documentElement;
      const cur = html.getAttribute('data-theme') || 'light';
      const next = cur === 'light' ? 'dark' : 'light';
      html.setAttribute('data-theme', next);
      document.getElementById('themeBtn').innerText = next === 'dark' ? '☀️' : '🌙';
      localStorage.setItem('oryx_theme', next);
    }
    const saved = localStorage.getItem('oryx_theme');
    if (saved) {
      document.documentElement.setAttribute('data-theme', saved);
      document.getElementById('themeBtn').innerText = saved === 'dark' ? '☀️' : '🌙';
    }
  </script>
</body>
</html>
"""

    # 4. ADMIN DESK (admin.html & desk.html) - Exact Screenshot 2 Match
    admin_html = """<!DOCTYPE html>
<html lang="en" data-theme="dark" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Loan Dashboard — Oryx Fund Admin</title>
  <meta name="description" content="Institutional credit and loan portfolio analytics dashboard for Oryx Fund.">
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg viewBox='0 0 32 32' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Crect width='32' height='32' rx='8' fill='%231F3224'/%3E%3Cpath d='M7 23L14 9H18L25 23H20.5L18.8 19H13.2L11.5 23H7ZM14.3 16.5H17.7L16 12.5L14.3 16.5Z' fill='%2300D26A'/%3E%3C/svg%3E">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    :root {
      --desk-bg: #090909;
      --desk-sidebar-bg: #0D0D0D;
      --desk-card-bg: #121212;
      --desk-card-hover: #171717;
      --desk-border: #1F1F1F;
      --desk-border-light: #181818;
      --text-main: #FAF8F5;
      --text-sub: #9E9E9E;
      --text-dim: #666666;
      --accent-green: #34D399;
      --accent-emerald: #00D26A;
      --accent-red: #F87171;
      --font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'IBM Plex Mono', monospace;
    }

    [data-theme="light"] {
      --desk-bg: #F4EFEB;
      --desk-sidebar-bg: #EAE3DC;
      --desk-card-bg: #FFFFFF;
      --desk-card-hover: #F9F7F5;
      --desk-border: #DFD5CB;
      --desk-border-light: #E8E0D7;
      --text-main: #1F3224;
      --text-sub: #556B5D;
      --text-dim: #829488;
      --accent-green: #059669;
      --accent-emerald: #059669;
      --accent-red: #DC2626;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      transition: background-color 0.15s ease, border-color 0.15s ease, color 0.15s ease;
    }

    body {
      font-family: var(--font-body);
      background-color: var(--desk-bg);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      overflow-x: hidden;
    }

    .desk-sidebar {
      width: 230px;
      min-width: 230px;
      background: var(--desk-sidebar-bg);
      border-right: 1px solid var(--desk-border);
      display: flex;
      flex-direction: column;
      padding: 14px 10px;
      height: 100vh;
      position: sticky;
      top: 0;
      overflow-y: auto;
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
    }

    .brand-title { font-size: 13px; font-weight: 700; }
    .brand-sub { font-size: 10px; color: var(--text-sub); }

    .sidebar-search-box {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--desk-border);
      border-radius: 6px;
      padding: 6px 10px;
      font-size: 12px;
      color: var(--text-sub);
      margin-bottom: 8px;
      cursor: pointer;
    }

    .kbd-shortcut {
      background: rgba(255, 255, 255, 0.08);
      font-size: 10px;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: var(--font-mono);
    }

    .sidebar-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 7px 10px;
      border-radius: 6px;
      font-size: 12.5px;
      font-weight: 500;
      color: var(--text-sub);
      text-decoration: none;
      cursor: pointer;
      margin-bottom: 2px;
    }

    .sidebar-item:hover {
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.04);
    }

    .sidebar-item.active {
      background: rgba(255, 255, 255, 0.08);
      color: var(--text-main);
      font-weight: 700;
    }

    [data-theme="light"] .sidebar-item.active {
      background: rgba(0, 0, 0, 0.06);
    }

    .sidebar-sub-item {
      padding: 5px 10px 5px 28px;
      font-size: 12px;
      color: var(--text-sub);
      text-decoration: none;
      display: block;
      cursor: pointer;
    }
    .sidebar-sub-item:hover { color: var(--text-main); }

    .sidebar-user-footer {
      margin-top: auto;
      display: flex;
      align-items: center;
      gap: 8px;
      padding: 10px;
      border-top: 1px solid var(--desk-border);
      border-radius: 6px;
    }

    .user-avatar-circle {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: #E0561B;
      color: #FFFFFF;
      font-size: 10px;
      font-weight: 800;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .desk-main {
      flex: 1;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow-y: auto;
    }

    .desk-topbar {
      height: 48px;
      padding: 0 24px;
      border-bottom: 1px solid var(--desk-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--desk-bg);
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .breadcrumb-wrap {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 13px;
      color: var(--text-sub);
    }

    .breadcrumb-current { font-weight: 700; color: var(--text-main); }

    .topbar-right {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .borrower-switch-link {
      background: rgba(0, 210, 106, 0.1);
      border: 1px solid var(--accent-emerald);
      color: var(--accent-emerald);
      padding: 4px 12px;
      border-radius: 16px;
      font-size: 11px;
      font-weight: 800;
      text-decoration: none;
    }

    .desk-canvas {
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .number-cards-grid {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 14px;
    }

    .number-card {
      background: var(--desk-card-bg);
      border: 1px solid var(--desk-border);
      border-radius: 10px;
      padding: 14px 16px;
      position: relative;
      transition: all 0.15s ease;
    }

    .number-card:hover {
      background: var(--desk-card-hover);
      border-color: rgba(255, 255, 255, 0.15);
    }

    .card-title {
      font-size: 11.5px;
      color: var(--text-sub);
      font-weight: 500;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .card-val {
      font-family: var(--font-mono);
      font-size: 20px;
      font-weight: 700;
      color: var(--text-main);
      margin-top: 6px;
    }

    .card-val.green { color: var(--accent-green); }
    .card-val.red { color: var(--accent-red); }

    .highlight-cards-row {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 14px;
    }

    .charts-grid-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }

    .chart-card {
      background: var(--desk-card-bg);
      border: 1px solid var(--desk-border);
      border-radius: 12px;
      padding: 18px 20px;
    }

    .chart-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }

    .chart-title-text { font-size: 13.5px; font-weight: 700; color: var(--text-main); }
    .chart-meta-filter {
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 11px;
      color: var(--text-sub);
    }

    .chart-canvas-mock {
      height: 180px;
      position: relative;
      display: flex;
      align-items: flex-end;
      padding-bottom: 24px;
    }

    .chart-grid-line {
      position: absolute;
      left: 0;
      right: 0;
      height: 1px;
      background: rgba(255, 255, 255, 0.04);
    }

    .chart-axis-labels {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      display: flex;
      justify-content: space-between;
      font-size: 10px;
      color: var(--text-dim);
      font-family: var(--font-mono);
    }

    .chart-svg-line {
      width: 100%;
      height: 100%;
      position: absolute;
      top: 0;
      left: 0;
    }

    @media (max-width: 1200px) {
      .number-cards-grid, .highlight-cards-row { grid-template-columns: repeat(3, 1fr); }
      .charts-grid-row { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <!-- Left Sidebar -->
  <aside class="desk-sidebar">
    <a href="#" class="desk-brand-header">
      <div style="display: flex; align-items: center; gap: 8px;">
        <svg width="20" height="20" viewBox="0 0 32 32" fill="none"><rect width="32" height="32" rx="6" fill="#1F3224"/><path d="M7 23L14 9H18L25 23H20.5L18.8 19H13.2L11.5 23H7Z" fill="#00D26A"/></svg>
        <div>
          <div class="brand-title">Oryx Fund</div>
          <div class="brand-sub">Lending Platform</div>
        </div>
      </div>
      <span style="font-size: 11px; color: var(--text-dim);">▼</span>
    </a>

    <div class="sidebar-search-box">
      <span>🔍 Search</span>
      <span class="kbd-shortcut">Ctrl+K</span>
    </div>

    <div class="sidebar-item">
      <span>🔔 Notification</span>
    </div>

    <div class="sidebar-item active">
      <span>📊 Dashboard</span>
    </div>

    <div style="margin-top: 6px;">
      <div class="sidebar-item">
        <span>⚙️ Setup</span>
        <span style="font-size: 10px;">▼</span>
      </div>
      <a class="sidebar-sub-item">Company</a>
      <a class="sidebar-sub-item">Loan Product</a>
      <a class="sidebar-sub-item">Charges</a>
    </div>

    <div style="margin-top: 6px;">
      <div class="sidebar-item">
        <span>📂 Loan Management</span>
        <span style="font-size: 10px;">▼</span>
      </div>
      <a class="sidebar-sub-item">Loan</a>
      <a class="sidebar-sub-item">Loan Disbursement</a>
      <a class="sidebar-sub-item">Loan Repayment Schedule</a>
      <a class="sidebar-sub-item">Loan Transfer</a>
      <a class="sidebar-sub-item">Loan Restructure</a>
      <a class="sidebar-sub-item">Loan Repayment</a>
      <a class="sidebar-sub-item">Loan Demand</a>
      <a class="sidebar-sub-item">Loan Interest Accrual</a>
      <a class="sidebar-sub-item">Loan Write Off</a>
      <a class="sidebar-sub-item">DPD Log</a>
    </div>

    <div style="margin-top: 6px;">
      <div class="sidebar-item">
        <span>👥 Loan Origination</span>
        <span style="font-size: 10px;">▼</span>
      </div>
      <a class="sidebar-sub-item">Customer</a>
      <a class="sidebar-sub-item">Loan Application</a>
    </div>

    <div style="margin-top: 6px;">
      <div class="sidebar-item">
        <span>🔒 Security Management</span>
        <span style="font-size: 10px;">▼</span>
      </div>
      <a class="sidebar-sub-item">Loan Security Type</a>
      <a class="sidebar-sub-item">Loan Security</a>
      <a class="sidebar-sub-item">Loan Security Price</a>
      <a class="sidebar-sub-item">Loan Security Assignment</a>
      <a class="sidebar-sub-item">Loan Security Release</a>
      <a class="sidebar-sub-item">Sanctioned Loan Amount</a>
    </div>

    <div class="sidebar-user-footer">
      <div class="user-avatar-circle">OF</div>
      <div>
        <div style="font-size: 11px; font-weight: 700;">Oryx Fund Admin</div>
        <div style="font-size: 9px; color: var(--text-sub);">admin@oryxfund.co.ke</div>
      </div>
    </div>
  </aside>

  <!-- Main Desk View -->
  <main class="desk-main">
    
    <header class="desk-topbar">
      <div class="breadcrumb-wrap">
        <span>🏠</span>
        <span>/</span>
        <span>Dashboard</span>
        <span>/</span>
        <span class="breadcrumb-current">Loan Dashboard</span>
      </div>

      <div class="topbar-right">
        <button class="theme-icon-btn" onclick="toggleAdminTheme()" id="adminThemeBtn" style="width: 32px; height: 32px; font-size: 14px; background: transparent; border: 1px solid var(--desk-border); color: var(--text-main); cursor: pointer; border-radius: 6px;" title="Toggle Light / Dark Mode">☀️</button>
        <a href="index.html" class="borrower-switch-link">➔ Open Borrower Portal</a>
        <span style="font-size: 14px; color: var(--text-dim); cursor: pointer;">•••</span>
      </div>
    </header>

    <div class="desk-canvas">
      
      <div class="number-cards-grid">
        <div class="number-card">
          <div class="card-title"><span>New Loans</span> <span>•••</span></div>
          <div class="card-val">0</div>
        </div>
        <div class="number-card">
          <div class="card-title"><span>Active Loans</span> <span>•••</span></div>
          <div class="card-val">0</div>
        </div>
        <div class="number-card">
          <div class="card-title"><span>Closed Loans</span> <span>•••</span></div>
          <div class="card-val">0</div>
        </div>
        <div class="number-card">
          <div class="card-title"><span>Total Disbursed</span> <span>•••</span></div>
          <div class="card-val">Sh 0.00</div>
        </div>
        <div class="number-card">
          <div class="card-title"><span>Open Loan Applications</span> <span>•••</span></div>
          <div class="card-val">0</div>
        </div>
      </div>

      <div class="number-cards-grid">
        <div class="number-card">
          <div class="card-title"><span>New Loan Applications</span> <span>•••</span></div>
          <div class="card-val">0</div>
        </div>
        <div class="number-card">
          <div class="card-title"><span>Total Sanctioned Amount</span> <span>•••</span></div>
          <div class="card-val">Sh 0.00</div>
        </div>
        <div class="number-card">
          <div class="card-title"><span>Active Securities</span> <span>•••</span></div>
          <div class="card-val">0</div>
        </div>
        <div class="number-card">
          <div class="card-title"><span>Applicants With Unpaid Shortfall</span> <span>•••</span></div>
          <div class="card-val">0</div>
        </div>
        <div class="number-card">
          <div class="card-title"><span>Total Shortfall Amount</span> <span>•••</span></div>
          <div class="card-val">Sh 0.00</div>
        </div>
      </div>

      <div class="highlight-cards-row">
        <div class="number-card">
          <div class="card-title"><span>Total Repayment</span> <span>•••</span></div>
          <div class="card-val green">Sh 0.00</div>
        </div>
        <div class="number-card">
          <div class="card-title"><span>Total Write Off</span> <span>•••</span></div>
          <div class="card-val red">Sh 0.00</div>
        </div>
      </div>

      <div class="charts-grid-row">
        
        <div class="chart-card">
          <div class="chart-header">
            <div>
              <div class="chart-title-text">New Loans</div>
              <div style="font-size: 10px; color: var(--text-dim); margin-top: 2px;">Last synced just now</div>
            </div>
            <div class="chart-meta-filter">
              <span>📅 Last Month</span>
              <span>:</span>
              <span>Daily</span>
              <span>:</span>
              <span>•••</span>
            </div>
          </div>
          <div class="chart-canvas-mock">
            <div class="chart-grid-line" style="top: 20%;"></div>
            <div class="chart-grid-line" style="top: 50%;"></div>
            <div class="chart-grid-line" style="top: 80%;"></div>
            <svg class="chart-svg-line" viewBox="0 0 500 150">
              <path d="M 0 130 L 500 130" stroke="#00D26A" stroke-width="2" fill="none" opacity="0.6"/>
            </svg>
            <div class="chart-axis-labels">
              <span>26-07-2026</span>
              <span>30-07-2026</span>
              <span>07-08-2026</span>
              <span>15-08-2026</span>
              <span>23-08-2026</span>
              <span>26-08-2026</span>
            </div>
          </div>
        </div>

        <div class="chart-card">
          <div class="chart-header">
            <div>
              <div class="chart-title-text">Loan Disbursements</div>
              <div style="font-size: 10px; color: var(--text-dim); margin-top: 2px;">Last synced just now</div>
            </div>
            <div class="chart-meta-filter">
              <span>📅 Last Month</span>
              <span>:</span>
              <span>Daily</span>
              <span>:</span>
              <span>•••</span>
            </div>
          </div>
          <div class="chart-canvas-mock">
            <div class="chart-grid-line" style="top: 20%;"></div>
            <div class="chart-grid-line" style="top: 50%;"></div>
            <div class="chart-grid-line" style="top: 80%;"></div>
            <svg class="chart-svg-line" viewBox="0 0 500 150">
              <path d="M 0 130 L 500 130" stroke="#00D26A" stroke-width="2" fill="none" opacity="0.6"/>
            </svg>
            <div class="chart-axis-labels">
              <span>26-07-2026</span>
              <span>30-07-2026</span>
              <span>07-08-2026</span>
              <span>15-08-2026</span>
              <span>23-08-2026</span>
              <span>26-08-2026</span>
            </div>
          </div>
        </div>

      </div>

      <div class="charts-grid-row">
        
        <div class="chart-card">
          <div class="chart-header">
            <div>
              <div class="chart-title-text">Top 10 Pledged Loan Securities</div>
              <div style="font-size: 10px; color: var(--text-dim); margin-top: 2px;">Last synced just now</div>
            </div>
            <div class="chart-meta-filter">
              <span>Filter</span>
              <span>•••</span>
            </div>
          </div>
          <div class="chart-canvas-mock">
            <div style="margin: auto; font-size: 12px; color: var(--text-dim);">No pledged securities recorded</div>
          </div>
        </div>

        <div class="chart-card">
          <div class="chart-header">
            <div>
              <div class="chart-title-text">Loan Interest Accrual</div>
              <div style="font-size: 10px; color: var(--text-dim); margin-top: 2px;">Last synced just now</div>
            </div>
            <div class="chart-meta-filter">
              <span>📅 Last Year</span>
              <span>:</span>
              <span>Monthly</span>
              <span>:</span>
              <span>•••</span>
            </div>
          </div>
          <div class="chart-canvas-mock">
            <div class="chart-grid-line" style="top: 20%;"></div>
            <div class="chart-grid-line" style="top: 50%;"></div>
            <div class="chart-grid-line" style="top: 80%;"></div>
            <svg class="chart-svg-line" viewBox="0 0 500 150">
              <path d="M 0 130 L 500 130" stroke="#00D26A" stroke-width="2.5" fill="none"/>
            </svg>
            <div class="chart-axis-labels">
              <span>Aug 2025</span>
              <span>Oct 2025</span>
              <span>Dec 2025</span>
              <span>Feb 2026</span>
              <span>Apr 2026</span>
              <span>Jun 2026</span>
              <span>Aug 2026</span>
            </div>
          </div>
        </div>

      </div>

    </div>
  </main>

  <script>
    function toggleAdminTheme() {
      const html = document.documentElement;
      const cur = html.getAttribute('data-theme') || 'dark';
      const next = cur === 'dark' ? 'light' : 'dark';
      html.setAttribute('data-theme', next);
      html.classList.toggle('dark', next === 'dark');
      document.getElementById('adminThemeBtn').innerText = next === 'dark' ? '☀️' : '🌙';
      localStorage.setItem('oryx_admin_theme', next);
    }
  </script>
</body>
</html>
"""

    with open(f"{base_dir}/index.html", "w") as f:
        f.write(borrower_html)
    with open(f"{base_dir}/my_loans.html", "w") as f:
        f.write(borrower_html)
    with open(f"{base_dir}/borrower.html", "w") as f:
        f.write(borrower_html)
    with open(f"{base_dir}/apply.html", "w") as f:
        f.write(apply_html)
    with open(f"{base_dir}/my_account.html", "w") as f:
        f.write(account_html)
    with open(f"{base_dir}/admin.html", "w") as f:
        f.write(admin_html)
    with open(f"{base_dir}/desk.html", "w") as f:
        f.write(admin_html)

    print("Complete static site written successfully!")

if __name__ == '__main__':
    create_complete_static_site()

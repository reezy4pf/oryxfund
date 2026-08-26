import os

base_dir = "/home/reezy/.gemini/antigravity-ide/scratch/oryx_fund"

# 1. LOGIN HTML
login_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login — Oryx Fund</title>
  <meta name="description" content="Secure authentication portal for Oryx Fund borrowers and administrators.">
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
      --card-shadow: 0 8px 32px rgba(31, 50, 36, 0.08);
      --font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'IBM Plex Mono', monospace;
    }

    [data-theme="dark"], html.dark {
      --bg-page: #09090B;
      --bg-surface: #121215;
      --bg-surface-alt: #16221A;
      --border-color: #1F3325;
      --border-light: #18281D;
      --text-primary: #FAF8F5;
      --text-secondary: #9DB4A5;
      --text-muted: #667D6F;
      --primary: #00D26A;
      --accent-green: #00D26A;
      --accent-emerald: #00D26A;
      --card-shadow: 0 8px 40px rgba(0, 0, 0, 0.5);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; transition: background-color 0.2s, border-color 0.2s, color 0.2s; }

    body {
      font-family: var(--font-body);
      background-color: var(--bg-page);
      color: var(--text-primary);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .login-container {
      max-width: 440px;
      width: 100%;
    }

    .auth-brand-head {
      text-align: center;
      margin-bottom: 24px;
    }

    .auth-brand-logo {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 8px;
      text-decoration: none;
      color: var(--text-primary);
    }

    .auth-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 18px;
      padding: 32px 30px;
      box-shadow: var(--card-shadow);
    }

    .role-tabs {
      display: flex;
      background: var(--bg-surface-alt);
      padding: 4px;
      border-radius: 12px;
      border: 1px solid var(--border-color);
      margin-bottom: 22px;
    }

    .role-tab-btn {
      flex: 1;
      text-align: center;
      padding: 8px 12px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      background: transparent;
      border: none;
      color: var(--text-secondary);
    }

    .role-tab-btn.active {
      background: var(--bg-surface);
      color: var(--text-primary);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    [data-theme="dark"] .role-tab-btn.active {
      background: var(--accent-emerald);
      color: #000000;
    }

    .quick-creds-banner {
      background: rgba(0, 210, 106, 0.08);
      border: 1px dashed var(--accent-emerald);
      border-radius: 10px;
      padding: 10px 14px;
      margin-bottom: 20px;
      font-size: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .quick-fill-btn {
      background: var(--primary);
      color: #FFF !important;
      border: none;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      cursor: pointer;
    }
    [data-theme="dark"] .quick-fill-btn {
      background: var(--accent-emerald);
      color: #000 !important;
    }

    .form-group { margin-bottom: 16px; }

    .form-label {
      display: block;
      font-size: 12px;
      font-weight: 700;
      color: var(--text-muted);
      margin-bottom: 6px;
    }

    .form-input {
      width: 100%;
      padding: 11px 14px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: var(--bg-surface-alt);
      color: var(--text-primary);
      font-size: 14px;
      font-family: var(--font-body);
      outline: none;
    }

    .form-input:focus {
      border-color: var(--accent-emerald);
      box-shadow: 0 0 0 3px rgba(0, 210, 106, 0.15);
    }

    .btn-submit {
      width: 100%;
      padding: 12px 20px;
      border-radius: 8px;
      border: none;
      background: var(--primary);
      color: #FFFFFF !important;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      margin-top: 8px;
      box-shadow: 0 4px 12px rgba(31, 50, 36, 0.2);
    }

    [data-theme="dark"] .btn-submit {
      background: var(--accent-emerald);
      color: #000000 !important;
      box-shadow: 0 4px 15px rgba(0, 210, 106, 0.35);
    }

    .btn-submit:hover { transform: translateY(-1px); }

    .auth-footer {
      text-align: center;
      margin-top: 20px;
      font-size: 12px;
      color: var(--text-muted);
    }
  </style>
</head>
<body>

  <div class="login-container">
    
    <div class="auth-brand-head">
      <a href="index.html" class="auth-brand-logo">
        <svg width="34" height="34" viewBox="0 0 32 32" fill="none">
          <rect width="32" height="32" rx="8" fill="#1F3224"/>
          <path d="M7 23L14 9H18L25 23H20.5L18.8 19H13.2L11.5 23H7ZM14.3 16.5H17.7L16 12.5L14.3 16.5Z" fill="#00D26A"/>
        </svg>
        <span style="font-size: 20px; font-weight: 800;">Oryx <span style="font-size: 13px; font-weight: 700; color: var(--text-muted);">Fund</span></span>
      </a>
      <p style="font-size: 13px; color: var(--text-secondary);">Enterprise Credit &amp; Institutional Lending Engine</p>
    </div>

    <div class="auth-card">
      
      <div class="role-tabs">
        <button type="button" class="role-tab-btn active" id="tabBorrower" onclick="setRole('borrower')">👤 Borrower Login</button>
        <button type="button" class="role-tab-btn" id="tabAdmin" onclick="setRole('admin')">🛡️ Admin Desk</button>
      </div>

      <div class="quick-creds-banner">
        <div>
          <span style="font-weight: 800;" id="quickLabel">Test Borrower:</span>
          <span style="font-family: var(--font-mono); margin-left: 4px;" id="quickEmail">reezyhoops@gmail.com</span>
        </div>
        <button type="button" class="quick-fill-btn" onclick="quickFill()">Quick-Fill</button>
      </div>

      <form id="loginForm" onsubmit="handleLogin(event)">
        <div class="form-group">
          <label class="form-label" for="loginEmail">Email / Phone Number</label>
          <input type="text" id="loginEmail" class="form-input" placeholder="e.g. reezyhoops@gmail.com" required value="reezyhoops@gmail.com">
        </div>

        <div class="form-group">
          <div style="display: flex; justify-content: space-between;">
            <label class="form-label" for="loginPassword">Password</label>
            <a href="#" style="font-size: 11px; color: var(--accent-green); text-decoration: none; font-weight: 700;">Forgot?</a>
          </div>
          <input type="password" id="loginPassword" class="form-input" placeholder="••••••••" required value="password123">
        </div>

        <button type="submit" class="btn-submit" id="submitBtn">
          ⚡ Sign In to Borrower Portal
        </button>
      </form>

    </div>

    <div class="auth-footer">
      <p>© 2026 Oryx Fund. All Rights Reserved. • <button onclick="toggleTheme()" style="background:none; border:none; color:var(--text-secondary); cursor:pointer; font-weight:700;">Toggle ☀️ / 🌙 Theme</button></p>
    </div>

  </div>

  <script>
    let currentRole = 'borrower';

    function setRole(role) {
      currentRole = role;
      document.getElementById('tabBorrower').classList.toggle('active', role === 'borrower');
      document.getElementById('tabAdmin').classList.toggle('active', role === 'admin');
      
      if (role === 'borrower') {
        document.getElementById('quickLabel').innerText = 'Test Borrower:';
        document.getElementById('quickEmail').innerText = 'reezyhoops@gmail.com';
        document.getElementById('loginEmail').value = 'reezyhoops@gmail.com';
        document.getElementById('submitBtn').innerText = '⚡ Sign In to Borrower Portal';
      } else {
        document.getElementById('quickLabel').innerText = 'Admin User:';
        document.getElementById('quickEmail').innerText = 'admin@oryxfund.co.ke';
        document.getElementById('loginEmail').value = 'admin@oryxfund.co.ke';
        document.getElementById('submitBtn').innerText = '🛡️ Sign In to Admin Desk';
      }
    }

    function quickFill() {
      if (currentRole === 'borrower') {
        document.getElementById('loginEmail').value = 'reezyhoops@gmail.com';
        document.getElementById('loginPassword').value = 'password123';
      } else {
        document.getElementById('loginEmail').value = 'admin@oryxfund.co.ke';
        document.getElementById('loginPassword').value = 'admin';
      }
    }

    function handleLogin(e) {
      e.preventDefault();
      const email = document.getElementById('loginEmail').value.trim();
      const user = {
        email: email,
        name: email.includes('admin') ? 'Oryx Fund Admin' : 'Reezy Mwangi',
        role: email.includes('admin') ? 'Administrator' : 'Borrower'
      };
      localStorage.setItem('oryx_auth_user', JSON.stringify(user));

      if (user.role === 'Administrator') {
        window.location.href = 'admin.html';
      } else {
        window.location.href = 'index.html';
      }
    }

    function toggleTheme() {
      const html = document.documentElement;
      const cur = html.getAttribute('data-theme') || 'light';
      const next = cur === 'light' ? 'dark' : 'light';
      html.setAttribute('data-theme', next);
      localStorage.setItem('oryx_theme', next);
    }
    const saved = localStorage.getItem('oryx_theme');
    if (saved) document.documentElement.setAttribute('data-theme', saved);
  </script>
</body>
</html>
"""

# 2. BORROWER PORTAL HTML
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
      --bg-page: #09090B;
      --bg-surface: #121215;
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
      --hero-bg: #121215;
      --hero-text: #FAF8F5;
      --card-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; transition: background-color 0.2s, border-color 0.2s, color 0.2s; }

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

    .hero-title { font-size: 24px; font-weight: 800; letter-spacing: -0.3px; margin-bottom: 6px; }
    .hero-desc { font-size: 13.5px; color: #B4C6BA; max-width: 520px; line-height: 1.45; }
    .hero-account-badge { font-size: 12px; color: #9DB4A5; margin-bottom: 12px; text-align: right; }

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
    }

    .oryx-subsequent-cta-card {
      background: linear-gradient(135deg, var(--bg-surface) 0%, rgba(0, 210, 106, 0.08) 100%);
      border: 1.5px solid #00D26A;
      border-radius: 16px;
      padding: 20px 26px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      box-shadow: var(--card-shadow);
    }

    .s-cta-badge { font-size: 10px; font-weight: 800; color: #059669; letter-spacing: 0.8px; }
    [data-theme="dark"] .s-cta-badge { color: #00D26A; }
    .s-cta-title { font-size: 18px; font-weight: 700; color: var(--text-primary); margin: 4px 0; }
    .s-cta-desc { font-size: 13px; color: var(--text-secondary); max-width: 580px; }

    .oryx-btn-express {
      background: linear-gradient(135deg, #00D26A 0%, #059669 100%) !important;
      color: #000000 !important;
      font-weight: 800 !important;
      font-size: 13px;
      padding: 10px 20px;
      border-radius: 8px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 4px 14px rgba(0, 210, 106, 0.35) !important;
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

    .stat-label { font-size: 10.5px; font-weight: 800; color: var(--text-muted); letter-spacing: 0.6px; text-transform: uppercase; }
    .stat-number { font-family: var(--font-mono); font-size: 20px; font-weight: 700; color: var(--text-primary); margin-top: 2px; }

    .portal-section-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 24px 28px;
      box-shadow: var(--card-shadow);
    }

    .card-head-title { font-size: 17px; font-weight: 700; color: var(--text-primary); }
    .card-head-desc { font-size: 13px; color: var(--text-secondary); margin-top: 2px; padding-bottom: 16px; border-bottom: 1px solid var(--border-light); }

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

    .empty-title { font-size: 16px; font-weight: 700; color: var(--text-primary); margin-bottom: 6px; }
    .empty-desc { font-size: 13px; color: var(--text-secondary); max-width: 440px; margin-bottom: 18px; line-height: 1.45; }

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
      <a href="my_account.html" class="nav-pill-btn nav-pill-light" id="navUserPill">👤 Reezy</a>
      <button class="theme-icon-btn" onclick="toggleTheme()" id="themeBtn" title="Toggle Light / Dark Mode">🌙</button>
      <a href="admin.html" class="admin-switch-btn" title="View Admin Desk">🛡️ Admin Link</a>
      <a href="login.html" class="admin-switch-btn" style="color:#E57373;" title="Switch Account / Sign Out">Switch Account</a>
    </div>
  </header>

  <main class="portal-container">

    <div class="portal-hero-card">
      <div>
        <span class="hero-pill-tag">MY PORTAL</span>
        <h1 class="hero-title">My Loans &amp; Repayments</h1>
        <p class="hero-desc">View your active loans, outstanding balances, and official M-Pesa Paybill payment instructions.</p>
      </div>
      <div>
        <div class="hero-account-badge" id="heroAccountText">Account: reezyhoops@gmail.com</div>
        <a href="apply.html" class="hero-apply-btn">+ Apply for a New Loan</a>
      </div>
    </div>

    <!-- Express Repeat Banner for Verified Returning Borrowers -->
    <div class="oryx-subsequent-cta-card">
      <div>
        <div class="s-cta-badge">⚡ EXPRESS REPEAT FACILITY</div>
        <h3 class="s-cta-title">Fast-Track Subsequent Loan</h3>
        <p class="s-cta-desc">Apply for a new advance using your existing verified profile. Fast underwriting with direct M-Pesa disbursal.</p>
      </div>
      <a href="apply.html?flow=express" class="oryx-btn-express">⚡ Apply in 60 Seconds ➔</a>
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

    try {
      const auth = JSON.parse(localStorage.getItem('oryx_auth_user'));
      if (auth && auth.email) {
        document.getElementById('heroAccountText').innerText = 'Account: ' + auth.email;
        document.getElementById('navUserPill').innerText = '👤 ' + (auth.name || auth.email.split('@')[0]);
      }
    } catch(e) {}
  </script>
</body>
</html>
"""

# Read existing apply_html, account_html, admin_html from disk or previous definitions
with open(f"{base_dir}/apply.html", "r") as f:
    apply_html = f.read()
with open(f"{base_dir}/my_account.html", "r") as f:
    account_html = f.read()
with open(f"{base_dir}/admin.html", "r") as f:
    admin_html = f.read()

# Write all pages
with open(f"{base_dir}/login.html", "w") as f:
    f.write(login_html)
with open(f"{base_dir}/index.html", "w") as f:
    f.write(borrower_html)
with open(f"{base_dir}/my_loans.html", "w") as f:
    f.write(borrower_html)
with open(f"{base_dir}/borrower.html", "w") as f:
    f.write(borrower_html)

print("Generated all files successfully!")

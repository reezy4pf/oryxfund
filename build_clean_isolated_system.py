import os

def generate_clean_isolated_system():
    base_dir = "/home/reezy/.gemini/antigravity-ide/scratch/oryx_fund"

    # =========================================================================
    # 1. LOGIN & REGISTRATION (login.html)
    # =========================================================================
    login_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Borrower Portal — Oryx Fund</title>
  <meta name="description" content="Secure borrower authentication and registration for Oryx Fund digital credit.">
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
      --primary-hover: #2D4834;
      --accent-green: #059669;
      --accent-emerald: #00D26A;
      --card-shadow: 0 8px 32px rgba(31, 50, 36, 0.08);
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
      --primary-hover: #00FF80;
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
      padding: 24px 16px;
    }

    .auth-box {
      max-width: 460px;
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

    .auth-tabs {
      display: flex;
      background: var(--bg-surface-alt);
      padding: 4px;
      border-radius: 12px;
      border: 1px solid var(--border-color);
      margin-bottom: 24px;
    }

    .tab-btn {
      flex: 1;
      text-align: center;
      padding: 9px 12px;
      border-radius: 8px;
      font-size: 13.5px;
      font-weight: 700;
      cursor: pointer;
      background: transparent;
      border: none;
      color: var(--text-secondary);
    }

    .tab-btn.active {
      background: var(--bg-surface);
      color: var(--text-primary);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }

    [data-theme="dark"] .tab-btn.active {
      background: var(--accent-emerald);
      color: #000000;
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

    .form-grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
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

    .auth-note {
      font-size: 11.5px;
      color: var(--text-muted);
      margin-top: 14px;
      text-align: center;
      line-height: 1.4;
    }

    .auth-footer {
      text-align: center;
      margin-top: 24px;
      font-size: 12px;
      color: var(--text-muted);
    }

    .status-alert {
      padding: 10px 14px;
      border-radius: 8px;
      font-size: 12.5px;
      margin-bottom: 16px;
      display: none;
    }
    .status-alert.error {
      background: rgba(220, 38, 38, 0.1);
      color: #DC2626;
      border: 1px solid rgba(220, 38, 38, 0.2);
    }
    .status-alert.success {
      background: rgba(0, 210, 106, 0.1);
      color: #059669;
      border: 1px solid rgba(0, 210, 106, 0.2);
    }
  </style>
</head>
<body>

  <div class="auth-box">
    
    <div class="auth-brand-head">
      <a href="index.html" class="auth-brand-logo">
        <svg width="34" height="34" viewBox="0 0 32 32" fill="none">
          <rect width="32" height="32" rx="8" fill="#1F3224"/>
          <path d="M7 23L14 9H18L25 23H20.5L18.8 19H13.2L11.5 23H7ZM14.3 16.5H17.7L16 12.5L14.3 16.5Z" fill="#00D26A"/>
        </svg>
        <span style="font-size: 20px; font-weight: 800;">Oryx <span style="font-size: 13px; font-weight: 700; color: var(--text-muted);">Fund</span></span>
      </a>
      <p style="font-size: 13px; color: var(--text-secondary);">Borrower Self-Service &amp; Digital Credit Portal</p>
    </div>

    <div class="auth-card">
      
      <div class="auth-tabs">
        <button type="button" class="tab-btn active" id="tabLogin" onclick="switchAuthTab('login')">🔑 Sign In</button>
        <button type="button" class="tab-btn" id="tabRegister" onclick="switchAuthTab('register')">✨ Create Account</button>
      </div>

      <div id="statusAlert" class="status-alert"></div>

      <!-- 1. SIGN IN FORM -->
      <form id="signInForm" onsubmit="handleSignIn(event)">
        <div class="form-group">
          <label class="form-label" for="loginIdentifier">Email or Mobile Number</label>
          <input type="text" id="loginIdentifier" class="form-input" placeholder="e.g. name@domain.com or +2547XXXXXXXX" required autofocus>
        </div>

        <div class="form-group">
          <div style="display: flex; justify-content: space-between;">
            <label class="form-label" for="loginPass">Password</label>
            <a href="javascript:void(0)" onclick="alert('Password reset link sent to your registered email.')" style="font-size: 11px; color: var(--accent-green); text-decoration: none; font-weight: 700;">Forgot Password?</a>
          </div>
          <input type="password" id="loginPass" class="form-input" placeholder="••••••••" required>
        </div>

        <button type="submit" class="btn-submit">
          Sign In to My Portal
        </button>

        <p class="auth-note">
          New to Oryx Fund? <a href="javascript:void(0)" onclick="switchAuthTab('register')" style="color: var(--accent-green); font-weight: 700; text-decoration: none;">Create a fresh account</a> to apply in minutes.
        </p>
      </form>

      <!-- 2. REGISTER FRESH ACCOUNT FORM -->
      <form id="registerForm" onsubmit="handleRegister(event)" style="display: none;">
        <div class="form-group">
          <label class="form-label" for="regFullName">Full Legal Name (as on ID)</label>
          <input type="text" id="regFullName" class="form-input" placeholder="e.g. John Kamau Mwangi" required>
        </div>

        <div class="form-grid-2">
          <div class="form-group">
            <label class="form-label" for="regEmail">Email Address</label>
            <input type="email" id="regEmail" class="form-input" placeholder="john@example.com" required>
          </div>
          <div class="form-group">
            <label class="form-label" for="regPhone">Mobile Phone (M-Pesa)</label>
            <input type="tel" id="regPhone" class="form-input" placeholder="+254712345678" required>
          </div>
        </div>

        <div class="form-group">
          <label class="form-label" for="regNationalId">National ID Number</label>
          <input type="text" id="regNationalId" class="form-input" placeholder="e.g. 29384756" required>
        </div>

        <div class="form-grid-2">
          <div class="form-group">
            <label class="form-label" for="regPass">Create Password</label>
            <input type="password" id="regPass" class="form-input" placeholder="Min. 6 chars" required minlength="6">
          </div>
          <div class="form-group">
            <label class="form-label" for="regPassConfirm">Confirm Password</label>
            <input type="password" id="regPassConfirm" class="form-input" placeholder="Repeat password" required minlength="6">
          </div>
        </div>

        <div style="margin-bottom: 16px; font-size: 11.5px; color: var(--text-secondary); display: flex; align-items: flex-start; gap: 8px;">
          <input type="checkbox" id="termsCheck" required style="margin-top: 2px;">
          <label for="termsCheck">I certify that my details are accurate and agree to Oryx Fund Credit Terms &amp; KYC Verification.</label>
        </div>

        <button type="submit" class="btn-submit">
          ✨ Create Secure Account &amp; Continue ➔
        </button>

        <p class="auth-note">
          Already registered? <a href="javascript:void(0)" onclick="switchAuthTab('login')" style="color: var(--accent-green); font-weight: 700; text-decoration: none;">Sign In here</a>.
        </p>
      </form>

    </div>

    <div class="auth-footer">
      <p>© 2026 Oryx Fund. All Rights Reserved. • <button onclick="toggleTheme()" style="background:none; border:none; color:var(--text-secondary); cursor:pointer; font-weight:700;">Toggle ☀️ / 🌙 Theme</button></p>
    </div>

  </div>

  <script>
    function switchAuthTab(tab) {
      document.getElementById('tabLogin').classList.toggle('active', tab === 'login');
      document.getElementById('tabRegister').classList.toggle('active', tab === 'register');
      document.getElementById('signInForm').style.display = tab === 'login' ? 'block' : 'none';
      document.getElementById('registerForm').style.display = tab === 'register' ? 'block' : 'none';
      document.getElementById('statusAlert').style.display = 'none';
    }

    function showAlert(msg, isError = true) {
      const alertBox = document.getElementById('statusAlert');
      alertBox.className = 'status-alert ' + (isError ? 'error' : 'success');
      alertBox.innerText = msg;
      alertBox.style.display = 'block';
    }

    function handleRegister(e) {
      e.preventDefault();
      const name = document.getElementById('regFullName').value.trim();
      const email = document.getElementById('regEmail').value.trim().toLowerCase();
      const phone = document.getElementById('regPhone').value.trim();
      const nationalId = document.getElementById('regNationalId').value.trim();
      const pass = document.getElementById('regPass').value;
      const passConfirm = document.getElementById('regPassConfirm').value;

      if (pass !== passConfirm) {
        showAlert('Passwords do not match. Please re-enter.');
        return;
      }

      // Fresh Isolated Borrower Account
      const newBorrower = {
        name: name,
        email: email,
        phone: phone,
        nationalId: nationalId,
        role: 'Borrower',
        created_at: new Date().toISOString(),
        active_loans: 0,
        total_principal: 0,
        outstanding_balance: 0,
        applications: []
      };

      // Save to isolated account key
      localStorage.setItem('oryx_borrower_' + email, JSON.stringify(newBorrower));
      // Set as active session
      localStorage.setItem('oryx_auth_user', JSON.stringify(newBorrower));

      showAlert('✨ Account created successfully! Redirecting...', false);
      setTimeout(() => {
        window.location.href = 'index.html';
      }, 800);
    }

    function handleSignIn(e) {
      e.preventDefault();
      const ident = document.getElementById('loginIdentifier').value.trim().toLowerCase();
      
      // Check if this borrower account exists locally
      let user = null;
      try {
        const stored = localStorage.getItem('oryx_borrower_' + ident);
        if (stored) {
          user = JSON.parse(stored);
        }
      } catch(err) {}

      if (!user) {
        // Create an on-demand clean borrower session for this email
        user = {
          name: ident.includes('@') ? ident.split('@')[0] : 'Borrower',
          email: ident,
          phone: ident.startsWith('+') ? ident : '+254700000000',
          nationalId: 'Pending KYC',
          role: 'Borrower',
          active_loans: 0,
          total_principal: 0,
          outstanding_balance: 0,
          applications: []
        };
        localStorage.setItem('oryx_borrower_' + ident, JSON.stringify(user));
      }

      localStorage.setItem('oryx_auth_user', JSON.stringify(user));
      window.location.href = 'index.html';
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

    # =========================================================================
    # 2. BORROWER PORTAL (index.html, my_loans.html, borrower.html)
    # (Completely Clean, NO Admin Desk Links, Dynamic Isolated Session)
    # =========================================================================
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

    .nav-pill-light:hover {
      border-color: var(--accent-emerald);
      transform: translateY(-1px);
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

    .signout-btn {
      background: transparent;
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 700;
      cursor: pointer;
    }
    .signout-btn:hover {
      color: #DC2626;
      border-color: #DC2626;
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

  <!-- Borrower Navbar: ZERO Admin Links -->
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
      <a href="apply.html" class="nav-pill-btn nav-pill-light">+ Apply</a>
      <a href="my_account.html" class="nav-pill-btn nav-pill-light" id="navUserPill">👤 My Account</a>
      <button class="theme-icon-btn" onclick="toggleTheme()" id="themeBtn" title="Toggle Light / Dark Mode">🌙</button>
      <button onclick="logoutBorrower()" class="signout-btn" id="signOutBtn" title="Log Out of Borrower Account">Sign Out</button>
    </div>
  </header>

  <!-- Borrower Main View -->
  <main class="portal-container">

    <div class="portal-hero-card">
      <div>
        <span class="hero-pill-tag">BORROWER PORTAL</span>
        <h1 class="hero-title">My Loans &amp; Repayments</h1>
        <p class="hero-desc">View your active loans, outstanding balances, and official M-Pesa Paybill payment instructions.</p>
      </div>
      <div>
        <div class="hero-account-badge" id="heroAccountText">Account: Guest</div>
        <a href="apply.html" class="hero-apply-btn">+ Apply for a New Loan</a>
      </div>
    </div>

    <!-- 3 KPI Cards -->
    <div class="stats-kpi-row">
      <div class="stat-kpi-card">
        <div class="stat-icon-capsule">💼</div>
        <div>
          <div class="stat-label">Active Loans</div>
          <div class="stat-number" id="statActiveLoans">0</div>
        </div>
      </div>
      <div class="stat-kpi-card">
        <div class="stat-icon-capsule">💲</div>
        <div>
          <div class="stat-label">Total Principal Borrowed</div>
          <div class="stat-number" id="statPrincipal">KES 0.00</div>
        </div>
      </div>
      <div class="stat-kpi-card">
        <div class="stat-icon-capsule">⏱️</div>
        <div>
          <div class="stat-label">Outstanding Balance</div>
          <div class="stat-number" id="statOutstanding">KES 0.00</div>
        </div>
      </div>
    </div>

    <!-- Active Loans Section -->
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

    <!-- Application History Section -->
    <section class="portal-section-card">
      <h2 class="card-head-title">Application History</h2>
      <p class="card-head-desc">Track status and review records of all submitted loan applications.</p>
      
      <div class="empty-state-wrap" id="appsContainer">
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

    function logoutBorrower() {
      localStorage.removeItem('oryx_auth_user');
      window.location.href = 'login.html';
    }

    // Load active session
    document.addEventListener('DOMContentLoaded', () => {
      try {
        const user = JSON.parse(localStorage.getItem('oryx_auth_user'));
        if (user && user.email) {
          document.getElementById('heroAccountText').innerText = 'Account: ' + user.email;
          document.getElementById('navUserPill').innerText = '👤 ' + (user.name || user.email.split('@')[0]);
          document.getElementById('signOutBtn').style.display = 'inline-block';
        } else {
          document.getElementById('heroAccountText').innerText = 'Account: Not Signed In';
          document.getElementById('navUserPill').innerHTML = '🔑 Sign In';
          document.getElementById('navUserPill').href = 'login.html';
          document.getElementById('signOutBtn').style.display = 'none';
        }
      } catch(e) {}
    });
  </script>
</body>
</html>
"""

    # =========================================================================
    # 3. LOAN APPLICATION (apply.html)
    # (Clean Borrower KYC, Dynamic Pre-fill, NO Admin Desk Links)
    # =========================================================================
    apply_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Loan Application — Oryx Fund</title>
  <meta name="description" content="Instant digital loan application portal for Oryx Fund.">
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

    * { box-sizing: border-box; margin: 0; padding: 0; transition: background-color 0.2s, border-color 0.2s, color 0.2s; }

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

    .apply-hero-bar {
      background: linear-gradient(135deg, #1F3224 0%, #101B13 100%);
      color: #FAF8F5;
      padding: 28px 32px;
      border-radius: 18px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: var(--card-shadow);
    }
    [data-theme="dark"] .apply-hero-bar {
      background: linear-gradient(135deg, #101712 0%, #080D0A 100%);
      border: 1px solid var(--border-color);
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
      margin-top: 14px;
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

    .hud-title { font-size: 10.5px; font-weight: 800; color: var(--text-muted); text-transform: uppercase; }
    .hud-number { font-family: var(--font-mono); font-size: 17px; font-weight: 700; color: var(--text-primary); margin-top: 4px; }

    .form-group { margin-bottom: 16px; }
    .form-label { display: block; font-size: 12px; font-weight: 700; color: var(--text-muted); margin-bottom: 4px; }
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

    .form-grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
    }

    .btn-submit-app {
      background: linear-gradient(135deg, #00D26A 0%, #059669 100%) !important;
      color: #000000 !important;
      font-weight: 800 !important;
      font-size: 14.5px;
      padding: 13px 28px;
      border-radius: 8px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 4px 14px rgba(0, 210, 106, 0.35) !important;
      cursor: pointer;
      border: none;
    }

    @media (max-width: 768px) {
      .metrics-live-hud, .form-grid-3 { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <!-- Borrower Navbar: ZERO Admin Links -->
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
      <a href="my_account.html" class="nav-pill-btn nav-pill-light" id="navUserPill">👤 My Account</a>
      <button class="theme-icon-btn" onclick="toggleTheme()" id="themeBtn" title="Toggle Light / Dark Mode">🌙</button>
    </div>
  </header>

  <main class="apply-container">

    <div class="apply-hero-bar">
      <div>
        <span style="background: rgba(0, 210, 106, 0.15); border: 1px solid #00D26A; color: #00D26A; font-size: 10.5px; font-weight: 800; padding: 4px 10px; border-radius: 12px; display: inline-block; margin-bottom: 6px;">DIGITAL APPLICATION</span>
        <h1 style="font-size: 24px; font-weight: 800;">Apply for an Oryx Credit Facility</h1>
        <p style="font-size: 13px; color: #B4C6BA;">Complete your loan terms and disbursal preferences below.</p>
      </div>
      <div style="text-align: right;">
        <div style="font-size: 11px; color: #9DB4A5; font-weight: 700; text-transform: uppercase;">Average Decision</div>
        <div style="font-family: var(--font-mono); font-size: 22px; font-weight: 700; color: #00D26A;">Same Day</div>
      </div>
    </div>

    <!-- 1. Facility Terms Card -->
    <section class="oryx-card">
      <h2 style="font-size: 18px; font-weight: 700;">1. Facility Terms &amp; Amortization</h2>
      <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 12px;">Adjust the requested principal amount and view real-time installment calculations.</p>

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
            <div class="hud-title">Est. Interest (14% p.a.)</div>
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
    </section>

    <!-- 2. Borrower Verification Details -->
    <section class="oryx-card">
      <h2 style="font-size: 18px; font-weight: 700; margin-bottom: 4px;">2. Borrower KYC &amp; Contact Details</h2>
      <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 18px;">Your registered borrower information is securely linked to this application.</p>

      <div class="form-grid-3">
        <div class="form-group">
          <label class="form-label">Full Legal Name</label>
          <input type="text" id="appFullName" class="form-control" placeholder="Enter Full Name" required>
        </div>
        <div class="form-group">
          <label class="form-label">Email Address</label>
          <input type="email" id="appEmail" class="form-control" placeholder="name@example.com" required>
        </div>
        <div class="form-group">
          <label class="form-label">Mobile Number</label>
          <input type="tel" id="appPhone" class="form-control" placeholder="+2547XXXXXXXX" required>
        </div>
      </div>

      <div class="form-grid-3">
        <div class="form-group">
          <label class="form-label">National ID Number</label>
          <input type="text" id="appNationalId" class="form-control" placeholder="National ID" required>
        </div>
        <div class="form-group">
          <label class="form-label">Employer / Business Name</label>
          <input type="text" id="appEmployer" class="form-control" placeholder="e.g. Acme Enterprise" required>
        </div>
        <div class="form-group">
          <label class="form-label">Monthly Net Income (KES)</label>
          <input type="number" id="appIncome" class="form-control" placeholder="e.g. 150000" required>
        </div>
      </div>
    </section>

    <!-- 3. Disbursal Preferences -->
    <section class="oryx-card">
      <h2 style="font-size: 18px; font-weight: 700; margin-bottom: 4px;">3. Direct Disbursal Preferences</h2>
      <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 18px;">Designate the payout route where loan funds will be disbursed upon approval.</p>

      <div class="form-grid-3">
        <div class="form-group">
          <label class="form-label">Disbursement Route</label>
          <select class="form-control" id="appDisbursalMethod">
            <option value="M-Pesa">M-Pesa Direct Payout</option>
            <option value="Bank Transfer">Bank Wire (EFT / RTGS)</option>
          </select>
        </div>
        <div class="form-group">
          <label class="form-label">M-Pesa Number / Account</label>
          <input type="text" id="appDisbursalAccount" class="form-control" placeholder="+2547XXXXXXXX" required>
        </div>
      </div>

      <div style="margin-top: 24px; display: flex; justify-content: flex-end;">
        <button type="button" class="btn-submit-app" onclick="submitLoanApplication()">
          🚀 Submit Loan Application for Underwriting
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

    // Populate user from active session if logged in
    document.addEventListener('DOMContentLoaded', () => {
      try {
        const user = JSON.parse(localStorage.getItem('oryx_auth_user'));
        if (user) {
          if (user.name && user.name !== 'Borrower') document.getElementById('appFullName').value = user.name;
          if (user.email) {
            document.getElementById('appEmail').value = user.email;
            document.getElementById('navUserPill').innerText = '👤 ' + (user.name || user.email.split('@')[0]);
          }
          if (user.phone) {
            document.getElementById('appPhone').value = user.phone;
            document.getElementById('appDisbursalAccount').value = user.phone;
          }
          if (user.nationalId && user.nationalId !== 'Pending KYC') {
            document.getElementById('appNationalId').value = user.nationalId;
          }
        }
      } catch(e) {}
    });

    function submitLoanApplication() {
      const amount = document.getElementById('hudPrincipal').innerText;
      const name = document.getElementById('appFullName').value.trim();
      const email = document.getElementById('appEmail').value.trim();

      if (!name || !email) {
        alert('Please provide your Full Legal Name and Email to submit.');
        return;
      }

      alert('🎉 Application for ' + amount + ' submitted successfully! Our credit team is reviewing your file.');
      window.location.href = 'index.html';
    }
  </script>
</body>
</html>
"""

    # =========================================================================
    # 4. BORROWER PROFILE & ACCOUNT (my_account.html)
    # (Completely Clean, NO Admin Desk Links)
    # =========================================================================
    account_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Account — Oryx Fund</title>
  <meta name="description" content="Manage your personal KYC, disbursement preferences, and security settings.">
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

    * { box-sizing: border-box; margin: 0; padding: 0; transition: background-color 0.2s, border-color 0.2s, color 0.2s; }

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

    .form-group { margin-bottom: 16px; }
    .form-label { font-size: 12px; font-weight: 700; color: var(--text-muted); display: block; margin-bottom: 4px; }
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

    .btn-save {
      background: var(--primary);
      color: #FFF !important;
      font-weight: 700;
      font-size: 13.5px;
      padding: 10px 20px;
      border-radius: 8px;
      border: none;
      cursor: pointer;
    }
    [data-theme="dark"] .btn-save {
      background: var(--accent-emerald);
      color: #000 !important;
    }

    @media (max-width: 768px) {
      .account-layout { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <!-- Borrower Navbar: ZERO Admin Links -->
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
      <a href="my_account.html" class="nav-pill-btn nav-pill-active" id="navUserPill">👤 My Account</a>
      <button class="theme-icon-btn" onclick="toggleTheme()" id="themeBtn" title="Toggle Light / Dark Mode">🌙</button>
      <button onclick="logoutBorrower()" style="background:none; border:1px solid var(--border-color); color:var(--text-muted); padding:6px 14px; border-radius:20px; font-size:12px; font-weight:700; cursor:pointer;">Sign Out</button>
    </div>
  </header>

  <main class="account-layout">
    
    <div>
      <section class="oryx-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
          <div>
            <h2 style="font-size: 18px; font-weight: 700;">Personal &amp; Contact Details</h2>
            <p style="font-size: 12.5px; color: var(--text-secondary);">Your verified KYC details used for identity assessment.</p>
          </div>
          <span style="background: rgba(0, 210, 106, 0.12); color: var(--accent-green); font-size: 12px; font-weight: 800; padding: 4px 12px; border-radius: 20px;">✓ Protected Profile</span>
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
          <div class="form-group">
            <label class="form-label">Full Legal Name</label>
            <input type="text" class="form-control" id="accName" placeholder="Enter Full Name">
          </div>
          <div class="form-group">
            <label class="form-label">Email Address</label>
            <input type="email" class="form-control" id="accEmail" readonly>
          </div>
          <div class="form-group">
            <label class="form-label">Mobile Number (M-Pesa)</label>
            <input type="tel" class="form-control" id="accPhone" placeholder="+2547XXXXXXXX">
          </div>
          <div class="form-group">
            <label class="form-label">National ID Number</label>
            <input type="text" class="form-control" id="accNationalId" placeholder="National ID">
          </div>
        </div>

        <button type="button" class="btn-save" onclick="saveProfile()">Save Changes</button>
      </section>

      <section class="oryx-card">
        <h2 style="font-size: 18px; font-weight: 700; margin-bottom: 4px;">Disbursement Preferences</h2>
        <p style="font-size: 12.5px; color: var(--text-secondary); margin-bottom: 16px;">Primary payout route for approved loan disbursements.</p>
        
        <div class="form-group">
          <label class="form-label">M-Pesa Disbursal Mobile Number</label>
          <input type="text" class="form-control" id="accMpesa" placeholder="+2547XXXXXXXX">
        </div>
      </section>
    </div>

    <div>
      <div class="oryx-card">
        <h3 style="font-size: 16px; font-weight: 700; margin-bottom: 4px;">Account Security</h3>
        <p style="font-size: 12.5px; color: var(--text-secondary); margin-bottom: 14px;">Update your login password.</p>
        <div class="form-group">
          <label class="form-label">Current Password</label>
          <input type="password" class="form-control" placeholder="••••••••">
        </div>
        <div class="form-group">
          <label class="form-label">New Password</label>
          <input type="password" class="form-control" placeholder="Min. 6 characters">
        </div>
        <button style="width: 100%; padding: 10px; border-radius: 8px; background: var(--primary); color: #FFF; font-weight: 700; border: none; cursor: pointer;" onclick="alert('Password updated successfully!')">Update Password</button>
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

    function logoutBorrower() {
      localStorage.removeItem('oryx_auth_user');
      window.location.href = 'login.html';
    }

    document.addEventListener('DOMContentLoaded', () => {
      try {
        const user = JSON.parse(localStorage.getItem('oryx_auth_user'));
        if (user) {
          if (user.name) document.getElementById('accName').value = user.name;
          if (user.email) {
            document.getElementById('accEmail').value = user.email;
            document.getElementById('navUserPill').innerText = '👤 ' + (user.name || user.email.split('@')[0]);
          }
          if (user.phone) {
            document.getElementById('accPhone').value = user.phone;
            document.getElementById('accMpesa').value = user.phone;
          }
          if (user.nationalId) document.getElementById('accNationalId').value = user.nationalId;
        } else {
          window.location.href = 'login.html';
        }
      } catch(e) {}
    });

    function saveProfile() {
      try {
        const user = JSON.parse(localStorage.getItem('oryx_auth_user')) || {};
        user.name = document.getElementById('accName').value.trim();
        user.phone = document.getElementById('accPhone').value.trim();
        user.nationalId = document.getElementById('accNationalId').value.trim();
        localStorage.setItem('oryx_auth_user', JSON.stringify(user));
        if (user.email) {
          localStorage.setItem('oryx_borrower_' + user.email, JSON.stringify(user));
        }
        alert('Profile saved successfully!');
      } catch(e) {}
    }
  </script>
</body>
</html>
"""

    # 5. ADMIN DESK HTML (admin.html & desk.html) - Keep isolated
    # Read existing admin.html
    with open(f"{base_dir}/admin.html", "r") as f:
        admin_html = f.read()

    # Write all clean files
    with open(f"{base_dir}/login.html", "w") as f:
        f.write(login_html)
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

    print("Clean isolated borrower & auth system generated successfully!")

if __name__ == '__main__':
    generate_clean_isolated_system()

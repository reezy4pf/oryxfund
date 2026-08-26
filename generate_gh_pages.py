import os

def generate_gh_pages_html():
    html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Oryx Fund — Next-Gen Lending & Credit Management Platform</title>
  <meta name="description" content="Oryx Fund is an enterprise-grade digital credit and lending platform offering seamless instant loans, returning borrower express facilities, and institutional portfolio underwriting.">
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg viewBox='0 0 32 32' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Crect width='32' height='32' rx='8' fill='%231F3224'/%3E%3Cpath d='M7 23L14 9H18L25 23H20.5L18.8 19H13.2L11.5 23H7ZM14.3 16.5H17.7L16 12.5L14.3 16.5Z' fill='%2300D26A'/%3E%3C/svg%3E">
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800;1,9..40,400;1,9..40,600&family=IBM+Plex+Mono:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;0,800;1,600;1,700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <style>
    /* ==========================================================================
       1. CSS Custom Properties & Design Tokens (Light & Dark)
       ========================================================================== */
    :root {
      --bg-page: #EAE0D8;
      --bg-surface: #FFFFFF;
      --bg-surface-alt: #F6F1EC;
      --bg-surface-elevated: #FFFFFF;
      --border-color: #DCD2C7;
      --border-light: #E7DFD6;
      
      --text-primary: #1F3224;
      --text-secondary: #556B5D;
      --text-muted: #829488;
      
      --primary: #1F3224;
      --primary-hover: #2D4834;
      --accent-green: #059669;
      --accent-emerald: #00D26A;
      --accent-terracotta: #C1440E;
      --accent-amber: #D97706;
      
      --card-shadow: 0 4px 20px rgba(31, 50, 36, 0.06);
      --card-shadow-hover: 0 8px 30px rgba(31, 50, 36, 0.12);
      
      --font-body: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-heading: 'Playfair Display', Georgia, serif;
      --font-mono: 'IBM Plex Mono', monospace;
      --font-sans: 'Plus Jakarta Sans', sans-serif;
      
      --nav-height: 64px;
    }

    [data-theme="dark"], html.dark {
      --bg-page: #09090B;
      --bg-surface: #121215;
      --bg-surface-alt: #16221A;
      --bg-surface-elevated: #1C2B21;
      --border-color: #1F3325;
      --border-light: #18281D;
      
      --text-primary: #FAF8F5;
      --text-secondary: #9DB4A5;
      --text-muted: #667D6F;
      
      --primary: #00D26A;
      --primary-hover: #00FF80;
      --accent-green: #00D26A;
      --accent-emerald: #00D26A;
      --accent-terracotta: #E0561B;
      --accent-amber: #FBBF24;
      
      --card-shadow: 0 4px 24px rgba(0, 0, 0, 0.5);
      --card-shadow-hover: 0 8px 36px rgba(0, 210, 106, 0.12);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      transition: background-color 0.25s ease, border-color 0.25s ease, color 0.25s ease;
    }

    body {
      font-family: var(--font-body);
      background-color: var(--bg-page);
      color: var(--text-primary);
      min-height: 100vh;
      line-height: 1.5;
      overflow-x: hidden;
    }

    /* Noise overlay removed */

    /* ==========================================================================
       2. Top Interactive Demo Navbar & Switcher
       ========================================================================== */
    .oryx-top-nav {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(234, 224, 216, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-color);
      height: var(--nav-height);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 28px;
    }

    [data-theme="dark"] .oryx-top-nav {
      background: rgba(8, 13, 10, 0.85);
      border-bottom-color: var(--border-color);
    }

    .brand-cluster {
      display: flex;
      align-items: center;
      gap: 14px;
      text-decoration: none;
      color: var(--text-primary);
    }

    .brand-logo-img {
      height: 34px;
      width: auto;
      display: block;
    }

    .nav-tabs-cluster {
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(0, 0, 0, 0.05);
      padding: 4px;
      border-radius: 30px;
      border: 1px solid var(--border-color);
    }

    [data-theme="dark"] .nav-tabs-cluster {
      background: rgba(255, 255, 255, 0.05);
    }

    .nav-tab-btn {
      background: transparent;
      border: none;
      color: var(--text-secondary);
      font-family: var(--font-body);
      font-size: 13px;
      font-weight: 600;
      padding: 7px 16px;
      border-radius: 20px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      white-space: nowrap;
    }

    .nav-tab-btn:hover {
      color: var(--text-primary);
    }

    .nav-tab-btn.active {
      background: var(--bg-surface);
      color: var(--text-primary);
      box-shadow: 0 2px 8px rgba(0,0,0,0.08);
      font-weight: 700;
    }

    [data-theme="dark"] .nav-tab-btn.active {
      background: var(--accent-emerald);
      color: #000000;
      box-shadow: 0 2px 10px rgba(0, 210, 106, 0.3);
    }

    .top-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .theme-toggle-btn {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      color: var(--text-primary);
      width: 38px;
      height: 38px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 16px;
      box-shadow: var(--card-shadow);
      transition: transform 0.15s ease;
    }

    .theme-toggle-btn:hover {
      transform: scale(1.05);
    }

    .github-link-btn {
      background: var(--primary);
      color: #FFFFFF !important;
      border: none;
      padding: 8px 16px;
      border-radius: 20px;
      font-size: 13px;
      font-weight: 700;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: var(--card-shadow);
    }

    [data-theme="dark"] .github-link-btn {
      background: var(--accent-emerald);
      color: #000000 !important;
      box-shadow: 0 4px 15px rgba(0, 210, 106, 0.3);
    }

    /* ==========================================================================
       3. Main App Container
       ========================================================================== */
    .app-viewport {
      max-width: 1180px;
      margin: 32px auto 64px;
      padding: 0 24px;
    }

    .view-panel {
      display: none;
      animation: fadeIn 0.3s ease;
    }

    .view-panel.active-view {
      display: block;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }

    /* ==========================================================================
       4. Express Subsequent Loan Form Elements
       ========================================================================== */
    .express-hero-bar {
      background: linear-gradient(135deg, #1F3224 0%, #101B13 100%);
      color: #FAF8F5;
      padding: 28px 32px;
      border-radius: 20px;
      margin-bottom: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: var(--card-shadow);
      border: 1px solid rgba(255, 255, 255, 0.08);
      position: relative;
      overflow: hidden;
    }

    [data-theme="dark"] .express-hero-bar {
      background: linear-gradient(135deg, #121215 0%, #09090B 100%);
      border-color: var(--border-color);
    }

    .express-badge-chip {
      background: rgba(0, 210, 106, 0.15);
      border: 1px solid #00D26A;
      color: #00D26A;
      font-size: 11px;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: 12px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }

    .express-hero-title {
      font-family: var(--font-heading);
      font-size: 28px;
      font-weight: 700;
      letter-spacing: -0.5px;
    }

    .express-hero-desc {
      color: #9DB4A5;
      font-size: 14px;
      margin-top: 4px;
    }

    /* Verified Borrower Banner */
    .verified-kyc-banner {
      background: var(--bg-surface);
      border: 1.5px solid #00D26A;
      border-radius: 16px;
      padding: 20px 24px;
      margin-bottom: 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      box-shadow: var(--card-shadow);
    }

    .kyc-profile-item {
      display: flex;
      flex-direction: column;
    }

    .kyc-label {
      font-size: 11px;
      color: var(--text-muted);
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 0.5px;
    }

    .kyc-val {
      font-size: 14.5px;
      font-weight: 700;
      color: var(--text-primary);
      margin-top: 2px;
    }

    .kyc-status-pill {
      background: rgba(0, 210, 106, 0.12);
      color: var(--accent-green);
      font-size: 12px;
      font-weight: 800;
      padding: 6px 14px;
      border-radius: 20px;
      border: 1px solid rgba(0, 210, 106, 0.3);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    /* Step Progress Indicator */
    .stepper-nav {
      display: flex;
      gap: 12px;
      margin-bottom: 24px;
    }

    .step-item {
      flex: 1;
      background: var(--bg-surface);
      border: 1.5px solid var(--border-color);
      padding: 14px 18px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      gap: 12px;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .step-item.active {
      border-color: var(--accent-emerald);
      background: rgba(0, 210, 106, 0.04);
    }

    .step-number {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: var(--bg-surface-alt);
      border: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      font-weight: 800;
    }

    .step-item.active .step-number {
      background: var(--accent-emerald);
      color: #000;
      border-color: var(--accent-emerald);
    }

    .step-name {
      font-size: 13.5px;
      font-weight: 700;
      color: var(--text-primary);
    }

    /* Facility & Calculator Card */
    .oryx-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 18px;
      padding: 28px 32px;
      margin-bottom: 24px;
      box-shadow: var(--card-shadow);
    }

    .section-headline {
      font-size: 18px;
      font-weight: 700;
      color: var(--text-primary);
      margin-bottom: 6px;
    }

    .section-sub {
      font-size: 13.5px;
      color: var(--text-secondary);
      margin-bottom: 20px;
    }

    /* Product Cards */
    .product-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }

    .product-choice-card {
      border: 1.5px solid var(--border-color);
      border-radius: 14px;
      padding: 18px;
      cursor: pointer;
      background: var(--bg-surface);
      transition: all 0.2s ease;
      position: relative;
    }

    .product-choice-card:hover {
      border-color: var(--accent-emerald);
      transform: translateY(-2px);
    }

    .product-choice-card.selected {
      border-color: var(--accent-emerald);
      background: rgba(0, 210, 106, 0.05);
      box-shadow: 0 4px 16px rgba(0, 210, 106, 0.15);
    }

    .product-name {
      font-size: 15px;
      font-weight: 700;
      margin-bottom: 4px;
    }

    .product-meta {
      font-size: 12px;
      color: var(--text-secondary);
    }

    .rate-badge {
      position: absolute;
      top: 14px;
      right: 14px;
      font-size: 11px;
      font-weight: 800;
      background: rgba(0, 210, 106, 0.15);
      color: var(--accent-green);
      padding: 2px 8px;
      border-radius: 10px;
    }

    /* Interactive Loan Slider HUD */
    .calc-box {
      background: var(--bg-surface-alt);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 24px;
      margin-top: 20px;
    }

    .amount-display-wrap {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }

    .amount-big-val {
      font-family: var(--font-mono);
      font-size: 32px;
      font-weight: 700;
      color: var(--text-primary);
    }

    .amount-slider {
      width: 100%;
      height: 8px;
      border-radius: 4px;
      background: var(--border-color);
      outline: none;
      -webkit-appearance: none;
      cursor: pointer;
      margin-bottom: 14px;
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
      margin-bottom: 24px;
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
      transition: all 0.15s ease;
    }

    .pill-btn:hover, .pill-btn.active {
      border-color: var(--accent-emerald);
      color: var(--text-primary);
      background: rgba(0, 210, 106, 0.08);
    }

    /* Real-Time Live HUD */
    .metrics-live-hud {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 16px;
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 18px 20px;
    }

    .metric-hud-item {
      display: flex;
      flex-direction: column;
    }

    .hud-title {
      font-size: 11px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
    }

    .hud-number {
      font-family: var(--font-mono);
      font-size: 18px;
      font-weight: 700;
      color: var(--text-primary);
      margin-top: 4px;
    }

    .hud-number.highlight {
      color: var(--accent-emerald);
    }

    /* Buttons */
    .oryx-btn-primary {
      background: #1F3224 !important;
      color: #FFFFFF !important;
      font-family: var(--font-body);
      font-size: 14px;
      font-weight: 700;
      padding: 12px 24px;
      border-radius: 10px;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(31, 50, 36, 0.15);
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      text-decoration: none;
    }

    .oryx-btn-primary:hover {
      background: #2D4834 !important;
      transform: translateY(-2px);
    }

    .oryx-btn-express {
      background: linear-gradient(135deg, #00D26A 0%, #059669 100%) !important;
      color: #000000 !important;
      font-family: var(--font-body);
      font-size: 14px;
      font-weight: 800 !important;
      padding: 13px 26px;
      border-radius: 10px;
      border: none;
      cursor: pointer;
      box-shadow: 0 4px 15px rgba(0, 210, 106, 0.35) !important;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      text-decoration: none;
    }

    .oryx-btn-express:hover {
      background: linear-gradient(135deg, #00FF80 0%, #00D26A 100%) !important;
      color: #000000 !important;
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(0, 210, 106, 0.45) !important;
    }

    /* Fast-Track Subsequent Loan Portal Card */
    .oryx-subsequent-cta-card {
      background: linear-gradient(135deg, var(--bg-surface) 0%, rgba(0, 210, 106, 0.08) 100%);
      border: 1.5px solid #00D26A;
      border-radius: 16px;
      padding: 22px 28px;
      margin-bottom: 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
      box-shadow: var(--card-shadow);
    }

    .s-cta-badge {
      font-size: 11px;
      font-weight: 800;
      color: #059669;
      letter-spacing: 0.8px;
    }

    [data-theme="dark"] .s-cta-badge {
      color: #00D26A;
    }

    .s-cta-title {
      font-size: 20px;
      font-weight: 700;
      color: var(--text-primary);
      margin: 4px 0;
    }

    .s-cta-desc {
      font-size: 13.5px;
      color: var(--text-secondary);
      max-width: 580px;
    }

    /* Stats Grid */
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 16px;
      margin-bottom: 28px;
    }

    .kpi-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 14px;
      padding: 20px;
      box-shadow: var(--card-shadow);
    }

    .kpi-label {
      font-size: 12px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
    }

    .kpi-value {
      font-family: var(--font-mono);
      font-size: 24px;
      font-weight: 700;
      color: var(--text-primary);
      margin: 6px 0;
    }

    .kpi-sub {
      font-size: 12px;
      color: var(--accent-green);
      font-weight: 600;
    }

    /* Admin Desk Showcase Mock */
    .desk-wrapper {
      display: flex;
      border: 1px solid var(--border-color);
      border-radius: 18px;
      overflow: hidden;
      box-shadow: var(--card-shadow);
      background: var(--bg-surface);
    }

    .desk-sidebar {
      width: 240px;
      background: var(--bg-surface-alt);
      border-right: 1px solid var(--border-color);
      padding: 20px 14px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }

    .desk-brand-capsule {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 12px;
      border-radius: 10px;
      background: rgba(0, 0, 0, 0.04);
    }

    [data-theme="dark"] .desk-brand-capsule {
      background: rgba(255, 255, 255, 0.04);
    }

    .sidebar-section-title {
      font-size: 11px;
      font-weight: 800;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 0 10px;
      margin-bottom: 6px;
    }

    .sidebar-nav-item {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 12px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      color: var(--text-secondary);
      text-decoration: none;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .sidebar-nav-item:hover {
      color: var(--text-primary);
      background: rgba(0, 0, 0, 0.04);
    }

    .sidebar-nav-item.active {
      color: var(--text-primary);
      background: var(--bg-surface);
      font-weight: 700;
      border: 1px solid var(--border-color);
    }

    [data-theme="dark"] .sidebar-nav-item.active {
      background: var(--bg-surface-elevated);
      border-color: var(--accent-emerald);
      color: var(--accent-emerald);
    }

    .desk-content {
      flex: 1;
      padding: 24px 28px;
      background: var(--bg-page);
    }

    /* Modal / Success Screen */
    .success-modal-overlay {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.6);
      backdrop-filter: blur(8px);
      z-index: 2000;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .success-modal-card {
      background: var(--bg-surface);
      border: 1.5px solid #00D26A;
      border-radius: 20px;
      max-width: 520px;
      width: 100%;
      padding: 32px;
      text-align: center;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.35);
      animation: modalSlide 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    }

    @keyframes modalSlide {
      from { transform: scale(0.92); opacity: 0; }
      to { transform: scale(1); opacity: 1; }
    }

    /* Footer */
    .oryx-footer {
      border-top: 1px solid var(--border-color);
      padding: 32px 0;
      text-align: center;
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 64px;
    }

    /* Responsive */
    @media (max-width: 768px) {
      .oryx-top-nav {
        padding: 0 16px;
      }
      .nav-tabs-cluster {
        display: none;
      }
      .desk-wrapper {
        flex-direction: column;
      }
      .desk-sidebar {
        width: 100%;
      }
    }
  </style>
</head>
<body>
  

  <!-- Top Sticky Navigation -->
  <header class="oryx-top-nav">
    <a href="#" class="brand-cluster">
      <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="32" height="32" rx="8" fill="#1F3224"/>
        <path d="M7 23L14 9H18L25 23H20.5L18.8 19H13.2L11.5 23H7ZM14.3 16.5H17.7L16 12.5L14.3 16.5Z" fill="#00D26A"/>
      </svg>
      <div>
        <div style="font-family: var(--font-heading); font-weight: 800; font-size: 17px; line-height: 1;">Oryx Fund</div>
        <div style="font-size: 10px; font-weight: 700; color: var(--text-muted); letter-spacing: 0.8px;">CREDIT &amp; LENDING</div>
      </div>
    </a>

    <!-- Page Switcher Tabs -->
    <div class="nav-tabs-cluster">
      <button class="nav-tab-btn active" onclick="switchView('express')">⚡ Express Subsequent</button>
      <button class="nav-tab-btn" onclick="switchView('portal')">📊 My Loans</button>
      <button class="nav-tab-btn" onclick="switchView('account')">👤 My Account</button>
      <button class="nav-tab-btn" onclick="switchView('desk')">🛡️ Admin Desk</button>
    </div>

    <!-- Actions & Theme Toggle -->
    <div class="top-actions">
      <button class="theme-toggle-btn" id="themeToggle" onclick="toggleTheme()" title="Toggle Light / Dark Mode">☀️</button>
      <a href="https://github.com/reezy4pf/oryxfund" target="_blank" class="github-link-btn">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
        <span>GitHub Repo</span>
      </a>
    </div>
  </header>

  <!-- Main Viewport -->
  <main class="app-viewport">

    <!-- ====================================================================
         VIEW 1: Express Subsequent Loan Application
         ==================================================================== -->
    <div id="view-express" class="view-panel active-view">
      
      <!-- Express Header Capsule -->
      <div class="express-hero-bar">
        <div>
          <div class="express-badge-chip">⚡ FAST-TRACK RETURNING BORROWER</div>
          <h1 class="express-hero-title">Subsequent Facility Application</h1>
          <p class="express-hero-desc">Your profile and KYC are verified. Choose your terms for priority underwriting.</p>
        </div>
        <div style="text-align: right; display: flex; flex-direction: column; align-items: flex-end;">
          <span style="font-size: 11px; color: #9DB4A5; font-weight: 700; text-transform: uppercase;">Average Approval</span>
          <span style="font-family: var(--font-mono); font-size: 22px; font-weight: 700; color: #00D26A;">15 Minutes</span>
        </div>
      </div>

      <!-- Verified KYC Banner -->
      <div class="verified-kyc-banner">
        <div class="kyc-profile-item">
          <span class="kyc-label">Borrower</span>
          <span class="kyc-val">Trooper Mwangi</span>
        </div>
        <div class="kyc-profile-item">
          <span class="kyc-label">National ID</span>
          <span class="kyc-val" style="font-family: var(--font-mono);">31****89</span>
        </div>
        <div class="kyc-profile-item">
          <span class="kyc-label">Disbursal Destination</span>
          <span class="kyc-val">M-Pesa (+254***678)</span>
        </div>
        <div class="kyc-status-pill">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>
          <span>Verified KYC on File</span>
        </div>
      </div>

      <!-- Stepper Indicator -->
      <div class="stepper-nav">
        <div class="step-item active" id="stepIndicator1" onclick="goToStep(1)">
          <div class="step-number">1</div>
          <div class="step-name">Facility Specs &amp; Calculator</div>
        </div>
        <div class="step-item" id="stepIndicator2" onclick="goToStep(2)">
          <div class="step-number">2</div>
          <div class="step-name">Quick Financial Check &amp; Confirmation</div>
        </div>
      </div>

      <!-- Step 1 Form -->
      <div id="step1Content" class="oryx-card">
        <h2 class="section-headline">1. Select Loan Product</h2>
        <p class="section-sub">Choose a customized lending structure tailored for your working capital needs.</p>

        <div class="product-grid">
          <div class="product-choice-card selected" onclick="selectProduct(this, 'Working Capital', 0.14, 3, 12)">
            <span class="rate-badge">14.0% p.a.</span>
            <div class="product-name">Working Capital Advance</div>
            <div class="product-meta">Tenure: 3 - 12 Months • Monthly Amortization</div>
          </div>
          <div class="product-choice-card" onclick="selectProduct(this, 'Asset Financing', 0.125, 6, 36)">
            <span class="rate-badge">12.5% p.a.</span>
            <div class="product-name">Asset &amp; Equipment Finance</div>
            <div class="product-meta">Tenure: 6 - 36 Months • Secured Asset</div>
          </div>
          <div class="product-choice-card" onclick="selectProduct(this, 'Business Growth', 0.11, 12, 60)">
            <span class="rate-badge">11.0% p.a.</span>
            <div class="product-name">Business Growth Facility</div>
            <div class="product-meta">Tenure: 12 - 60 Months • Term Facility</div>
          </div>
        </div>

        <!-- Interactive Slider Box -->
        <div class="calc-box">
          <div class="amount-display-wrap">
            <span style="font-size: 13px; font-weight: 700; color: var(--text-muted); text-transform: uppercase;">Requested Facility Amount</span>
            <span id="loanAmountText" class="amount-big-val">KES 250,000</span>
          </div>

          <input type="range" id="loanSlider" class="amount-slider" min="10000" max="2000000" step="10000" value="250000" oninput="updateCalculator(this.value)">

          <div class="preset-pills">
            <button class="pill-btn" onclick="setPreset(50000)">KES 50K</button>
            <button class="pill-btn" onclick="setPreset(100000)">KES 100K</button>
            <button class="pill-btn active" onclick="setPreset(250000)">KES 250K</button>
            <button class="pill-btn" onclick="setPreset(500000)">KES 500K</button>
            <button class="pill-btn" onclick="setPreset(1000000)">KES 1.0M</button>
          </div>

          <!-- Live Metrics HUD -->
          <div class="metrics-live-hud">
            <div class="metric-hud-item">
              <span class="hud-title">Principal Facility</span>
              <span id="hudPrincipal" class="hud-number">KES 250,000</span>
            </div>
            <div class="metric-hud-item">
              <span class="hud-title">Est. Total Interest</span>
              <span id="hudInterest" class="hud-number">KES 17,500</span>
            </div>
            <div class="metric-hud-item">
              <span class="hud-title">Monthly Installment</span>
              <span id="hudMonthly" class="hud-number highlight">KES 44,583 / mo</span>
            </div>
            <div class="metric-hud-item">
              <span class="hud-title">Total Repayment</span>
              <span id="hudTotal" class="hud-number">KES 267,500</span>
            </div>
          </div>
        </div>

        <div style="margin-top: 28px; display: flex; justify-content: flex-end;">
          <button class="oryx-btn-express" onclick="goToStep(2)">
            <span>Proceed to Confirmation ➔</span>
          </button>
        </div>
      </div>

      <!-- Step 2 Form -->
      <div id="step2Content" class="oryx-card" style="display: none;">
        <h2 class="section-headline">2. Fast-Track Verification &amp; Submit</h2>
        <p class="section-sub">Confirm your profile details to release funds directly to your verified payout route.</p>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 24px;">
          <div style="background: var(--bg-surface-alt); border: 1.5px solid var(--border-color); border-radius: 12px; padding: 18px;">
            <div style="font-weight: 700; font-size: 14px; margin-bottom: 4px;">Verified Income Source</div>
            <div style="font-size: 12.5px; color: var(--text-secondary);">Using verified historical financial statements on record.</div>
          </div>
          <div style="background: var(--bg-surface-alt); border: 1.5px solid var(--border-color); border-radius: 12px; padding: 18px;">
            <div style="font-weight: 700; font-size: 14px; margin-bottom: 4px;">Guarantor on File</div>
            <div style="font-size: 12.5px; color: var(--text-secondary);">Primary Guarantor: <strong>Jane Doe (+254***912)</strong></div>
          </div>
        </div>

        <div style="background: rgba(0, 210, 106, 0.08); border: 1.5px dashed var(--accent-emerald); border-radius: 12px; padding: 16px; margin-bottom: 24px; display: flex; align-items: center; gap: 12px;">
          <span style="font-size: 24px;">⚡</span>
          <div style="font-size: 13.5px; color: var(--text-primary);">
            <strong>Priority Underwriting SLA:</strong> Because your previous loan <code>ACC-LOAP-2026-00018</code> was completed in good standing, this facility is routed to the express instant-approval channel.
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center;">
          <button class="oryx-btn-primary" onclick="goToStep(1)" style="background: var(--bg-surface-alt) !important; color: var(--text-primary) !important; border: 1px solid var(--border-color) !important;">
            <span>← Back to Facility Specs</span>
          </button>
          <button class="oryx-btn-express" onclick="submitExpressApplication()">
            <span>⚡ Submit Subsequent Loan Application</span>
          </button>
        </div>
      </div>

    </div>

    <!-- ====================================================================
         VIEW 2: Borrower Portal (My Loans)
         ==================================================================== -->
    <div id="view-portal" class="view-panel">
      
      <!-- Express CTA Banner -->
      <div class="oryx-subsequent-cta-card">
        <div>
          <div class="s-cta-badge">⚡ ELIGIBLE FOR EXPRESS FINANCING</div>
          <h3 class="s-cta-title">Need a Subsequent Loan?</h3>
          <p class="s-cta-desc">Because your identity &amp; KYC are already verified, returning borrowers bypass standard documentation with priority same-day underwriting.</p>
        </div>
        <button class="oryx-btn-express" onclick="switchView('express')">
          <span>⚡ Apply in 60 Seconds ➔</span>
        </button>
      </div>

      <!-- KPI Summary -->
      <div class="kpi-grid">
        <div class="kpi-card">
          <div class="kpi-label">Active Facilities</div>
          <div class="kpi-value">1 Facility</div>
          <div class="kpi-sub">Working Capital • Active</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-label">Outstanding Balance</div>
          <div class="kpi-value">KES 88,400</div>
          <div class="kpi-sub">Current on schedule</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-label">Next Payment Due</div>
          <div class="kpi-value">KES 22,100</div>
          <div class="kpi-sub" style="color: var(--accent-amber);">Due in 8 Days (04-Sep)</div>
        </div>
        <div class="kpi-card">
          <div class="kpi-label">Borrower Standing</div>
          <div class="kpi-value" style="color: var(--accent-emerald);">Grade A+</div>
          <div class="kpi-sub">Express-eligible borrower</div>
        </div>
      </div>

      <!-- Facility Details Card -->
      <div class="oryx-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px;">
          <div>
            <h2 class="section-headline">Active Loan: ACC-LOAN-2026-00012</h2>
            <div style="font-size: 13px; color: var(--text-secondary);">Disbursed on 15-Jun-2026 • 6 Months Tenure</div>
          </div>
          <span style="background: rgba(0, 210, 106, 0.15); color: var(--accent-green); font-size: 12px; font-weight: 800; padding: 4px 12px; border-radius: 20px;">IN REPAYMENT</span>
        </div>

        <div style="height: 10px; background: var(--bg-surface-alt); border-radius: 5px; overflow: hidden; margin-bottom: 14px;">
          <div style="width: 65%; height: 100%; background: var(--accent-emerald);"></div>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 12.5px; color: var(--text-secondary);">
          <span>Repaid: KES 161,600 (65%)</span>
          <span>Remaining: KES 88,400 (35%)</span>
        </div>
      </div>

    </div>

    <!-- ====================================================================
         VIEW 3: Borrower Profile (My Account)
         ==================================================================== -->
    <div id="view-account" class="view-panel">
      <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 24px;">
        
        <div class="oryx-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <h2 class="section-headline">Personal &amp; KYC Profile</h2>
            <span class="kyc-status-pill">✓ Verified Borrower</span>
          </div>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px;">
            <div>
              <label style="font-size: 12px; font-weight: 700; color: var(--text-muted);">Legal Full Name</label>
              <input type="text" value="Trooper Mwangi" readonly style="width: 100%; padding: 10px; border-radius: 8px; border: 1px solid var(--border-color); background: var(--bg-surface-alt); color: var(--text-primary); margin-top: 4px; font-weight: 600;">
            </div>
            <div>
              <label style="font-size: 12px; font-weight: 700; color: var(--text-muted);">National ID Number</label>
              <input type="text" value="31456789" readonly style="width: 100%; padding: 10px; border-radius: 8px; border: 1px solid var(--border-color); background: var(--bg-surface-alt); color: var(--text-primary); margin-top: 4px; font-weight: 600;">
            </div>
          </div>

          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
            <div>
              <label style="font-size: 12px; font-weight: 700; color: var(--text-muted);">KRA PIN</label>
              <input type="text" value="A012345678Z" readonly style="width: 100%; padding: 10px; border-radius: 8px; border: 1px solid var(--border-color); background: var(--bg-surface-alt); color: var(--text-primary); margin-top: 4px; font-weight: 600;">
            </div>
            <div>
              <label style="font-size: 12px; font-weight: 700; color: var(--text-muted);">County / Region</label>
              <input type="text" value="Nairobi, Kenya" readonly style="width: 100%; padding: 10px; border-radius: 8px; border: 1px solid var(--border-color); background: var(--bg-surface-alt); color: var(--text-primary); margin-top: 4px; font-weight: 600;">
            </div>
          </div>
        </div>

        <!-- Express Facility Card in My Account -->
        <div class="oryx-card" style="border: 1.5px solid var(--accent-emerald); background: linear-gradient(145deg, rgba(0, 210, 106, 0.08) 0%, transparent 100%);">
          <span style="font-size: 10px; font-weight: 800; color: var(--accent-emerald); letter-spacing: 0.8px;">⚡ EXPRESS REPEAT FACILITY</span>
          <h3 style="font-size: 17px; font-weight: 700; margin: 6px 0;">Fast-Track Subsequent Loan</h3>
          <p style="font-size: 12.5px; color: var(--text-secondary); margin-bottom: 16px;">Apply for a new advance using your existing verified profile.</p>
          <button class="oryx-btn-express" onclick="switchView('express')" style="width: 100%;">
            ⚡ Apply in 60 Seconds ➔
          </button>
        </div>

      </div>
    </div>

    <!-- ====================================================================
         VIEW 4: Admin Desk Showcase
         ==================================================================== -->
    <div id="view-desk" class="view-panel">
      <div class="desk-wrapper">
        
        <!-- Sidebar with Dashboard #1 and Quick Links at Bottom -->
        <aside class="desk-sidebar">
          <div class="desk-brand-capsule">
            <svg width="22" height="22" viewBox="0 0 32 32" fill="none"><rect width="32" height="32" rx="6" fill="#1F3224"/><path d="M7 23L14 9H18L25 23H20.5L18.8 19H13.2L11.5 23H7Z" fill="#00D26A"/></svg>
            <div>
              <div style="font-weight: 700; font-size: 13px;">Oryx Fund</div>
              <div style="font-size: 9px; color: var(--text-muted);">Lending Platform</div>
            </div>
          </div>

          <div style="display: flex; flex-direction: column; gap: 4px;">
            <div class="sidebar-nav-item active">📊 Dashboard</div>
          </div>

          <div>
            <div class="sidebar-section-title">Users &amp; Access</div>
            <div style="display: flex; flex-direction: column; gap: 2px;">
              <div class="sidebar-nav-item">👥 Users</div>
              <div class="sidebar-nav-item">🔑 Role Permissions</div>
              <div class="sidebar-nav-item">🛡️ User Permissions</div>
            </div>
          </div>

          <div>
            <div class="sidebar-section-title">System &amp; Tools</div>
            <div style="display: flex; flex-direction: column; gap: 2px;">
              <div class="sidebar-nav-item">📁 File Manager</div>
              <div class="sidebar-nav-item">📄 Page Builder</div>
              <div class="sidebar-nav-item">💬 SMS Log</div>
            </div>
          </div>

          <div>
            <div class="sidebar-section-title">Reports</div>
            <div style="display: flex; flex-direction: column; gap: 2px;">
              <div class="sidebar-nav-item">📈 Portfolio Analytics</div>
              <div class="sidebar-nav-item">📑 Document Reports</div>
            </div>
          </div>

          <div style="margin-top: auto;">
            <div class="sidebar-section-title">Navigation</div>
            <div class="sidebar-nav-item" style="border: 1px dashed var(--border-color);">🔗 Quick Links</div>
          </div>
        </aside>

        <!-- Desk Content Area -->
        <div class="desk-content">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
            <div>
              <h2 style="font-family: var(--font-heading); font-size: 22px; font-weight: 700;">Institutional Loan Dashboard</h2>
              <p style="font-size: 12.5px; color: var(--text-secondary);">Real-time underwriting queue and portfolio exposure metrics</p>
            </div>
            <span style="background: rgba(0, 210, 106, 0.12); color: var(--accent-green); font-size: 12px; font-weight: 800; padding: 5px 12px; border-radius: 20px;">● System Online</span>
          </div>

          <div class="kpi-grid" style="grid-template-columns: repeat(3, 1fr); margin-bottom: 20px;">
            <div class="kpi-card">
              <div class="kpi-label">Active Portfolio</div>
              <div class="kpi-value">KES 142.5M</div>
              <div class="kpi-sub">+12.4% MoM Growth</div>
            </div>
            <div class="kpi-card">
              <div class="kpi-label">Subsequent Repeat Loans</div>
              <div class="kpi-value" style="color: var(--accent-emerald);">68.2%</div>
              <div class="kpi-sub">Priority Fast-Track Queue</div>
            </div>
            <div class="kpi-card">
              <div class="kpi-label">PAR &gt; 30 Days</div>
              <div class="kpi-value" style="color: var(--accent-green);">1.8%</div>
              <div class="kpi-sub">Institutional Grade</div>
            </div>
          </div>

          <div class="oryx-card" style="margin-bottom: 0;">
            <h3 style="font-size: 15px; font-weight: 700; margin-bottom: 12px;">Recent Loan Applications Queue</h3>
            <table style="width: 100%; font-size: 13px; border-collapse: collapse;">
              <thead>
                <tr style="border-bottom: 1px solid var(--border-color); color: var(--text-muted); text-align: left;">
                  <th style="padding: 8px;">Application ID</th>
                  <th style="padding: 8px;">Applicant</th>
                  <th style="padding: 8px;">Facility Type</th>
                  <th style="padding: 8px;">Amount</th>
                  <th style="padding: 8px;">Flow Type</th>
                  <th style="padding: 8px;">Status</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom: 1px solid var(--border-light);">
                  <td style="padding: 10px 8px; font-family: var(--font-mono); font-weight: 700;">ACC-LOAP-2026-00042</td>
                  <td style="padding: 10px 8px;">Trooper Mwangi</td>
                  <td style="padding: 10px 8px;">Working Capital</td>
                  <td style="padding: 10px 8px; font-weight: 700;">KES 250,000</td>
                  <td style="padding: 10px 8px;"><span style="color: var(--accent-emerald); font-weight: 800;">⚡ Subsequent</span></td>
                  <td style="padding: 10px 8px;"><span style="background: rgba(0,210,106,0.15); color: var(--accent-green); font-size: 11px; font-weight: 800; padding: 2px 8px; border-radius: 10px;">Sanctioned</span></td>
                </tr>
                <tr>
                  <td style="padding: 10px 8px; font-family: var(--font-mono); font-weight: 700;">ACC-LOAP-2026-00041</td>
                  <td style="padding: 10px 8px;">Amani Ventures Ltd</td>
                  <td style="padding: 10px 8px;">Asset Finance</td>
                  <td style="padding: 10px 8px; font-weight: 700;">KES 1,200,000</td>
                  <td style="padding: 10px 8px;"><span style="color: var(--text-muted);">Standard</span></td>
                  <td style="padding: 10px 8px;"><span style="background: rgba(217,119,6,0.15); color: var(--accent-amber); font-size: 11px; font-weight: 800; padding: 2px 8px; border-radius: 10px;">Appraising</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

      </div>
    </div>

  </main>

  <!-- Submission Success Modal -->
  <div id="successModal" class="success-modal-overlay">
    <div class="success-modal-card">
      <div style="font-size: 48px; margin-bottom: 12px;">⚡</div>
      <span class="express-badge-chip">PRIORITY DISBURSAL QUEUE</span>
      <h2 style="font-family: var(--font-heading); font-size: 26px; font-weight: 700; margin: 8px 0;">Subsequent Loan Submitted!</h2>
      <p style="font-size: 14px; color: var(--text-secondary); margin-bottom: 20px;">
        Application <strong id="modalAppId" style="font-family: var(--font-mono); color: var(--text-primary);">ACC-LOAP-2026-00042</strong> has been logged. Because your KYC is verified, disbursal to M-Pesa is processed within 15 minutes.
      </p>
      <div style="background: var(--bg-surface-alt); border-radius: 12px; padding: 14px; margin-bottom: 24px; font-size: 13px;">
        <strong>Disbursal Amount:</strong> <span id="modalAmount" style="font-family: var(--font-mono); font-weight: 700; color: var(--accent-emerald);">KES 250,000</span>
      </div>
      <button class="oryx-btn-express" style="width: 100%;" onclick="closeSuccessModal()">
        <span>Return to My Portal</span>
      </button>
    </div>
  </div>

  <!-- Footer -->
  <footer class="oryx-footer">
    <div style="max-width: 1180px; margin: 0 auto; padding: 0 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
      <div>© 2026 Oryx Fund. All Rights Reserved. Custom Frappe Lending Engine.</div>
      <div style="font-family: var(--font-mono); font-size: 11px;">Obsidian &amp; Nairobi Craft Design System</div>
    </div>
  </footer>

  <!-- Scripts -->
  <script>
    let currentAmount = 250000;
    let currentRate = 0.14;
    let currentTenureMonths = 6;

    function toggleTheme() {
      const html = document.documentElement;
      const currentTheme = html.getAttribute('data-theme') || 'light';
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';
      html.setAttribute('data-theme', newTheme);
      document.getElementById('themeToggle').innerText = newTheme === 'dark' ? '🌙' : '☀️';
    }

    function switchView(viewId) {
      document.querySelectorAll('.view-panel').forEach(el => el.classList.remove('active-view'));
      document.querySelectorAll('.nav-tab-btn').forEach(el => el.classList.remove('active'));
      
      const targetView = document.getElementById('view-' + viewId);
      if (targetView) targetView.classList.add('active-view');
      
      const buttons = document.querySelectorAll('.nav-tab-btn');
      if (viewId === 'express') buttons[0].classList.add('active');
      if (viewId === 'portal') buttons[1].classList.add('active');
      if (viewId === 'account') buttons[2].classList.add('active');
      if (viewId === 'desk') buttons[3].classList.add('active');

      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function goToStep(stepNumber) {
      if (stepNumber === 1) {
        document.getElementById('step1Content').style.display = 'block';
        document.getElementById('step2Content').style.display = 'none';
        document.getElementById('stepIndicator1').classList.add('active');
        document.getElementById('stepIndicator2').classList.remove('active');
      } else {
        document.getElementById('step1Content').style.display = 'none';
        document.getElementById('step2Content').style.display = 'block';
        document.getElementById('stepIndicator1').classList.remove('active');
        document.getElementById('stepIndicator2').classList.add('active');
      }
    }

    function selectProduct(element, name, rate, minTenure, maxTenure) {
      document.querySelectorAll('.product-choice-card').forEach(c => c.classList.remove('selected'));
      element.classList.add('selected');
      currentRate = rate;
      currentTenureMonths = Math.round((minTenure + maxTenure) / 2);
      updateCalculator(currentAmount);
    }

    function setPreset(amount) {
      document.getElementById('loanSlider').value = amount;
      document.querySelectorAll('.pill-btn').forEach(btn => {
        btn.classList.toggle('active', btn.innerText.includes((amount/1000) + 'K') || (amount >= 1000000 && btn.innerText.includes('1.0M')));
      });
      updateCalculator(amount);
    }

    function updateCalculator(val) {
      currentAmount = parseInt(val, 10);
      document.getElementById('loanAmountText').innerText = 'KES ' + currentAmount.toLocaleString('en-US');
      
      const interest = Math.round(currentAmount * currentRate * (currentTenureMonths / 12));
      const total = currentAmount + interest;
      const monthly = Math.round(total / currentTenureMonths);
      
      document.getElementById('hudPrincipal').innerText = 'KES ' + currentAmount.toLocaleString('en-US');
      document.getElementById('hudInterest').innerText = 'KES ' + interest.toLocaleString('en-US');
      document.getElementById('hudMonthly').innerText = 'KES ' + monthly.toLocaleString('en-US') + ' / mo';
      document.getElementById('hudTotal').innerText = 'KES ' + total.toLocaleString('en-US');
    }

    function submitExpressApplication() {
      const modal = document.getElementById('successModal');
      document.getElementById('modalAmount').innerText = 'KES ' + currentAmount.toLocaleString('en-US');
      modal.style.display = 'flex';
    }

    function closeSuccessModal() {
      document.getElementById('successModal').style.display = 'none';
      switchView('portal');
    }
  </script>
</body>
</html>
"""
    return html

if __name__ == '__main__':
    with open('/home/reezy/.gemini/antigravity-ide/scratch/oryx_fund/index.html', 'w') as f:
        f.write(generate_gh_pages_html())
    print("GitHub Pages index.html generated successfully!")

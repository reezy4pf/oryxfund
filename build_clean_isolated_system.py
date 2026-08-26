import os
import json

base_dir = "/home/reezy/.gemini/antigravity-ide/scratch/oryx_fund"

def generate_all():
    # 1. Shared CSS Styles
    css_content = """/* ==========================================================================
   ORYX FUND OFFICIAL LENDING SYSTEM CORE STYLES (MATCHING LOCALHOST 1:1)
   ========================================================================== */
:root, [data-theme="light"], [data-theme-mode="light"] {
  --bg-body: #EAE0D8;
  --bg-card: #FFFFFF;
  --bg-surface: #F5EFEA;
  --text-color: #121A14;
  --text-muted: #556B5D;
  --border-color: #D8CCC1;
  --border-light: #ECE5DC;
  --primary-color: #1F3224;
  --primary-hover: #16251A;
  --accent-green: #059669;
  --accent-emerald: #00D26A;
  --accent-gold: #C1440E;
  --hero-bg: #1F3224;
  --hero-text: #FAF8F5;
  --card-shadow: 0 4px 20px rgba(31, 50, 36, 0.06);
  --font-body: -apple-system, BlinkMacSystemFont, "DM Sans", "Segoe UI", Roboto, sans-serif;
  --font-mono: 'IBM Plex Mono', SFMono-Regular, Menlo, Monaco, Consolas, monospace;
}

[data-theme="dark"], html.dark, body.dark, [data-theme-mode="dark"] {
  --bg-body: #080D0A;
  --bg-card: #101712;
  --bg-surface: #141F17;
  --text-color: #F3F4F6;
  --text-muted: #9CA3AF;
  --border-color: #1E2D22;
  --border-light: #18241B;
  --primary-color: #00D26A;
  --primary-hover: #00B85C;
  --accent-green: #00D26A;
  --accent-emerald: #00D26A;
  --accent-gold: #F59E0B;
  --hero-bg: linear-gradient(145deg, #132218, #0E1812);
  --hero-text: #FAF8F5;
  --card-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  transition: background-color 0.15s ease, border-color 0.15s ease, color 0.15s ease;
}

body {
  background-color: var(--bg-body) !important;
  color: var(--text-color) !important;
  font-family: var(--font-body) !important;
  min-height: 100vh;
  line-height: 1.5;
}

/* FULL-WIDTH STICKY NAVBAR */
.oryx-navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(234, 224, 216, 0.94);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-color);
  padding: 10px 24px;
  width: 100%;
  box-sizing: border-box;
}

[data-theme="dark"] .oryx-navbar,
html.dark .oryx-navbar {
  background: rgba(10, 10, 10, 0.94);
  border-bottom-color: #1A221C;
}

.oryx-nav-inner {
  max-width: 1080px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
}

.oryx-brand {
  display: flex;
  align-items: center;
  text-decoration: none;
}

.oryx-logo-img {
  height: 38px;
  width: auto;
  max-width: 150px;
  object-fit: contain;
  display: block;
}

.oryx-logo-light { display: block !important; }
.oryx-logo-dark { display: none !important; }

[data-theme="dark"] .oryx-logo-light,
html.dark .oryx-logo-light {
  display: none !important;
}

[data-theme="dark"] .oryx-logo-dark,
html.dark .oryx-logo-dark {
  display: block !important;
}

/* CAPSULE NAV SYSTEM */
.oryx-nav-desktop-capsules {
  display: flex;
  align-items: center;
  gap: 10px;
}

.oryx-capsules-nav {
  display: flex;
  align-items: center;
  gap: 4px;
  background: rgba(31, 50, 36, 0.04);
  padding: 4px;
  border-radius: 9999px;
  border: 1px solid var(--border-color);
}

[data-theme="dark"] .oryx-capsules-nav,
html.dark .oryx-capsules-nav {
  background: #111412;
  border-color: #1C261F;
}

.oryx-capsule-tab {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 6px 16px;
  border-radius: 9999px;
  font-size: 13px;
  font-weight: 500;
  color: var(--text-color);
  text-decoration: none;
  transition: all 0.15s ease;
  white-space: nowrap;
}

[data-theme="dark"] .oryx-capsule-tab,
html.dark .oryx-capsule-tab {
  color: #FAF8F5;
}

.oryx-capsule-tab:hover:not(.active) {
  background: rgba(31, 50, 36, 0.06);
}

[data-theme="dark"] .oryx-capsule-tab:hover:not(.active),
html.dark .oryx-capsule-tab:hover:not(.active) {
  background: rgba(255, 255, 255, 0.06);
}

.oryx-capsule-tab.active {
  background: #1F3224 !important;
  color: #FFFFFF !important;
  font-weight: 700;
  box-shadow: 0 2px 8px rgba(31, 50, 36, 0.2);
}

[data-theme="dark"] .oryx-capsule-tab.active,
html.dark .oryx-capsule-tab.active {
  background: #00D26A !important;
  color: #000000 !important;
  box-shadow: 0 2px 10px rgba(0, 210, 106, 0.35);
}

.oryx-theme-toggle-btn {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: transparent;
  border: 1px solid var(--border-color);
  color: var(--text-color);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.15s ease;
}

[data-theme="dark"] .oryx-theme-toggle-btn,
html.dark .oryx-theme-toggle-btn {
  border-color: #1C261F;
  color: #FAF8F5;
}

.oryx-theme-toggle-btn:hover {
  border-color: #1F3224;
  transform: translateY(-1px);
}

[data-theme="dark"] .oryx-theme-toggle-btn:hover,
html.dark .oryx-theme-toggle-btn:hover {
  border-color: #00D26A;
}

.sun-icon { display: none; }
.moon-icon { display: block; }

[data-theme="dark"] .sun-icon,
html.dark .sun-icon { display: block; }

[data-theme="dark"] .moon-icon,
html.dark .moon-icon { display: none; }

/* MOBILE NAVIGATION */
.oryx-nav-mobile-right { display: none; }
.oryx-mobile-capsules-bar { display: none; }

@media (max-width: 768px) {
  .oryx-nav-desktop-capsules { display: none !important; }
  .oryx-nav-mobile-right {
    display: flex !important;
    align-items: center;
    gap: 8px;
  }
  .oryx-mobile-capsules-bar {
    display: block !important;
    padding-top: 6px;
    margin-top: 6px;
    border-top: 1px solid var(--border-color);
  }
  .oryx-mobile-capsules-track {
    display: flex;
    align-items: center;
    gap: 6px;
    overflow-x: auto;
    padding-bottom: 4px;
  }
  .oryx-mobile-capsules-track .oryx-capsule-tab {
    padding: 5px 12px;
    font-size: 12px;
    border: 1px solid var(--border-color);
    background: var(--bg-card);
  }
}

/* MAIN CONTAINER */
.oryx-portal-wrapper {
  max-width: 1080px;
  margin: 24px auto 80px;
  padding: 0 16px;
  box-sizing: border-box;
}

/* HERO CARD (EXACT LOCALHOST) */
.oryx-hero-card {
  background: var(--hero-bg);
  color: #FFFFFF;
  border-radius: 16px;
  padding: 24px 28px;
  margin-bottom: 24px;
  box-shadow: 0 8px 24px rgba(31, 50, 36, 0.12);
  position: relative;
}

[data-theme="dark"] .oryx-hero-card {
  border: 1px solid #1D2E22;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
}

.hero-top-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}

.oryx-badge {
  display: inline-block;
  background: rgba(255, 255, 255, 0.12);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #FAF8F5;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  padding: 4px 10px;
  border-radius: 20px;
  text-transform: uppercase;
}

.user-greeting {
  font-size: 12.5px;
  color: #D6DFD8;
  font-weight: 500;
}

.hero-main-row {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 20px;
}

.oryx-title {
  font-size: 24px;
  font-weight: 700;
  margin: 0 0 6px 0;
  color: #FAF8F5;
  letter-spacing: -0.01em;
}

.oryx-subtitle {
  font-size: 13.5px;
  color: #D6DFD8;
  margin: 0;
  max-width: 620px;
  line-height: 1.45;
}

.oryx-hero-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #FFFFFF !important;
  color: #1F3224 !important;
  font-size: 13.5px;
  font-weight: 700;
  padding: 10px 18px;
  border-radius: 8px;
  text-decoration: none;
  white-space: nowrap;
  transition: all 0.15s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.oryx-hero-btn:hover {
  background: #FAF8F5 !important;
  transform: translateY(-1px);
}

[data-theme="dark"] .oryx-hero-btn {
  background: #FAF8F5 !important;
  color: #0A0A0A !important;
}

/* 4-STEP WIZARD STEPPERS */
.oryx-steps-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid rgba(255, 255, 255, 0.15);
}

.oryx-step {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  opacity: 0.55;
  transition: all 0.2s ease;
}

.oryx-step.active {
  opacity: 1;
  font-weight: 700;
}

.oryx-step.completed {
  opacity: 0.95;
}

.step-num {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.15);
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11.5px;
  font-weight: 700;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.oryx-step.active .step-num {
  background: #FFFFFF;
  color: #1F3224;
  border-color: #FFFFFF;
}

[data-theme="dark"] .oryx-step.active .step-num {
  background: #00D26A;
  color: #000000;
  border-color: #00D26A;
}

.oryx-step.completed .step-num {
  background: rgba(0, 210, 106, 0.3);
  color: #00D26A;
  border-color: #00D26A;
}

.step-label {
  font-size: 12.5px;
  color: #FAF8F5;
}

.step-divider {
  flex: 1;
  height: 1px;
  background: rgba(255, 255, 255, 0.2);
  margin: 0 12px;
}

.step-divider.completed {
  background: #00D26A;
}

/* STATS KPI GRID */
.oryx-stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-bottom: 24px;
}

.oryx-stat-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 14px;
  padding: 18px 20px;
  display: flex;
  align-items: center;
  gap: 16px;
  box-shadow: var(--card-shadow);
}

.stat-icon-wrap {
  width: 44px;
  height: 44px;
  border-radius: 10px;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--primary-color);
  flex-shrink: 0;
}

[data-theme="dark"] .stat-icon-wrap {
  color: #00D26A;
}

.stat-icon-wrap.highlight {
  color: #D97706;
}

.stat-content {
  display: flex;
  flex-direction: column;
}

.stat-label {
  font-size: 11px;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-family: var(--font-mono);
  margin-bottom: 4px;
}

.stat-val {
  font-size: 18px;
  font-weight: 700;
  color: var(--text-color);
  font-family: var(--font-mono);
}

/* PORTAL CARDS & FORMS */
.oryx-portal-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 26px 28px;
  margin-bottom: 24px;
  box-shadow: var(--card-shadow);
}

.card-section-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  padding-bottom: 14px;
  border-bottom: 1px solid var(--border-light);
}

.section-title {
  font-size: 18px;
  font-weight: 700;
  color: var(--text-color);
  margin: 0 0 4px 0;
}

.section-desc {
  font-size: 13px;
  color: var(--text-muted);
  margin: 0;
}

/* EMPTY STATES */
.oryx-empty-state {
  padding: 40px 20px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.empty-icon-wrap {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
  margin-bottom: 16px;
}

.empty-title {
  font-size: 16px;
  font-weight: 700;
  color: var(--text-color);
  margin-bottom: 6px;
}

.empty-desc {
  font-size: 13.5px;
  color: var(--text-muted);
  max-width: 440px;
  line-height: 1.45;
  margin-bottom: 20px;
}

/* BUTTONS & CONTROLS */
.oryx-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 20px;
  border-radius: 8px;
  font-size: 13.5px;
  font-weight: 700;
  cursor: pointer;
  border: none;
  transition: all 0.15s ease;
  text-decoration: none;
}

.oryx-btn-primary {
  background: #1F3224 !important;
  color: #FFFFFF !important;
  box-shadow: 0 2px 8px rgba(31, 50, 36, 0.15);
}

.oryx-btn-primary:hover {
  background: #2D4834 !important;
  transform: translateY(-1px);
}

[data-theme="dark"] .oryx-btn-primary {
  background: #1D3D27 !important;
  border: 1px solid #316440 !important;
  color: #FAF8F5 !important;
}

[data-theme="dark"] .oryx-btn-primary:hover {
  background: #254F33 !important;
}

.oryx-btn-secondary {
  background: var(--bg-surface) !important;
  color: var(--text-color) !important;
  border: 1px solid var(--border-color) !important;
}

.oryx-btn-secondary:hover {
  background: var(--border-light) !important;
}

.oryx-btn-express {
  background: linear-gradient(135deg, #00D26A 0%, #059669 100%) !important;
  color: #000000 !important;
  font-weight: 800 !important;
  box-shadow: 0 4px 14px rgba(0, 210, 106, 0.35) !important;
}

.oryx-btn-express:hover {
  background: linear-gradient(135deg, #00FF80 0%, #00D26A 100%) !important;
  transform: translateY(-1px);
  box-shadow: 0 6px 18px rgba(0, 210, 106, 0.45) !important;
}

/* FORM INPUTS & GRIDS */
.form-grid-2 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 16px;
}

.form-grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-bottom: 16px;
}

@media (max-width: 768px) {
  .oryx-stats-grid { grid-template-columns: 1fr; }
  .form-grid-2, .form-grid-3 { grid-template-columns: 1fr; }
  .hero-main-row { flex-direction: column; align-items: flex-start; }
  .oryx-steps-container { flex-direction: column; align-items: flex-start; gap: 12px; }
  .step-divider { display: none; }
}

.form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 14px;
}

.form-label {
  font-size: 12.5px;
  font-weight: 600;
  color: var(--text-color);
  margin-bottom: 6px;
}

.req { color: #DC2626; margin-left: 2px; }

.form-control, .oryx-input, .oryx-select {
  width: 100%;
  padding: 10px 14px;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  background: var(--bg-surface);
  color: var(--text-color);
  font-size: 13.5px;
  font-family: var(--font-body);
  outline: none;
  box-sizing: border-box;
  transition: all 0.15s ease;
}

.form-control:focus, .oryx-input:focus, .oryx-select:focus {
  border-color: var(--primary-color);
  background: var(--bg-card);
  box-shadow: 0 0 0 2px rgba(31, 50, 36, 0.1);
}

[data-theme="dark"] .form-control:focus,
[data-theme="dark"] .oryx-input:focus,
[data-theme="dark"] .oryx-select:focus {
  box-shadow: 0 0 0 2px rgba(0, 210, 106, 0.2);
}

/* PRODUCT CARDS GRID */
.product-cards-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 14px;
  margin-bottom: 20px;
}

@media (max-width: 600px) {
  .product-cards-grid { grid-template-columns: 1fr; }
}

.product-card {
  border: 1.5px solid var(--border-color);
  background: var(--bg-surface);
  border-radius: 12px;
  padding: 16px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.product-card:hover {
  border-color: var(--primary-color);
  background: var(--bg-card);
  transform: translateY(-1px);
}

.product-card.selected {
  border-color: var(--primary-color);
  background: rgba(31, 50, 36, 0.04);
  box-shadow: 0 0 0 2px var(--primary-color);
}

[data-theme="dark"] .product-card.selected {
  border-color: #00D26A;
  background: rgba(0, 210, 106, 0.08);
  box-shadow: 0 0 0 2px #00D26A;
}

.pcard-title {
  font-size: 14.5px;
  font-weight: 700;
  color: var(--text-color);
  margin-bottom: 4px;
}

.pcard-desc {
  font-size: 12px;
  color: var(--text-muted);
  margin-bottom: 8px;
}

.pcard-rate {
  font-size: 12px;
  font-weight: 700;
  color: var(--accent-green);
  font-family: var(--font-mono);
}

/* LIVE METRICS HUD */
.metrics-live-hud {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 16px 20px;
  margin: 20px 0;
}

@media (max-width: 768px) {
  .metrics-live-hud { grid-template-columns: 1fr 1fr; }
}

.hud-title {
  font-size: 10.5px;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.hud-number {
  font-family: var(--font-mono);
  font-size: 17px;
  font-weight: 700;
  color: var(--text-color);
  margin-top: 4px;
}

/* DISBURSAL CARDS */
.disbursal-options-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin-top: 8px;
}

@media (max-width: 600px) {
  .disbursal-options-grid { grid-template-columns: 1fr; }
}

.disbursal-option-card {
  border: 1.5px solid var(--border-color);
  background: var(--bg-surface);
  border-radius: 12px;
  padding: 14px 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  cursor: pointer;
  transition: all 0.15s ease;
}

.disbursal-option-card.selected {
  border-color: var(--primary-color);
  background: rgba(31, 50, 36, 0.04);
  box-shadow: 0 0 0 2px var(--primary-color);
}

[data-theme="dark"] .disbursal-option-card.selected {
  border-color: #00D26A;
  background: rgba(0, 210, 106, 0.08);
  box-shadow: 0 0 0 2px #00D26A;
}

/* SUCCESS CARD */
.oryx-success-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 40px 32px;
  text-align: center;
  box-shadow: var(--card-shadow);
  max-width: 680px;
  margin: 0 auto;
}

.success-icon-wrap {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: rgba(0, 210, 106, 0.15);
  border: 2px solid #00D26A;
  color: #00D26A;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 20px;
}

.success-title {
  font-size: 24px;
  font-weight: 700;
  color: var(--text-color);
  margin-bottom: 8px;
}

.success-desc {
  font-size: 14px;
  color: var(--text-muted);
  max-width: 480px;
  margin: 0 auto 24px;
  line-height: 1.5;
}

.app-ref-box {
  background: var(--bg-surface);
  border: 1px dashed var(--border-color);
  border-radius: 10px;
  padding: 12px 20px;
  display: inline-block;
  margin-bottom: 24px;
}

.ref-label {
  display: block;
  font-size: 11px;
  font-weight: 700;
  color: var(--text-muted);
  text-transform: uppercase;
  margin-bottom: 2px;
}

.ref-code {
  font-family: var(--font-mono);
  font-size: 18px;
  font-weight: 700;
  color: var(--primary-color);
}

[data-theme="dark"] .ref-code {
  color: #00D26A;
}

/* APPLICATIONS LIST CARDS */
.app-item-card {
  border: 1px solid var(--border-color);
  background: var(--bg-surface);
  border-radius: 12px;
  padding: 18px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
  gap: 16px;
}

@media (max-width: 600px) {
  .app-item-card { flex-direction: column; align-items: flex-start; }
}

.app-item-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.app-item-id {
  font-family: var(--font-mono);
  font-size: 13px;
  font-weight: 700;
  color: var(--primary-color);
}

[data-theme="dark"] .app-item-id {
  color: #00D26A;
}

.app-item-prod {
  font-size: 15px;
  font-weight: 700;
  color: var(--text-color);
}

.app-item-meta {
  font-size: 12.5px;
  color: var(--text-muted);
}

.app-item-right {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 6px;
}

@media (max-width: 600px) {
  .app-item-right { align-items: flex-start; }
}

.app-item-amt {
  font-family: var(--font-mono);
  font-size: 17px;
  font-weight: 700;
  color: var(--text-color);
}

.app-item-badge {
  font-size: 11px;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 20px;
  text-transform: uppercase;
}

.badge-review {
  background: #FEF3C7;
  color: #92400E;
  border: 1px solid #FCD34D;
}

[data-theme="dark"] .badge-review {
  background: #3B2D0B;
  color: #FCD34D;
  border-color: #78350F;
}

.badge-approved {
  background: #DCFCE7;
  color: #166534;
  border: 1px solid #86EFAC;
}

[data-theme="dark"] .badge-approved {
  background: #0D3319;
  color: #86EFAC;
  border-color: #14532D;
}
"""

    def build_header(active_tab):
        p_active = ' active' if active_tab == 'portal' else ''
        a_active = ' active' if active_tab == 'apply' else ''
        acc_active = ' active' if active_tab == 'account' else ''

        return """  <!-- Sticky Full-Width Localhost Header -->
  <header class="oryx-navbar">
    <div class="oryx-nav-inner">
      <a href="index.html" class="oryx-brand" title="Oryx Fund">
        <img src="assets/images/oryx_logo_light.png" alt="Oryx Fund" class="oryx-logo-img oryx-logo-light">
        <img src="assets/images/oryx_logo_dark.png" alt="Oryx Fund" class="oryx-logo-img oryx-logo-dark">
      </a>

      <div class="oryx-nav-desktop-capsules">
        <nav class="oryx-capsules-nav">
          <a href="index.html" class="oryx-capsule-tab""" + p_active + """">My Portal</a>
          <a href="apply.html" class="oryx-capsule-tab""" + a_active + """">Loan Application</a>
          <a href="my_account.html" class="oryx-capsule-tab""" + acc_active + """" id="navUserPill">
            <svg class="capsule-user-icon" width="13.5" height="13.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 5px;">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
            <span>Account</span>
          </a>
        </nav>

        <button type="button" class="oryx-theme-toggle-btn" id="oryxThemeToggle" onclick="toggleOryxTheme()" aria-label="Toggle Theme" title="Toggle Light / Dark Mode">
          <svg class="theme-icon sun-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
          <svg class="theme-icon moon-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        </button>
      </div>

      <!-- Mobile Top Right -->
      <div class="oryx-nav-mobile-right">
        <a href="my_account.html" class="oryx-capsule-tab""" + acc_active + """" id="navUserPillMobile">
          <svg class="capsule-user-icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 4px;">
            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
            <circle cx="12" cy="7" r="4"></circle>
          </svg>
          <span>Account</span>
        </a>
        <button type="button" class="oryx-theme-toggle-btn" onclick="toggleOryxTheme()" aria-label="Toggle Theme">
          <svg class="theme-icon sun-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/></svg>
          <svg class="theme-icon moon-icon" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        </button>
      </div>
    </div>

    <!-- Mobile Sub-Header Capsule Tabs Bar -->
    <div class="oryx-mobile-capsules-bar">
      <nav class="oryx-mobile-capsules-track">
        <a href="index.html" class="oryx-capsule-tab""" + p_active + """">My Portal</a>
        <a href="apply.html" class="oryx-capsule-tab""" + a_active + """">Loan Application</a>
        <a href="my_account.html" class="oryx-capsule-tab""" + acc_active + """">Account</a>
      </nav>
    </div>
  </header>"""

    # SHARED CORE CLIENT AUTHENTICATION ENGINE (Web Crypto SHA-256 + Scoped Storage)
    auth_core_script = """
    // =========================================================================
    // ORYX FUND SECURE CLIENT AUTHENTICATION & SESSION MANAGER
    // =========================================================================
    const ORYX_AUTH_SALT = "oryx_fund_2026_salt_sec_";

    async function hashPassword(password) {
      const enc = new TextEncoder();
      const buf = await crypto.subtle.digest("SHA-256", enc.encode(ORYX_AUTH_SALT + password));
      return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
    }

    function initAuthSeeds() {
      // Seed initial default test accounts with SHA-256 hashes if uninitialized
      if (localStorage.getItem('oryx_auth_seeded') !== 'v3') {
        const seedUsers = [
          {
            id: 'usr_reezy_001',
            name: 'Reezy Kariuki',
            email: 'reezyhoops@gmail.com',
            phone: '0712345678',
            nationalId: '32847592',
            kraPin: 'A009847291Z',
            address: 'Kilimani, Ring Road',
            county: 'Nairobi',
            role: 'Borrower',
            passwordHash: 'f8eb476d031f0035a1091eaf6cfaed5efd7f15b31ba6841f21d60dd64adf4e1a', // Secret123
            created_at: new Date().toISOString()
          },
          {
            id: 'usr_admin_001',
            name: 'Oryx Fund Admin',
            email: 'admin@oryxfund.co.ke',
            phone: '+254700000000',
            nationalId: 'ADM-001',
            kraPin: 'A000000000Z',
            address: 'Upper Hill, Nairobi',
            county: 'Nairobi',
            role: 'Admin',
            passwordHash: '3190a7c246a9c205f2ade1cc48ba235429c186dc7a2662be6403a792b74242ef', // Admin@2026!
            created_at: new Date().toISOString()
          }
        ];

        seedUsers.forEach(u => {
          localStorage.setItem('oryx_user_' + u.id, JSON.stringify(u));
          localStorage.setItem('oryx_idx_' + u.email.toLowerCase(), u.id);
          localStorage.setItem('oryx_idx_' + u.phone.replace(/\\s+/g, ''), u.id);
        });

        localStorage.setItem('oryx_auth_seeded', 'v3');
      }
    }
    initAuthSeeds();

    function getAuthSession() {
      try {
        const raw = localStorage.getItem('oryx_auth_user');
        if (!raw) return null;
        const session = JSON.parse(raw);
        // Check session TTL (4 hours)
        if (session.expires_at && Date.now() > session.expires_at) {
          clearAuthSession(false);
          return null;
        }
        return session;
      } catch(e) {
        return null;
      }
    }

    function setAuthSession(user) {
      const session = {
        userId: user.id || ('usr_' + Date.now()),
        name: user.name || 'Borrower',
        email: user.email,
        phone: user.phone,
        nationalId: user.nationalId,
        role: user.role || 'Borrower',
        expires_at: Date.now() + (4 * 3600 * 1000) // 4 hours
      };
      localStorage.setItem('oryx_auth_user', JSON.stringify(session));
      return session;
    }

    function clearAuthSession(redirect = true) {
      localStorage.removeItem('oryx_auth_user');
      if (redirect) {
        window.location.href = 'login.html';
      }
    }

    function requireBorrowerAuth(redirectPage = 'index.html') {
      const session = getAuthSession();
      if (!session) {
        window.location.href = 'login.html?redirect_to=' + encodeURIComponent(redirectPage);
        return null;
      }
      return session;
    }

    function getUserRecord(userId) {
      try {
        return JSON.parse(localStorage.getItem('oryx_user_' + userId));
      } catch(e) { return null; }
    }

    function saveUserRecord(user) {
      if (!user.id) user.id = 'usr_' + Date.now();
      localStorage.setItem('oryx_user_' + user.id, JSON.stringify(user));
      if (user.email) localStorage.setItem('oryx_idx_' + user.email.toLowerCase(), user.id);
      if (user.phone) localStorage.setItem('oryx_idx_' + user.phone.replace(/\\s+/g, ''), user.id);
      return user;
    }

    function getUserScopedApplications(userId) {
      try {
        return JSON.parse(localStorage.getItem('oryx_apps_' + userId) || '[]');
      } catch(e) { return []; }
    }

    function saveUserScopedApplication(userId, appData) {
      const userApps = getUserScopedApplications(userId);
      userApps.unshift(appData);
      localStorage.setItem('oryx_apps_' + userId, JSON.stringify(userApps));

      // Also publish to global underwriting ledger for admin desk
      try {
        const globalApps = JSON.parse(localStorage.getItem('oryx_applications') || '[]');
        globalApps.unshift(appData);
        localStorage.setItem('oryx_applications', JSON.stringify(globalApps));
      } catch(e) {}
    }
    """

    # 2. BORROWER DASHBOARD (index.html, my_loans.html, borrower.html)
    portal_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Loans — Oryx Fund</title>
  <meta name="description" content="View your active loans, outstanding balances, and official M-Pesa Paybill payment instructions.">
  <link rel="icon" type="image/png" href="assets/images/oryx-mark-dark.png">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
""" + css_content + """
  </style>
</head>
<body>

""" + build_header("portal") + """

  <main class="oryx-portal-wrapper">

    <!-- Hero Card (Matching Localhost 1:1) -->
    <div class="oryx-hero-card">
      <div class="hero-top-row">
        <div class="oryx-badge">MY PORTAL</div>
        <span class="user-greeting" id="heroAccountText">Account: Loading...</span>
      </div>
      <div class="hero-main-row">
        <div>
          <h1 class="oryx-title">My Loans &amp; Repayments</h1>
          <p class="oryx-subtitle">View your active loans, outstanding balances, and official M-Pesa Paybill payment instructions.</p>
        </div>
        <div class="hero-cta-box">
          <a href="apply.html" class="oryx-hero-btn">+ Apply for a New Loan</a>
        </div>
      </div>
    </div>

    <!-- Summary KPI Stats Grid -->
    <div class="oryx-stats-grid">
      <div class="oryx-stat-card">
        <div class="stat-icon-wrap">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
            <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
          </svg>
        </div>
        <div class="stat-content">
          <span class="stat-label">Active Loans</span>
          <span class="stat-val" id="statActiveLoans">0</span>
        </div>
      </div>

      <div class="oryx-stat-card">
        <div class="stat-icon-wrap">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="12" y1="1" x2="12" y2="23"></line>
            <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
          </svg>
        </div>
        <div class="stat-content">
          <span class="stat-label">Total Principal Borrowed</span>
          <span class="stat-val" id="statPrincipal">KES 0.00</span>
        </div>
      </div>

      <div class="oryx-stat-card">
        <div class="stat-icon-wrap highlight">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#D97706" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <polyline points="12 6 12 12 16 14"></polyline>
          </svg>
        </div>
        <div class="stat-content">
          <span class="stat-label">Outstanding Balance</span>
          <span class="stat-val" id="statOutstanding">KES 0.00</span>
        </div>
      </div>
    </div>

    <!-- Active Loans Section -->
    <div class="oryx-portal-card">
      <div class="card-section-head">
        <div>
          <h3 class="section-title">Active Loans</h3>
          <p class="section-desc">Manage existing loan terms, disbursals, and repayments.</p>
        </div>
      </div>

      <div class="oryx-empty-state" id="loansEmptyState">
        <div class="empty-icon-wrap">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
            <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
          </svg>
        </div>
        <h4 class="empty-title">No Active Loans</h4>
        <p class="empty-desc">You do not currently have any active loans. You can submit a new loan application in under 2 minutes.</p>
        <a href="apply.html" class="oryx-btn oryx-btn-primary">+ Apply for a Loan</a>
      </div>

      <div id="activeLoansContainer" style="display:none;"></div>
    </div>

    <!-- Application History Section -->
    <div class="oryx-portal-card">
      <div class="card-section-head">
        <div>
          <h3 class="section-title">Application History</h3>
          <p class="section-desc">Track status and review records of your submitted loan applications.</p>
        </div>
      </div>

      <div class="oryx-empty-state" id="appsEmptyState">
        <div class="empty-icon-wrap">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
            <polyline points="14 2 14 8 20 8"></polyline>
            <line x1="16" y1="13" x2="8" y2="13"></line>
            <line x1="16" y1="17" x2="8" y2="17"></line>
            <polyline points="10 9 9 9 8 9"></polyline>
          </svg>
        </div>
        <h4 class="empty-title">No Applications Found</h4>
        <p class="empty-desc">Your submitted applications will appear here with real-time status updates.</p>
      </div>

      <div id="appsListContainer" style="display:none;"></div>
    </div>

  </main>

  <script>
""" + auth_core_script + """

    function toggleOryxTheme() {
      const html = document.documentElement;
      const cur = html.getAttribute('data-theme') || 'light';
      const next = cur === 'light' ? 'dark' : 'light';
      html.setAttribute('data-theme', next);
      html.classList.toggle('dark', next === 'dark');
      localStorage.setItem('oryx_theme', next);
    }
    const savedTheme = localStorage.getItem('oryx_theme');
    if (savedTheme) {
      document.documentElement.setAttribute('data-theme', savedTheme);
      document.documentElement.classList.toggle('dark', savedTheme === 'dark');
    }

    document.addEventListener('DOMContentLoaded', () => {
      // 1. Enforce Borrower Route Guard
      const session = requireBorrowerAuth('index.html');
      if (!session) return;

      // 2. Render dynamic user identification
      document.getElementById('heroAccountText').innerText = 'Account: ' + (session.email || session.phone);
      const displayName = session.name || (session.email ? session.email.split('@')[0] : 'Borrower');
      document.querySelectorAll('#navUserPill span, #navUserPillMobile span').forEach(el => el.innerText = displayName);

      // 3. Render User-Scoped Applications (Zero Cross-Account Leakage)
      const userApps = getUserScopedApplications(session.userId);
      if (userApps.length > 0) {
        document.getElementById('appsEmptyState').style.display = 'none';
        const listEl = document.getElementById('appsListContainer');
        listEl.style.display = 'block';
        listEl.innerHTML = '';

        userApps.forEach(app => {
          const card = document.createElement('div');
          card.className = 'app-item-card';
          card.innerHTML = `
            <div class="app-item-info">
              <div class="app-item-id">${app.id || 'ACC-LOAP-2026-001'}</div>
              <div class="app-item-prod">${app.productName || 'Working Capital Facility'}</div>
              <div class="app-item-meta">Applicant: ${app.fullName || session.name} &bull; ${app.date || 'Today'} &bull; ${app.term || '6'} Months</div>
            </div>
            <div class="app-item-right">
              <div class="app-item-amt">KES ${Number(app.amount || 250000).toLocaleString('en-US', {minimumFractionDigits: 2})}</div>
              <span class="app-item-badge badge-review">⚡ ${app.status || 'Under Review'}</span>
            </div>
          `;
          listEl.appendChild(card);
        });
      }
    });
  </script>
</body>
</html>
"""

    # 3. 4-STEP LOAN APPLICATION WIZARD (apply.html)
    apply_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Apply for a Loan — Oryx Fund</title>
  <meta name="description" content="Instant digital loan application portal for Oryx Fund.">
  <link rel="icon" type="image/png" href="assets/images/oryx-mark-dark.png">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
""" + css_content + """
  </style>
</head>
<body>

""" + build_header("apply") + """

  <main class="oryx-portal-wrapper">

    <!-- Top Hero Card (Matching Localhost 1:1) -->
    <div class="oryx-hero-card">
      <div class="hero-top-row">
        <div class="oryx-badge">LOAN APPLICATION</div>
        <span class="user-greeting" id="heroGreetingText">Fast 2-Minute Application</span>
      </div>
      <div class="hero-main-row">
        <div class="hero-title-box">
          <h1 class="oryx-title">Loan Application Form</h1>
          <p class="oryx-subtitle">Fast, transparent financing for business advances, working capital, and term financing in Kenya.</p>
        </div>
      </div>
      
      <!-- 4-Step Indicator -->
      <div class="oryx-steps-container">
        <div class="oryx-step active" id="step-badge-1" onclick="goToStep(1)">
          <span class="step-num">1</span>
          <span class="step-label">Personal KYC</span>
        </div>
        <div class="step-divider" id="step-div-1"></div>
        <div class="oryx-step" id="step-badge-2" onclick="goToStep(2)">
          <span class="step-num">2</span>
          <span class="step-label">Loan Specs</span>
        </div>
        <div class="step-divider" id="step-div-2"></div>
        <div class="oryx-step" id="step-badge-3" onclick="goToStep(3)">
          <span class="step-num">3</span>
          <span class="step-label">Cashflow &amp; Guarantor</span>
        </div>
        <div class="step-divider" id="step-div-3"></div>
        <div class="oryx-step" id="step-badge-4" onclick="goToStep(4)">
          <span class="step-num">4</span>
          <span class="step-label">Consent &amp; Submit</span>
        </div>
      </div>
    </div>

    <!-- Form Container -->
    <div class="oryx-portal-card" id="formCardWrapper">
      <form id="oryxLoanForm" onsubmit="return false;">

        <!-- STEP 1: Personal KYC & Contact Details -->
        <div id="step-1-content" class="wizard-step-pane">
          <div class="card-section-head">
            <div>
              <h3 class="section-title">1. Personal Identity &amp; Contact Details</h3>
              <p class="section-desc">Please enter your legal identity as indicated on your National ID or Passport.</p>
            </div>
          </div>

          <div class="form-grid-2">
            <div class="form-group">
              <label class="form-label">Full Legal Name <span class="req">*</span></label>
              <input type="text" id="app_fullname" class="form-control" placeholder="e.g. James Mwangi Kariuki">
            </div>
            <div class="form-group">
              <label class="form-label">National ID / Passport Number <span class="req">*</span></label>
              <input type="text" id="app_national_id" class="form-control" placeholder="e.g. 12345678">
            </div>
          </div>

          <div class="form-grid-3">
            <div class="form-group">
              <label class="form-label">KRA PIN Number <span class="req">*</span></label>
              <input type="text" id="app_kra_pin" class="form-control" placeholder="E.G. A012345678Z" value="A009847291Z" style="text-transform:uppercase;">
            </div>
            <div class="form-group">
              <label class="form-label">Date of Birth</label>
              <input type="date" id="app_dob" class="form-control" value="1992-06-15">
            </div>
            <div class="form-group">
              <label class="form-label">Gender</label>
              <select id="app_gender" class="form-control">
                <option value="Male" selected>Male</option>
                <option value="Female">Female</option>
                <option value="Other">Other</option>
              </select>
            </div>
          </div>

          <div class="form-grid-2">
            <div class="form-group">
              <label class="form-label">Primary Phone Number (M-Pesa Registered) <span class="req">*</span></label>
              <input type="tel" id="app_phone" class="form-control" placeholder="e.g. 0712345678">
            </div>
            <div class="form-group">
              <label class="form-label">Email Address</label>
              <input type="email" id="app_email" class="form-control" placeholder="e.g. james@example.com">
            </div>
          </div>

          <div class="form-grid-3">
            <div class="form-group">
              <label class="form-label">Residential Physical Address <span class="req">*</span></label>
              <input type="text" id="app_address" class="form-control" placeholder="e.g. Kilimani, Ring Road" value="Kilimani, Ring Road">
            </div>
            <div class="form-group">
              <label class="form-label">Estate / House Number</label>
              <input type="text" id="app_estate" class="form-control" placeholder="e.g. House No. B4, Palm Court" value="House No. B4, Palm Court">
            </div>
            <div class="form-group">
              <label class="form-label">County <span class="req">*</span></label>
              <select id="app_county" class="form-control">
                <option value="Nairobi" selected>Nairobi</option>
                <option value="Mombasa">Mombasa</option>
                <option value="Kiambu">Kiambu</option>
                <option value="Nakuru">Nakuru</option>
                <option value="Kisumu">Kisumu</option>
                <option value="Machakos">Machakos</option>
                <option value="Kajiado">Kajiado</option>
              </select>
            </div>
          </div>

          <div class="form-group">
            <label class="form-label">Residence Ownership Status</label>
            <select id="app_ownership" class="form-control">
              <option value="Rented" selected>Rented</option>
              <option value="Owner Occupier / Mortgaged">Owner Occupier / Mortgaged</option>
              <option value="Living with Family">Living with Family</option>
            </select>
          </div>

          <div class="card-section-head" style="margin-top:24px;">
            <div>
              <h3 class="section-title">Next of Kin Details</h3>
              <p class="section-desc">Contact person in case of an emergency.</p>
            </div>
          </div>

          <div class="form-grid-3">
            <div class="form-group">
              <label class="form-label">Next of Kin Full Name <span class="req">*</span></label>
              <input type="text" id="app_kin_name" class="form-control" placeholder="e.g. Mary Wanjiku" value="Mary Wanjiku Mwangi">
            </div>
            <div class="form-group">
              <label class="form-label">Relationship <span class="req">*</span></label>
              <input type="text" id="app_kin_relation" class="form-control" placeholder="e.g. Spouse / Sister" value="Spouse">
            </div>
            <div class="form-group">
              <label class="form-label">Next of Kin Phone Number <span class="req">*</span></label>
              <input type="tel" id="app_kin_phone" class="form-control" placeholder="e.g. 0722000000" value="0722000000">
            </div>
          </div>

          <div style="display:flex; justify-content:flex-end; margin-top:24px;">
            <button type="button" class="oryx-btn oryx-btn-primary" onclick="goToStep(2)">Continue to Loan Specs &rarr;</button>
          </div>
        </div>

        <!-- STEP 2: Facility Specs, Calculator & Disbursal -->
        <div id="step-2-content" class="wizard-step-pane" style="display:none;">
          <div class="card-section-head">
            <div>
              <h3 class="section-title">2. Choose Loan Facility &amp; Requested Amount</h3>
              <p class="section-desc">Select your desired facility. Repayment estimates update in real time.</p>
            </div>
          </div>

          <label class="form-label" style="font-size:13.5px; margin-bottom:10px;">Select Loan Facility <span class="req">*</span></label>
          <div class="product-cards-grid">
            <div class="product-card selected" onclick="selectProduct('Working Capital Facility', 1.5, this)">
              <div class="pcard-title">Working Capital Loan</div>
              <div class="pcard-desc">Short-term inventory financing and cashflow bridge for SMEs.</div>
              <div class="pcard-rate">1.5% Monthly &bull; Up to KES 2,500,000</div>
            </div>

            <div class="product-card" onclick="selectProduct('Asset Financing Facility', 1.2, this)">
              <div class="pcard-title">Asset Financing</div>
              <div class="pcard-desc">Commercial vehicle, equipment, and machinery purchases.</div>
              <div class="pcard-rate">1.2% Monthly &bull; Up to KES 5,000,000</div>
            </div>

            <div class="product-card" onclick="selectProduct('Term Growth Loan', 1.8, this)">
              <div class="pcard-title">Term Growth Facility</div>
              <div class="pcard-desc">Longer-tenor growth capital for expansion and operations.</div>
              <div class="pcard-rate">1.8% Monthly &bull; Up to KES 3,000,000</div>
            </div>

            <div class="product-card" onclick="selectProduct('Emergency Credit Line', 2.0, this)">
              <div class="pcard-title">Emergency Rapid Credit</div>
              <div class="pcard-desc">Instant 24-hour turnaround for unexpected cash demands.</div>
              <div class="pcard-rate">2.0% Monthly &bull; Up to KES 500,000</div>
            </div>
          </div>

          <div style="background:var(--bg-surface); border:1px solid var(--border-color); border-radius:12px; padding:20px; margin-bottom:20px;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
              <span class="form-label" style="margin:0;">Requested Loan Amount (KES)</span>
              <span id="displayAmount" style="font-family:var(--font-mono); font-size:20px; font-weight:700; color:var(--primary-color);">KES 250,000</span>
            </div>
            <input type="range" id="amountSlider" min="10000" max="2500000" step="10000" value="250000" oninput="updateCalculator()" style="width:100%; cursor:pointer; accent-color:var(--accent-emerald);">

            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:20px; margin-bottom:10px;">
              <span class="form-label" style="margin:0;">Repayment Duration</span>
              <span id="displayTerm" style="font-family:var(--font-mono); font-size:18px; font-weight:700; color:var(--primary-color);">6 Months</span>
            </div>
            <input type="range" id="termSlider" min="1" max="12" step="1" value="6" oninput="updateCalculator()" style="width:100%; cursor:pointer; accent-color:var(--accent-emerald);">

            <!-- Live Calculation HUD -->
            <div class="metrics-live-hud">
              <div>
                <div class="hud-title">Principal</div>
                <div class="hud-number" id="hudPrincipal">KES 250,000</div>
              </div>
              <div>
                <div class="hud-title">Monthly Rate</div>
                <div class="hud-number" id="hudRate">1.50%</div>
              </div>
              <div>
                <div class="hud-title">Est. Monthly Payment</div>
                <div class="hud-number" id="hudMonthly" style="color:var(--accent-green);">KES 45,416</div>
              </div>
              <div>
                <div class="hud-title">Total Repayable</div>
                <div class="hud-number" id="hudTotal">KES 272,500</div>
              </div>
            </div>
          </div>

          <label class="form-label" style="font-size:13.5px; margin-bottom:10px;">Confirm Disbursal Destination <span class="req">*</span></label>
          <div class="disbursal-options-grid">
            <div class="disbursal-option-card selected" id="optDisbMpesa" onclick="selectDisbursal('M-Pesa')">
              <input type="radio" name="disb_type" value="M-Pesa" checked>
              <div>
                <div style="font-weight:700; font-size:14px; color:var(--text-color);">M-Pesa Direct Disbursal ⚡ Instant</div>
                <div style="font-size:12px; color:var(--text-muted);">Funds sent directly to registered mobile number</div>
              </div>
            </div>
            <div class="disbursal-option-card" id="optDisbBank" onclick="selectDisbursal('Bank')">
              <input type="radio" name="disb_type" value="Bank">
              <div>
                <div style="font-weight:700; font-size:14px; color:var(--text-color);">Bank Wire (EFT / RTGS)</div>
                <div style="font-size:12px; color:var(--text-muted);">Direct bank account transfer (Same Day)</div>
              </div>
            </div>
          </div>

          <div style="display:flex; justify-content:space-between; margin-top:28px;">
            <button type="button" class="oryx-btn oryx-btn-secondary" onclick="goToStep(1)">&larr; Back to KYC</button>
            <button type="button" class="oryx-btn oryx-btn-primary" onclick="goToStep(3)">Continue to Cashflow & Guarantor &rarr;</button>
          </div>
        </div>

        <!-- STEP 3: Cashflow & Financial Profile -->
        <div id="step-3-content" class="wizard-step-pane" style="display:none;">
          <div class="card-section-head">
            <div>
              <h3 class="section-title">3. Monthly Cashflow &amp; Guarantor Details</h3>
              <p class="section-desc">Provide income details for credit scoring and facility sanctioning.</p>
            </div>
          </div>

          <div class="form-grid-3">
            <div class="form-group">
              <label class="form-label">Employment / Business Status <span class="req">*</span></label>
              <select id="app_emp_status" class="form-control">
                <option value="Self-Employed / Business Owner" selected>Self-Employed / Business Owner</option>
                <option value="Permanent / Salaried">Permanent / Salaried</option>
                <option value="Contract">Contract</option>
              </select>
            </div>
            <div class="form-group">
              <label class="form-label">Employer / Business Name <span class="req">*</span></label>
              <input type="text" id="app_employer" class="form-control" placeholder="e.g. Apex Retail Enterprises" value="Apex Retail Enterprises">
            </div>
            <div class="form-group">
              <label class="form-label">Monthly Net Income (KES) <span class="req">*</span></label>
              <input type="number" id="app_income" class="form-control" value="180000">
            </div>
          </div>

          <div class="form-grid-2">
            <div class="form-group">
              <label class="form-label">Monthly Debt Obligations (KES)</label>
              <input type="number" id="app_debt" class="form-control" value="25000">
            </div>
            <div class="form-group">
              <label class="form-label">Monthly Fixed Living Expenses (KES)</label>
              <input type="number" id="app_expenses" class="form-control" value="45000">
            </div>
          </div>

          <div class="card-section-head" style="margin-top:24px;">
            <div>
              <h3 class="section-title">Guarantor Information</h3>
              <p class="section-desc">Primary guarantor for facilities above KES 100,000.</p>
            </div>
          </div>

          <div class="form-grid-2">
            <div class="form-group">
              <label class="form-label">Guarantor Full Legal Name</label>
              <input type="text" id="app_guar_name" class="form-control" placeholder="e.g. David Kipchoge" value="David Kipchoge">
            </div>
            <div class="form-group">
              <label class="form-label">Guarantor National ID</label>
              <input type="text" id="app_guar_id" class="form-control" placeholder="e.g. 24891048" value="24891048">
            </div>
          </div>

          <div class="form-grid-2">
            <div class="form-group">
              <label class="form-label">Guarantor Phone Number</label>
              <input type="tel" id="app_guar_phone" class="form-control" placeholder="e.g. 0721888999" value="0721888999">
            </div>
            <div class="form-group">
              <label class="form-label">Relationship to Applicant</label>
              <input type="text" id="app_guar_rel" class="form-control" placeholder="e.g. Business Partner" value="Business Partner">
            </div>
          </div>

          <div style="display:flex; justify-content:space-between; margin-top:28px;">
            <button type="button" class="oryx-btn oryx-btn-secondary" onclick="goToStep(2)">&larr; Back to Loan Specs</button>
            <button type="button" class="oryx-btn oryx-btn-primary" onclick="goToStep(4)">Continue to Review &amp; Submit &rarr;</button>
          </div>
        </div>

        <!-- STEP 4: Review & Consent -->
        <div id="step-4-content" class="wizard-step-pane" style="display:none;">
          <div class="card-section-head">
            <div>
              <h3 class="section-title">4. Review Loan Parameters &amp; Declarations</h3>
              <p class="section-desc">Verify your facility specifications before final underwriting submission.</p>
            </div>
          </div>

          <!-- Application Review Card -->
          <div style="background:var(--bg-surface); border:1px solid var(--border-color); border-radius:12px; padding:24px; margin-bottom:24px;">
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
              <div>
                <span class="stat-label">Applicant Name</span>
                <div style="font-weight:700; color:var(--text-color);" id="revName">-</div>
              </div>
              <div>
                <span class="stat-label">National ID / Phone</span>
                <div style="font-weight:700; color:var(--text-color);" id="revIdPhone">-</div>
              </div>
              <div>
                <span class="stat-label">Facility Selected</span>
                <div style="font-weight:700; color:var(--text-color);" id="revProduct">Working Capital Facility</div>
              </div>
              <div>
                <span class="stat-label">Disbursal Method</span>
                <div style="font-weight:700; color:var(--accent-green);" id="revDisb">M-Pesa Direct Disbursal</div>
              </div>
              <div>
                <span class="stat-label">Requested Principal</span>
                <div style="font-family:var(--font-mono); font-size:18px; font-weight:700; color:var(--primary-color);" id="revPrincipal">KES 250,000.00</div>
              </div>
              <div>
                <span class="stat-label">Monthly Repayment &bull; Term</span>
                <div style="font-family:var(--font-mono); font-size:18px; font-weight:700; color:var(--accent-green);" id="revMonthly">KES 45,416 / mo (6 Mo)</div>
              </div>
            </div>
          </div>

          <div style="margin-bottom:24px;">
            <label style="display:flex; align-items:flex-start; gap:10px; cursor:pointer; font-size:13px; color:var(--text-color);">
              <input type="checkbox" id="consentCheck" checked style="margin-top:3px; accent-color:var(--accent-emerald);">
              <span>I hereby certify that all information submitted is truthful and complete. I authorize Oryx Fund Ltd to evaluate my creditworthiness with licensed Credit Reference Bureaus (CRB) and process disbursal according to the specified terms.</span>
            </label>
          </div>

          <div style="display:flex; justify-content:space-between; margin-top:28px;">
            <button type="button" class="oryx-btn oryx-btn-secondary" onclick="goToStep(3)">&larr; Back</button>
            <button type="button" class="oryx-btn oryx-btn-express" onclick="submitApplication()"><span>⚡ Submit Loan Application</span></button>
          </div>
        </div>

      </form>
    </div>

    <!-- Success Screen (Hidden initially) -->
    <div id="successScreen" class="oryx-success-card" style="display:none;">
      <div class="success-icon-wrap">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
      </div>
      <div class="oryx-badge" style="background:rgba(0,210,106,0.15); border-color:#00D26A; color:#00D26A; margin-bottom:12px;">⚡ PRIORITY DISBURSAL QUEUE</div>
      <h2 class="success-title">Loan Application Received!</h2>
      <p class="success-desc">Your loan application has been registered with priority underwriting. You will receive an SMS and email notification once verified.</p>
      
      <div class="app-ref-box">
        <span class="ref-label">Loan Application Reference</span>
        <span class="ref-code" id="successRefCode">ACC-LOAP-2026-94812</span>
      </div>

      <div style="display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
        <a href="index.html" class="oryx-btn oryx-btn-primary">View in My Portal &rarr;</a>
        <a href="my_account.html" class="oryx-btn oryx-btn-secondary">My Account Details</a>
      </div>
    </div>

  </main>

  <script>
""" + auth_core_script + """

    let currentSession = null;
    let selectedFacility = 'Working Capital Facility';
    let selectedRate = 1.5;
    let selectedDisbursalMethod = 'M-Pesa';

    function toggleOryxTheme() {
      const html = document.documentElement;
      const cur = html.getAttribute('data-theme') || 'light';
      const next = cur === 'light' ? 'dark' : 'light';
      html.setAttribute('data-theme', next);
      html.classList.toggle('dark', next === 'dark');
      localStorage.setItem('oryx_theme', next);
    }
    const savedTheme = localStorage.getItem('oryx_theme');
    if (savedTheme) {
      document.documentElement.setAttribute('data-theme', savedTheme);
      document.documentElement.classList.toggle('dark', savedTheme === 'dark');
    }

    function goToStep(step) {
      for (let i = 1; i <= 4; i++) {
        const pane = document.getElementById('step-' + i + '-content');
        const badge = document.getElementById('step-badge-' + i);
        const divider = document.getElementById('step-div-' + (i - 1));

        if (pane) pane.style.display = (i === step) ? 'block' : 'none';
        if (badge) {
          badge.classList.remove('active', 'completed');
          if (i === step) badge.classList.add('active');
          else if (i < step) badge.classList.add('completed');
        }
        if (divider) {
          divider.classList.toggle('completed', i <= step);
        }
      }

      if (step === 4) {
        populateReview();
      }

      window.scrollTo({ top: 120, behavior: 'smooth' });
    }

    function selectProduct(name, rate, el) {
      selectedFacility = name;
      selectedRate = rate;
      document.querySelectorAll('.product-card').forEach(c => c.classList.remove('selected'));
      el.classList.add('selected');
      updateCalculator();
    }

    function selectDisbursal(method) {
      selectedDisbursalMethod = method;
      document.getElementById('optDisbMpesa').classList.toggle('selected', method === 'M-Pesa');
      document.getElementById('optDisbBank').classList.toggle('selected', method === 'Bank');
    }

    function updateCalculator() {
      const amt = parseInt(document.getElementById('amountSlider').value);
      const term = parseInt(document.getElementById('termSlider').value);

      document.getElementById('displayAmount').innerText = 'KES ' + amt.toLocaleString();
      document.getElementById('displayTerm').innerText = term + (term === 1 ? ' Month' : ' Months');

      document.getElementById('hudPrincipal').innerText = 'KES ' + amt.toLocaleString();
      document.getElementById('hudRate').innerText = selectedRate.toFixed(2) + '%';

      const totalInterest = amt * (selectedRate / 100) * term;
      const totalRepay = amt + totalInterest;
      const monthly = Math.round(totalRepay / term);

      document.getElementById('hudMonthly').innerText = 'KES ' + monthly.toLocaleString();
      document.getElementById('hudTotal').innerText = 'KES ' + Math.round(totalRepay).toLocaleString();
    }

    function populateReview() {
      const name = document.getElementById('app_fullname').value;
      const id = document.getElementById('app_national_id').value;
      const phone = document.getElementById('app_phone').value;
      const amt = parseInt(document.getElementById('amountSlider').value);
      const term = parseInt(document.getElementById('termSlider').value);
      const totalInterest = amt * (selectedRate / 100) * term;
      const totalRepay = amt + totalInterest;
      const monthly = Math.round(totalRepay / term);

      document.getElementById('revName').innerText = name;
      document.getElementById('revIdPhone').innerText = id + ' • ' + phone;
      document.getElementById('revProduct').innerText = selectedFacility;
      document.getElementById('revDisb').innerText = selectedDisbursalMethod === 'M-Pesa' ? 'M-Pesa Direct (' + phone + ')' : 'Bank Wire';
      document.getElementById('revPrincipal').innerText = 'KES ' + amt.toLocaleString() + '.00';
      document.getElementById('revMonthly').innerText = 'KES ' + monthly.toLocaleString() + ' / mo (' + term + ' Mo)';
    }

    function submitApplication() {
      const name = document.getElementById('app_fullname').value.trim();
      const id = document.getElementById('app_national_id').value.trim();
      const phone = document.getElementById('app_phone').value.trim();
      const amt = parseInt(document.getElementById('amountSlider').value);
      const term = parseInt(document.getElementById('termSlider').value);
      const randomCode = 'ACC-LOAP-2026-' + Math.floor(10000 + Math.random() * 90000);

      const appData = {
        id: randomCode,
        fullName: name,
        nationalId: id,
        phone: phone,
        productName: selectedFacility,
        amount: amt,
        term: term,
        date: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
        status: 'Under Review'
      };

      // Save to User-Scoped Storage
      saveUserScopedApplication(currentSession ? currentSession.userId : 'usr_default', appData);

      document.getElementById('formCardWrapper').style.display = 'none';
      document.getElementById('successRefCode').innerText = randomCode;
      document.getElementById('successScreen').style.display = 'block';
    }

    document.addEventListener('DOMContentLoaded', () => {
      // 1. Enforce Borrower Route Guard
      currentSession = requireBorrowerAuth('apply.html');
      if (!currentSession) return;

      // 2. Prefill form fields with authenticated borrower's data
      const userRec = getUserRecord(currentSession.userId) || currentSession;
      if (userRec) {
        if (userRec.name) document.getElementById('app_fullname').value = userRec.name;
        if (userRec.nationalId) document.getElementById('app_national_id').value = userRec.nationalId;
        if (userRec.kraPin) document.getElementById('app_kra_pin').value = userRec.kraPin;
        if (userRec.phone) document.getElementById('app_phone').value = userRec.phone;
        if (userRec.email) document.getElementById('app_email').value = userRec.email;
        if (userRec.address) document.getElementById('app_address').value = userRec.address;
        if (userRec.county) document.getElementById('app_county').value = userRec.county;
      }

      const displayName = currentSession.name || (currentSession.email ? currentSession.email.split('@')[0] : 'Borrower');
      document.querySelectorAll('#navUserPill span, #navUserPillMobile span').forEach(el => el.innerText = displayName);

      updateCalculator();
    });
  </script>
</body>
</html>
"""

    # 4. MY ACCOUNT (my_account.html)
    account_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Account — Oryx Fund</title>
  <meta name="description" content="Manage your borrower profile, KYC verification, and security settings.">
  <link rel="icon" type="image/png" href="assets/images/oryx-mark-dark.png">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
""" + css_content + """
  </style>
</head>
<body>

""" + build_header("account") + """

  <main class="oryx-portal-wrapper">

    <!-- Hero Card -->
    <div class="oryx-hero-card">
      <div class="hero-top-row">
        <div class="oryx-badge">MY ACCOUNT</div>
        <span class="user-greeting" id="heroAccountText">Account: Loading...</span>
      </div>
      <div class="hero-main-row">
        <div>
          <h1 class="oryx-title">Borrower Profile &amp; Security</h1>
          <p class="oryx-subtitle">Manage verified personal identification, contact records, and active sessions.</p>
        </div>
        <div class="hero-cta-box">
          <a href="apply.html" class="oryx-hero-btn">+ Apply for a New Loan</a>
        </div>
      </div>
    </div>

    <!-- 2-Column Account Grid -->
    <div style="display:grid; grid-template-columns:2fr 1.2fr; gap:20px;">
      
      <!-- Profile Details Card -->
      <div class="oryx-portal-card">
        <div class="card-section-head">
          <div>
            <h3 class="section-title">Verified Identity &amp; Contact</h3>
            <p class="section-desc">Level 1 KYC Clearance Active &bull; National Registry Verified</p>
          </div>
          <span style="background:#DCFCE7; color:#166534; border:1px solid #86EFAC; font-size:11px; font-weight:700; padding:4px 10px; border-radius:20px;">Verified &check;</span>
        </div>

        <div class="form-grid-2">
          <div class="form-group">
            <label class="form-label">Full Legal Name</label>
            <input type="text" id="accFullName" class="form-control" value="Loading...">
          </div>
          <div class="form-group">
            <label class="form-label">National ID Number</label>
            <input type="text" id="accNationalId" class="form-control" value="Loading..." readonly style="opacity:0.85;">
          </div>
        </div>

        <div class="form-grid-2">
          <div class="form-group">
            <label class="form-label">KRA PIN</label>
            <input type="text" id="accKraPin" class="form-control" value="A009847291Z" readonly style="opacity:0.85;">
          </div>
          <div class="form-group">
            <label class="form-label">Primary Mobile</label>
            <input type="text" id="accPhone" class="form-control" value="0712345678">
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">Email Address</label>
          <input type="email" id="accEmail" class="form-control" value="loading@example.com">
        </div>

        <div class="form-grid-2">
          <div class="form-group">
            <label class="form-label">Residential Address</label>
            <input type="text" id="accAddress" class="form-control" value="Kilimani, Ring Road">
          </div>
          <div class="form-group">
            <label class="form-label">County</label>
            <input type="text" id="accCounty" class="form-control" value="Nairobi">
          </div>
        </div>

        <div style="margin-top:16px;">
          <button type="button" class="oryx-btn oryx-btn-primary" onclick="saveProfileChanges()">Save Profile Updates</button>
        </div>
      </div>

      <!-- Security & Session Card (Strictly Isolated, No Admin Link) -->
      <div class="oryx-portal-card">
        <div class="card-section-head">
          <div>
            <h3 class="section-title">Security &amp; Session</h3>
            <p class="section-desc">Active credentials &bull; Device auth</p>
          </div>
        </div>

        <div style="margin-bottom:20px;">
          <div class="stat-label">Session Status</div>
          <div style="display:flex; align-items:center; gap:8px; margin-top:4px;">
            <span style="width:8px; height:8px; border-radius:50%; background:#00D26A; display:inline-block;"></span>
            <span style="font-weight:700; font-size:14px; color:var(--text-color);">Active &bull; Authenticated</span>
          </div>
        </div>

        <div style="margin-bottom:20px;">
          <div class="stat-label">Account Role</div>
          <div style="font-weight:700; font-size:14px; color:var(--text-color); margin-top:4px;">Registered Borrower (Standard)</div>
        </div>

        <div style="border-top:1px solid var(--border-light); padding-top:20px; margin-top:20px;">
          <button type="button" class="oryx-btn" style="width:100%; background:transparent; border:1px solid #DC2626; color:#DC2626; font-weight:700; cursor:pointer;" onclick="logout()">
            Sign Out
          </button>
        </div>
      </div>

    </div>

  </main>

  <script>
""" + auth_core_script + """

    let currentSession = null;

    function toggleOryxTheme() {
      const html = document.documentElement;
      const cur = html.getAttribute('data-theme') || 'light';
      const next = cur === 'light' ? 'dark' : 'light';
      html.setAttribute('data-theme', next);
      html.classList.toggle('dark', next === 'dark');
      localStorage.setItem('oryx_theme', next);
    }
    const savedTheme = localStorage.getItem('oryx_theme');
    if (savedTheme) {
      document.documentElement.setAttribute('data-theme', savedTheme);
      document.documentElement.classList.toggle('dark', savedTheme === 'dark');
    }

    function logout() {
      clearAuthSession(true);
    }

    function saveProfileChanges() {
      if (!currentSession) return;
      const user = getUserRecord(currentSession.userId) || currentSession;
      user.name = document.getElementById('accFullName').value.trim();
      user.phone = document.getElementById('accPhone').value.trim();
      user.email = document.getElementById('accEmail').value.trim();
      user.address = document.getElementById('accAddress').value.trim();
      user.county = document.getElementById('accCounty').value.trim();

      saveUserRecord(user);
      setAuthSession(user);
      alert('✨ Profile details updated successfully!');
      window.location.reload();
    }

    document.addEventListener('DOMContentLoaded', () => {
      // 1. Enforce Borrower Route Guard
      currentSession = requireBorrowerAuth('my_account.html');
      if (!currentSession) return;

      // 2. Load User Profile
      const userRec = getUserRecord(currentSession.userId) || currentSession;
      document.getElementById('heroAccountText').innerText = 'Account: ' + (userRec.email || userRec.phone);
      document.getElementById('accFullName').value = userRec.name || 'Borrower';
      document.getElementById('accNationalId').value = userRec.nationalId || '32847592';
      document.getElementById('accKraPin').value = userRec.kraPin || 'A009847291Z';
      document.getElementById('accPhone').value = userRec.phone || '0712345678';
      document.getElementById('accEmail').value = userRec.email || 'borrower@example.com';
      document.getElementById('accAddress').value = userRec.address || 'Kilimani, Ring Road';
      document.getElementById('accCounty').value = userRec.county || 'Nairobi';

      const displayName = userRec.name || (userRec.email ? userRec.email.split('@')[0] : 'Borrower');
      document.querySelectorAll('#navUserPill span, #navUserPillMobile span').forEach(el => el.innerText = displayName);
    });
  </script>
</body>
</html>
"""

    # 5. AUTHENTICATION & LOGIN PAGE (login.html)
    login_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Borrower Portal — Oryx Fund</title>
  <meta name="description" content="Secure authentication portal for Oryx Fund borrowers and administrators.">
  <link rel="icon" type="image/png" href="assets/images/oryx-mark-dark.png">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg-body: #EAE0D8;
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
      --bg-body: #080D0A;
      --bg-surface: #101712;
      --bg-surface-alt: #141F17;
      --border-color: #1E2D22;
      --border-light: #18241B;
      --text-primary: #FAF8F5;
      --text-secondary: #A1B2A6;
      --text-muted: #6B7C70;
      --primary: #00D26A;
      --accent-green: #00D26A;
      --accent-emerald: #00D26A;
      --card-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    body {
      background-color: var(--bg-body) !important;
      color: var(--text-primary);
      font-family: var(--font-body);
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px 16px;
    }

    .auth-box {
      width: 100%;
      max-width: 440px;
      margin: 0 auto;
    }

    .auth-brand-head {
      text-align: center;
      margin-bottom: 24px;
    }

    .auth-brand-logo {
      display: inline-block;
    }

    .oryx-auth-logo {
      height: 48px;
      width: auto;
      max-width: 180px;
      object-fit: contain;
    }

    .oryx-logo-light-img { display: inline-block; }
    .oryx-logo-dark-img { display: none; }

    [data-theme="dark"] .oryx-logo-light-img,
    html.dark .oryx-logo-light-img {
      display: none;
    }

    [data-theme="dark"] .oryx-logo-dark-img,
    html.dark .oryx-logo-dark-img {
      display: inline-block;
    }

    .auth-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 10px; /* User strict directive: exactly 10px padding */
      box-shadow: var(--card-shadow);
    }

    .auth-card-inner {
      padding: 18px 20px;
    }

    .auth-tabs {
      display: flex;
      background: var(--bg-surface-alt);
      padding: 4px;
      border-radius: 12px;
      border: 1px solid var(--border-color);
      margin-bottom: 20px;
    }

    .tab-btn {
      flex: 1;
      text-align: center;
      padding: 8px 12px;
      border-radius: 8px;
      font-size: 13.5px;
      font-weight: 700;
      cursor: pointer;
      background: transparent;
      border: none;
      color: var(--text-secondary);
      transition: all 0.15s ease;
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

    .form-group {
      margin-bottom: 16px;
    }

    .form-label {
      display: block;
      font-size: 12.5px;
      font-weight: 600;
      color: var(--text-primary);
      margin-bottom: 6px;
    }

    .form-input {
      width: 100%;
      padding: 11px 14px;
      border-radius: 8px;
      border: 1px solid var(--border-color);
      background: var(--bg-surface-alt);
      color: var(--text-primary);
      font-size: 13.5px;
      font-family: inherit;
      outline: none;
      transition: all 0.15s ease;
    }

    .form-input:focus {
      border-color: var(--accent-emerald);
      background: var(--bg-surface);
      box-shadow: 0 0 0 2px rgba(0, 210, 106, 0.2);
    }

    .form-grid-2 {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }

    .btn-submit {
      width: 100%;
      padding: 12px;
      border-radius: 8px;
      background: #1F3224;
      color: #FFFFFF;
      border: none;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.15s ease;
      margin-top: 6px;
    }

    .btn-submit:hover {
      background: #2D4834;
      transform: translateY(-1px);
    }

    [data-theme="dark"] .btn-submit {
      background: var(--accent-emerald);
      color: #000000;
    }

    .status-alert {
      padding: 10px 14px;
      border-radius: 8px;
      font-size: 12.5px;
      font-weight: 600;
      margin-bottom: 16px;
      display: none;
    }

    .status-alert.error {
      background: #FEE2E2;
      color: #991B1B;
      border: 1px solid #F87171;
    }

    [data-theme="dark"] .status-alert.error {
      background: #3B1212;
      color: #FCA5A5;
      border-color: #7F1D1D;
    }

    .status-alert.success {
      background: #DCFCE7;
      color: #166534;
      border: 1px solid #86EFAC;
    }

    .auth-note {
      text-align: center;
      font-size: 12px;
      color: var(--text-secondary);
      margin-top: 16px;
    }

    .auth-footer {
      text-align: center;
      margin-top: 24px;
      font-size: 12px;
      color: var(--text-secondary);
    }
  </style>
</head>
<body>

  <div class="auth-box">
    
    <div class="auth-brand-head">
      <a href="index.html" class="auth-brand-logo" title="Oryx Fund">
        <img src="assets/images/oryx_logo_light.png" alt="Oryx Fund" class="oryx-auth-logo oryx-logo-light-img">
        <img src="assets/images/oryx_logo_dark.png" alt="Oryx Fund" class="oryx-auth-logo oryx-logo-dark-img">
      </a>
      <p style="font-size: 13px; color: var(--text-secondary); margin-top: 6px;">Borrower Self-Service &amp; Digital Credit Portal</p>
    </div>

    <!-- Parent Card with strict 10px padding -->
    <div class="auth-card">
      <div class="auth-card-inner">
        
        <div class="auth-tabs">
          <button type="button" class="tab-btn active" id="tabLogin" onclick="switchAuthTab('login')">🔑 Sign In</button>
          <button type="button" class="tab-btn" id="tabRegister" onclick="switchAuthTab('register')">✨ Create Account</button>
        </div>

        <div id="statusAlert" class="status-alert"></div>

        <!-- 1. SIGN IN FORM -->
        <form id="signInForm" onsubmit="handleSignIn(event)">
          <div class="form-group">
            <label class="form-label" for="loginIdentifier">Email or Mobile Number</label>
            <input type="text" id="loginIdentifier" class="form-input" placeholder="e.g. reezyhoops@gmail.com or 0712345678" required autofocus>
          </div>

          <div class="form-group">
            <div style="display: flex; justify-content: space-between;">
              <label class="form-label" for="loginPass">Password</label>
              <a href="javascript:void(0)" onclick="alert('Password reset OTP sent to registered phone/email.')" style="font-size: 11px; color: var(--accent-green); text-decoration: none; font-weight: 700;">Forgot Password?</a>
            </div>
            <input type="password" id="loginPass" class="form-input" placeholder="••••••••" required>
          </div>

          <button type="submit" class="btn-submit" id="signInSubmitBtn">
            Sign In to My Portal
          </button>

          <p class="auth-note">
            New to Oryx Fund? <a href="javascript:void(0)" onclick="switchAuthTab('register')" style="color: var(--accent-green); font-weight: 700; text-decoration: none;">Create a fresh account</a> to apply in minutes.
          </p>
        </form>

        <!-- 2. REGISTER FRESH ACCOUNT FORM -->
        <form id="registerForm" onsubmit="handleRegister(event)" style="display: none;">
          <div class="form-group">
            <label class="form-label" for="regFullName">Full Legal Name (as on National ID)</label>
            <input type="text" id="regFullName" class="form-input" placeholder="e.g. James Mwangi Kariuki" required>
          </div>

          <div class="form-grid-2">
            <div class="form-group">
              <label class="form-label" for="regEmail">Email Address</label>
              <input type="email" id="regEmail" class="form-input" placeholder="james@example.com" required>
            </div>
            <div class="form-group">
              <label class="form-label" for="regPhone">Mobile Phone (M-Pesa)</label>
              <input type="tel" id="regPhone" class="form-input" placeholder="0712345678" required>
            </div>
          </div>

          <div class="form-group">
            <label class="form-label" for="regNationalId">National ID Number</label>
            <input type="text" id="regNationalId" class="form-input" placeholder="e.g. 32847592" required>
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
            <input type="checkbox" id="termsCheck" required checked style="margin-top: 2px;">
            <label for="termsCheck">I agree to Oryx Fund Digital Lending Terms &amp; KYC Verification.</label>
          </div>

          <button type="submit" class="btn-submit" id="regSubmitBtn">
            ✨ Create Secure Account &amp; Continue ➔
          </button>

          <p class="auth-note">
            Already registered? <a href="javascript:void(0)" onclick="switchAuthTab('login')" style="color: var(--accent-green); font-weight: 700; text-decoration: none;">Sign In here</a>.
          </p>
        </form>

      </div>
    </div>

    <div class="auth-footer">
      <p>© 2026 Oryx Fund. All Rights Reserved. &bull; <button onclick="toggleTheme()" style="background:none; border:none; color:var(--text-secondary); cursor:pointer; font-weight:700;">Toggle ☀️ / 🌙 Theme</button> &bull; <a href="admin.html" style="color:var(--text-secondary); text-decoration:none; font-size:11.5px; font-weight:600;">Staff Desk 🔒</a></p>
    </div>

  </div>

  <script>
""" + auth_core_script + """

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

    async function handleRegister(e) {
      e.preventDefault();
      const name = document.getElementById('regFullName').value.trim();
      const email = document.getElementById('regEmail').value.trim().toLowerCase();
      const phone = document.getElementById('regPhone').value.trim().replace(/\\s+/g, '');
      const nationalId = document.getElementById('regNationalId').value.trim();
      const pass = document.getElementById('regPass').value;
      const passConfirm = document.getElementById('regPassConfirm').value;

      if (pass.length < 6) {
        showAlert('Password must be at least 6 characters.');
        return;
      }
      if (pass !== passConfirm) {
        showAlert('Passwords do not match. Please re-enter.');
        return;
      }

      // Check if user already exists in index
      const existingByEmail = localStorage.getItem('oryx_idx_' + email);
      const existingByPhone = localStorage.getItem('oryx_idx_' + phone);
      if (existingByEmail || existingByPhone) {
        showAlert('An account with this email or phone number already exists. Please Sign In.');
        return;
      }

      document.getElementById('regSubmitBtn').innerText = 'Creating account...';

      // Hash password securely with Web Crypto SHA-256
      const hashed = await hashPassword(pass);

      const userId = 'usr_' + Date.now();
      const newBorrower = {
        id: userId,
        name: name,
        email: email,
        phone: phone,
        nationalId: nationalId,
        kraPin: 'A00' + Math.floor(1000000 + Math.random() * 9000000) + 'Z',
        address: 'Nairobi CBD',
        county: 'Nairobi',
        role: 'Borrower',
        passwordHash: hashed,
        created_at: new Date().toISOString()
      };

      saveUserRecord(newBorrower);
      setAuthSession(newBorrower);

      showAlert('✨ Account registered successfully! Redirecting...', false);

      const urlParams = new URLSearchParams(window.location.search);
      const redirectTo = urlParams.get('redirect_to') || 'index.html';

      setTimeout(() => {
        window.location.href = redirectTo;
      }, 700);
    }

    async function handleSignIn(e) {
      e.preventDefault();
      const ident = document.getElementById('loginIdentifier').value.trim().toLowerCase().replace(/\\s+/g, '');
      const pass = document.getElementById('loginPass').value;

      document.getElementById('signInSubmitBtn').innerText = 'Verifying credentials...';

      // 1. Check Administrator Sign In
      if (ident === 'admin' || ident === 'admin@oryxfund.co.ke' || ident === 'staff@oryxfund.co.ke') {
        const hashed = await hashPassword(pass);
        // Valid admin passwords: password or Admin@2026! or oryx2026
        const validAdminHashes = [
          await hashPassword('Admin@2026!'),
          await hashPassword('password'),
          await hashPassword('oryx2026'),
          await hashPassword('admin')
        ];

        if (!validAdminHashes.includes(hashed)) {
          document.getElementById('signInSubmitBtn').innerText = 'Sign In to My Portal';
          showAlert('⛔ Invalid administrator password. Please check your credentials.');
          return;
        }

        const adminUser = {
          id: 'usr_admin_001',
          name: 'Oryx Fund Admin',
          email: 'admin@oryxfund.co.ke',
          role: 'Admin'
        };
        setAuthSession(adminUser);
        showAlert('🔒 Administrator session verified. Redirecting to Institutional Desk...', false);
        setTimeout(() => {
          window.location.href = 'admin.html';
        }, 600);
        return;
      }

      // 2. Check Registered Borrower by Email or Phone
      let userId = localStorage.getItem('oryx_idx_' + ident);
      if (!userId) {
        // Fallback check legacy storage
        const legacy = localStorage.getItem('oryx_borrower_' + ident);
        if (legacy) {
          try {
            const parsed = JSON.parse(legacy);
            userId = parsed.id || 'usr_' + Date.now();
            parsed.id = userId;
            parsed.passwordHash = await hashPassword(pass);
            saveUserRecord(parsed);
          } catch(err) {}
        }
      }

      if (!userId) {
        document.getElementById('signInSubmitBtn').innerText = 'Sign In to My Portal';
        showAlert('No borrower account found matching this identifier. Please create an account.');
        return;
      }

      const user = getUserRecord(userId);
      if (!user) {
        document.getElementById('signInSubmitBtn').innerText = 'Sign In to My Portal';
        showAlert('Account profile could not be loaded. Please re-register.');
        return;
      }

      // Verify Password Hash
      const enteredHash = await hashPassword(pass);
      if (user.passwordHash && user.passwordHash !== enteredHash) {
        document.getElementById('signInSubmitBtn').innerText = 'Sign In to My Portal';
        showAlert('Incorrect password. Please verify and try again.');
        return;
      }

      // If user had no password hash (legacy migration), set it now
      if (!user.passwordHash) {
        user.passwordHash = enteredHash;
        saveUserRecord(user);
      }

      user.role = 'Borrower';
      setAuthSession(user);
      showAlert('✨ Authentication successful! Redirecting...', false);

      const urlParams = new URLSearchParams(window.location.search);
      const redirectTo = urlParams.get('redirect_to') || 'index.html';

      setTimeout(() => {
        window.location.href = redirectTo;
      }, 600);
    }

    function toggleTheme() {
      const html = document.documentElement;
      const cur = html.getAttribute('data-theme') || 'light';
      const next = cur === 'light' ? 'dark' : 'light';
      html.setAttribute('data-theme', next);
      html.classList.toggle('dark', next === 'dark');
      localStorage.setItem('oryx_theme', next);
    }
    const saved = localStorage.getItem('oryx_theme');
    if (saved) {
      document.documentElement.setAttribute('data-theme', saved);
      document.documentElement.classList.toggle('dark', saved === 'dark');
    }
  </script>
</body>
</html>
"""

    # Write files
    files_to_write = {
        "index.html": portal_html,
        "my_loans.html": portal_html,
        "borrower.html": portal_html,
        "apply.html": apply_html,
        "my_account.html": account_html,
        "login.html": login_html
    }

    for filename, content in files_to_write.items():
        path = os.path.join(base_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully generated {filename} ({len(content)} bytes)")

if __name__ == "__main__":
    generate_all()

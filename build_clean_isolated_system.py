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
            <span>Reezy</span>
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
          <span>Reezy</span>
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

    # 2. BORROWER DASHBOARD HTML (index.html, my_loans.html, borrower.html)
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
        <span class="user-greeting" id="heroAccountText">Account: reezyhoops@gmail.com</span>
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
          <p class="section-desc">Track status and review records of all submitted loan applications.</p>
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
      try {
        const authUser = JSON.parse(localStorage.getItem('oryx_auth_user'));
        if (authUser && authUser.email) {
          document.getElementById('heroAccountText').innerText = 'Account: ' + authUser.email;
          const uName = authUser.name || authUser.email.split('@')[0];
          document.querySelectorAll('#navUserPill span, #navUserPillMobile span').forEach(el => el.innerText = uName);
        }

        // Render submitted applications from localStorage
        const apps = JSON.parse(localStorage.getItem('oryx_applications') || '[]');
        if (apps.length > 0) {
          document.getElementById('appsEmptyState').style.display = 'none';
          const listEl = document.getElementById('appsListContainer');
          listEl.style.display = 'block';
          listEl.innerHTML = '';

          apps.forEach(app => {
            const card = document.createElement('div');
            card.className = 'app-item-card';
            card.innerHTML = `
              <div class="app-item-info">
                <div class="app-item-id">${app.id || 'ACC-LOAP-2026-001'}</div>
                <div class="app-item-prod">${app.productName || 'Working Capital Loan'}</div>
                <div class="app-item-meta">Applicant: ${app.fullName || 'Reezy'} &bull; ${app.date || 'Today'} &bull; ${app.term || '6'} Months</div>
              </div>
              <div class="app-item-right">
                <div class="app-item-amt">KES ${Number(app.amount || 250000).toLocaleString('en-US', {minimumFractionDigits: 2})}</div>
                <span class="app-item-badge badge-review">⚡ Under Review</span>
              </div>
            `;
            listEl.appendChild(card);
          });
        }
      } catch(e) {
        console.error(e);
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
              <input type="text" id="app_fullname" class="form-control" placeholder="e.g. James Mwangi Kariuki" value="James Mwangi Kariuki">
            </div>
            <div class="form-group">
              <label class="form-label">National ID / Passport Number <span class="req">*</span></label>
              <input type="text" id="app_national_id" class="form-control" placeholder="e.g. 12345678" value="32847592">
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
              <input type="tel" id="app_phone" class="form-control" placeholder="e.g. 0712345678" value="0712345678">
            </div>
            <div class="form-group">
              <label class="form-label">Email Address</label>
              <input type="email" id="app_email" class="form-control" placeholder="e.g. james@example.com" value="reezyhoops@gmail.com">
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
            <input type="range" id="amountSlider" min="10000" max="2500000" step="10000" value="2500000" oninput="updateCalculator()" style="width:100%; cursor:pointer; accent-color:var(--accent-emerald);">

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
                <div style="font-weight:700; color:var(--text-color);" id="revName">James Mwangi Kariuki</div>
              </div>
              <div>
                <span class="stat-label">National ID / Phone</span>
                <div style="font-weight:700; color:var(--text-color);" id="revIdPhone">32847592 &bull; 0712345678</div>
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
      const name = document.getElementById('app_fullname').value;
      const amt = parseInt(document.getElementById('amountSlider').value);
      const term = parseInt(document.getElementById('termSlider').value);
      const randomCode = 'ACC-LOAP-2026-' + Math.floor(10000 + Math.random() * 90000);

      const appData = {
        id: randomCode,
        fullName: name,
        productName: selectedFacility,
        amount: amt,
        term: term,
        date: new Date().toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }),
        status: 'Under Review'
      };

      const existingApps = JSON.parse(localStorage.getItem('oryx_applications') || '[]');
      existingApps.unshift(appData);
      localStorage.setItem('oryx_applications', JSON.stringify(existingApps));

      document.getElementById('formCardWrapper').style.display = 'none';
      document.getElementById('successRefCode').innerText = randomCode;
      document.getElementById('successScreen').style.display = 'block';
    }

    document.addEventListener('DOMContentLoaded', () => {
      updateCalculator();
    });
  </script>
</body>
</html>
"""

    # 4. MY ACCOUNT HTML (my_account.html)
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
        <span class="user-greeting" id="heroAccountText">Account: reezyhoops@gmail.com</span>
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
            <input type="text" class="form-control" value="James Mwangi Kariuki" readonly style="opacity:0.85;">
          </div>
          <div class="form-group">
            <label class="form-label">National ID Number</label>
            <input type="text" class="form-control" value="32847592" readonly style="opacity:0.85;">
          </div>
        </div>

        <div class="form-grid-2">
          <div class="form-group">
            <label class="form-label">KRA PIN</label>
            <input type="text" class="form-control" value="A009847291Z" readonly style="opacity:0.85;">
          </div>
          <div class="form-group">
            <label class="form-label">Primary Mobile</label>
            <input type="text" class="form-control" value="0712345678">
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">Email Address</label>
          <input type="email" class="form-control" id="accEmail" value="reezyhoops@gmail.com">
        </div>

        <div class="form-grid-2">
          <div class="form-group">
            <label class="form-label">Residential Address</label>
            <input type="text" class="form-control" value="Kilimani, Ring Road">
          </div>
          <div class="form-group">
            <label class="form-label">County</label>
            <input type="text" class="form-control" value="Nairobi">
          </div>
        </div>

        <div style="margin-top:16px;">
          <button type="button" class="oryx-btn oryx-btn-primary" onclick="alert('Profile details updated successfully!')">Save Profile Updates</button>
        </div>
      </div>

      <!-- Security & Session Card -->
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
      localStorage.removeItem('oryx_auth_user');
      window.location.href = 'login.html';
    }

    document.addEventListener('DOMContentLoaded', () => {
      try {
        const authUser = JSON.parse(localStorage.getItem('oryx_auth_user'));
        if (authUser && authUser.email) {
          document.getElementById('heroAccountText').innerText = 'Account: ' + authUser.email;
          document.getElementById('accEmail').value = authUser.email;
          const uName = authUser.name || authUser.email.split('@')[0];
          document.querySelectorAll('#navUserPill span, #navUserPillMobile span').forEach(el => el.innerText = uName);
        }
      } catch(e) {}
    });
  </script>
</body>
</html>
"""

    # Write all files
    files_to_write = {
        "index.html": portal_html,
        "my_loans.html": portal_html,
        "borrower.html": portal_html,
        "apply.html": apply_html,
        "my_account.html": account_html
    }

    for filename, content in files_to_write.items():
        path = os.path.join(base_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully generated {filename} ({len(content)} bytes)")

if __name__ == "__main__":
    generate_all()

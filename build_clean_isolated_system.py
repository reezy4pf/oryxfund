import os
import json

base_dir = "/home/reezy/.gemini/antigravity-ide/scratch/oryx_fund"

def generate_all():
    # 1. Master CSS Stylesheet with Design Tokens, Modals, Sliders, DTI Meter, & Micro-Animations
    css_content = """/* ==========================================================================
   ORYX FUND DIGITAL LENDING PLATFORM — BESPOKE CINEMATIC STYLES
   ========================================================================== */
:root, [data-theme="light"], [data-theme-mode="light"] {
  --bg-body: #EAE0D8;
  --bg-card: #FFFFFF;
  --bg-surface: #F5EFEA;
  --bg-surface-elevated: #FFFFFF;
  --text-color: #121A14;
  --text-muted: #556B5D;
  --text-dim: #7E9284;
  --border-color: #D8CCC1;
  --border-light: #ECE5DC;
  --primary-color: #1F3224;
  --primary-hover: #16251A;
  --accent-green: #059669;
  --accent-emerald: #00D26A;
  --accent-gold: #C1440E;
  --accent-amber: #D97706;
  --accent-red: #DC2626;
  --hero-bg: #1F3224;
  --hero-text: #FAF8F5;
  --card-shadow: 0 4px 24px rgba(31, 50, 36, 0.07);
  --modal-backdrop: rgba(18, 26, 20, 0.65);
  --font-body: -apple-system, BlinkMacSystemFont, "DM Sans", "Segoe UI", Roboto, sans-serif;
  --font-mono: 'IBM Plex Mono', SFMono-Regular, Menlo, Monaco, Consolas, monospace;
}

[data-theme="dark"], html.dark, body.dark, [data-theme-mode="dark"] {
  --bg-body: #09090B;
  --bg-card: #121215;
  --bg-surface: #18181C;
  --bg-surface-elevated: #202025;
  --text-color: #FAF8F5;
  --text-muted: #A1A1AA;
  --text-dim: #71717A;
  --border-color: #27272A;
  --border-light: #1E1E22;
  --primary-color: #00D26A;
  --primary-hover: #05E575;
  --accent-green: #00D26A;
  --accent-emerald: #00D26A;
  --accent-gold: #F59E0B;
  --accent-amber: #F59E0B;
  --accent-red: #EF4444;
  --hero-bg: #121215;
  --hero-text: #FAF8F5;
  --card-shadow: 0 12px 32px -5px rgba(0, 0, 0, 0.7);
  --modal-backdrop: rgba(0, 0, 0, 0.85);
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
  overflow-x: hidden;
}

/* CLEAN BESPOKE STYLING */

/* FULL-WIDTH STICKY NAVBAR */
.oryx-navbar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(234, 224, 216, 0.94);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--border-color);
  padding: 10px 24px;
  width: 100%;
  box-sizing: border-box;
}

[data-theme="dark"] .oryx-navbar,
html.dark .oryx-navbar {
  background: rgba(9, 9, 11, 0.94);
  border-bottom-color: var(--border-color);
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
  background: rgba(31, 50, 36, 0.05);
  padding: 4px;
  border-radius: 9999px;
  border: 1px solid var(--border-color);
}

[data-theme="dark"] .oryx-capsules-nav,
html.dark .oryx-capsules-nav {
  background: var(--bg-surface);
  border-color: var(--border-color);
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
  background: rgba(31, 50, 36, 0.07);
}

[data-theme="dark"] .oryx-capsule-tab:hover:not(.active),
html.dark .oryx-capsule-tab:hover:not(.active) {
  background: rgba(255, 255, 255, 0.08);
}

.oryx-capsule-tab.active {
  background: #1F3224 !important;
  color: #FFFFFF !important;
  font-weight: 700;
  box-shadow: 0 2px 8px rgba(31, 50, 36, 0.25);
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
  border-color: var(--border-color);
  color: #FAF8F5;
}

.oryx-theme-toggle-btn:hover {
  border-color: var(--primary-color);
  transform: translateY(-1px);
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

/* HERO CARD (EXACT LOCALHOST 1:1) */
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
  background: var(--hero-bg);
  border: 1px solid var(--border-color);
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
  background: #00D26A !important;
  color: #000000 !important;
  font-weight: 800 !important;
}
[data-theme="dark"] .oryx-hero-btn:hover {
  background: #05E575 !important;
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
  transition: transform 0.2s cubic-bezier(0.25, 0.46, 0.45, 0.94), box-shadow 0.2s ease;
}

.oryx-stat-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
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
  transition: all 0.18s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  text-decoration: none;
}

.oryx-btn:hover {
  transform: scale(1.02);
}

.oryx-btn-primary {
  background: #1F3224 !important;
  color: #FFFFFF !important;
  box-shadow: 0 2px 8px rgba(31, 50, 36, 0.15);
}

.oryx-btn-primary:hover {
  background: #2D4834 !important;
}

[data-theme="dark"] .oryx-btn-primary {
  background: #00D26A !important;
  border: none !important;
  color: #000000 !important;
  font-weight: 800 !important;
}

[data-theme="dark"] .oryx-btn-primary:hover {
  background: #05E575 !important;
}

.oryx-btn-secondary {
  background: var(--bg-surface) !important;
  color: var(--text-color) !important;
  border: 1px solid var(--border-color) !important;
}

.oryx-btn-secondary:hover {
  background: var(--border-light) !important;
}

.oryx-btn-mpesa {
  background: linear-gradient(135deg, #00D26A 0%, #059669 100%) !important;
  color: #000000 !important;
  font-weight: 800 !important;
  box-shadow: 0 4px 14px rgba(0, 210, 106, 0.35) !important;
}

.oryx-btn-mpesa:hover {
  background: linear-gradient(135deg, #00FF80 0%, #00D26A 100%) !important;
  box-shadow: 0 6px 18px rgba(0, 210, 106, 0.45) !important;
}

.oryx-btn-express {
  background: linear-gradient(135deg, #00D26A 0%, #059669 100%) !important;
  color: #000000 !important;
  font-weight: 800 !important;
  box-shadow: 0 4px 14px rgba(0, 210, 106, 0.35) !important;
}

.oryx-btn-express:hover {
  background: linear-gradient(135deg, #00FF80 0%, #00D26A 100%) !important;
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
  box-shadow: 0 0 0 2px rgba(31, 50, 36, 0.12);
}

[data-theme="dark"] .form-control:focus,
[data-theme="dark"] .oryx-input:focus,
[data-theme="dark"] .oryx-select:focus {
  box-shadow: 0 0 0 2px rgba(0, 210, 106, 0.25);
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
  transform: translateY(-2px);
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

/* DTI METER */
.dti-meter-wrapper {
  background: var(--bg-surface);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 16px 20px;
  margin-top: 14px;
}

.dti-bar-track {
  height: 8px;
  background: rgba(0,0,0,0.1);
  border-radius: 4px;
  position: relative;
  overflow: hidden;
  margin: 10px 0;
}

[data-theme="dark"] .dti-bar-track {
  background: rgba(255,255,255,0.1);
}

.dti-bar-fill {
  height: 100%;
  width: 32%;
  background: linear-gradient(90deg, #00D26A 0%, #D97706 70%, #EF4444 100%);
  border-radius: 4px;
  transition: width 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

/* DROPZONE STYLES */
.oryx-dropzone {
  border: 2px dashed var(--border-color);
  background: var(--bg-surface);
  border-radius: 12px;
  padding: 24px 20px;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s ease;
  position: relative;
}

.oryx-dropzone:hover, .oryx-dropzone.dragover {
  border-color: var(--accent-emerald);
  background: rgba(0, 210, 106, 0.04);
}

.dropzone-icon {
  font-size: 28px;
  margin-bottom: 8px;
}

.uploaded-file-chip {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(0, 210, 106, 0.15);
  border: 1px solid #00D26A;
  color: var(--text-color);
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  margin-top: 10px;
}

/* MODAL SYSTEM (REPLACING PROMPT/ALERT) */
.oryx-modal-backdrop {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: var(--modal-backdrop);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  padding: 20px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.22s ease;
}

.oryx-modal-backdrop.active {
  opacity: 1;
  pointer-events: auto;
}

.oryx-modal-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 18px;
  padding: 32px 28px;
  max-width: 480px;
  width: 100%;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
  transform: scale(0.95);
  transition: transform 0.22s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
}

.oryx-modal-backdrop.active .oryx-modal-card {
  transform: scale(1);
}

.modal-close-btn {
  position: absolute;
  top: 18px; right: 20px;
  background: transparent;
  border: none;
  font-size: 18px;
  color: var(--text-muted);
  cursor: pointer;
}

.modal-close-btn:hover { color: var(--text-color); }

/* AMORTIZATION TABLE ACCORDION */
.amort-table-wrap {
  margin-top: 20px;
  border: 1px solid var(--border-color);
  border-radius: 12px;
  overflow: hidden;
}

.amort-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12.5px;
}

.amort-table th {
  background: var(--bg-surface);
  color: var(--text-muted);
  font-weight: 700;
  text-align: left;
  padding: 10px 14px;
  border-bottom: 1px solid var(--border-color);
  font-family: var(--font-mono);
  font-size: 11px;
}

.amort-table td {
  padding: 10px 14px;
  border-bottom: 1px solid var(--border-light);
  color: var(--text-color);
  font-family: var(--font-mono);
}

.amort-table tr:last-child td {
  border-bottom: none;
}

/* LOAN PROGRESS PIPELINE */
.pipeline-track {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 16px 0 8px;
}

.pipeline-node {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  font-size: 11px;
  font-weight: 700;
}

.pipeline-dot {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--bg-surface);
  border: 1.5px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 10px;
}

.pipeline-node.done .pipeline-dot {
  background: #00D26A;
  color: #000;
  border-color: #00D26A;
}

.pipeline-node.current .pipeline-dot {
  background: #D97706;
  color: #FFF;
  border-color: #D97706;
  box-shadow: 0 0 0 3px rgba(217, 119, 6, 0.25);
  animation: pulseNode 1.5s infinite;
}

@keyframes pulseNode {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.15); }
}

.pipeline-line {
  flex: 1;
  height: 2px;
  background: var(--border-color);
  margin: 0 6px 16px;
}

.pipeline-line.done {
  background: #00D26A;
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

/* PASSWORD STRENGTH */
.pass-strength-bar {
  display: flex;
  gap: 4px;
  height: 4px;
  margin-top: 6px;
}

.strength-segment {
  flex: 1;
  background: var(--border-color);
  border-radius: 2px;
  transition: background-color 0.2s ease;
}

.strength-segment.active-weak { background: #EF4444; }
.strength-segment.active-fair { background: #F59E0B; }
.strength-segment.active-good { background: #10B981; }
.strength-segment.active-strong { background: #00D26A; }
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
      if (localStorage.getItem('oryx_auth_seeded') !== 'v4') {
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

        // Seed initial default active loan for Reezy to enable interactive repayment demo
        const seedReezyLoan = {
          loanId: 'ACC-LOAN-2026-00001',
          productName: 'Working Capital Facility',
          principal: 250000,
          disbursedDate: '2026-08-15',
          termMonths: 12,
          monthlyRate: 1.5,
          monthlyInstallment: 23750,
          balance: 213750,
          nextDueDate: '2026-09-15',
          repayments: [
            { id: 'REP-2026-0001', date: '2026-08-20', amount: 23750, ref: 'QK91827364', method: 'M-Pesa STK Push' }
          ]
        };
        localStorage.setItem('oryx_active_loan_usr_reezy_001', JSON.stringify(seedReezyLoan));

        localStorage.setItem('oryx_auth_seeded', 'v4');
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

    function getUserActiveLoan(userId) {
      try {
        return JSON.parse(localStorage.getItem('oryx_active_loan_' + userId));
      } catch(e) { return null; }
    }

    function saveUserActiveLoan(userId, loanData) {
      localStorage.setItem('oryx_active_loan_' + userId, JSON.stringify(loanData));
    }
    """

    # 2. MASTER BORROWER PORTAL (index.html, my_loans.html, borrower.html)
    portal_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Loans — Oryx Fund</title>
  <meta name="description" content="View active loans, amortizations, submit repayments via M-Pesa STK Push, and track applications.">
  <link rel="icon" type="image/png" href="assets/images/oryx-mark-dark.png">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
""" + css_content + """
  </style>
</head>
<body >

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
          <p class="oryx-subtitle">View your active facilities, schedule amortizations, and make instant M-Pesa Paybill repayments.</p>
        </div>
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
          <button type="button" class="oryx-hero-btn" onclick="openMpesaModal()" style="background:#00D26A !important; color:#000 !important; cursor:pointer;">
            <span>💚 Make Repayment</span>
          </button>
          <a href="apply.html" class="oryx-hero-btn">+ Apply for Loan</a>
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

    <!-- Active Facility Details Card -->
    <div class="oryx-portal-card" id="activeLoanSection">
      <div class="card-section-head">
        <div>
          <h3 class="section-title">Active Facility Overview</h3>
          <p class="section-desc">Real-time facility balance, next due date, and M-Pesa STK Push clearing.</p>
        </div>
        <div style="display: flex; gap: 8px;">
          <button type="button" class="oryx-btn oryx-btn-secondary" style="font-size:12px; padding:6px 14px;" onclick="printStatement()">
            📄 Download Statement
          </button>
          <button type="button" class="oryx-btn oryx-btn-mpesa" style="font-size:12px; padding:6px 14px;" onclick="openMpesaModal()">
            ⚡ Pay via M-Pesa
          </button>
        </div>
      </div>

      <div id="activeLoanCardContent">
        <!-- Injected dynamically -->
      </div>
    </div>

    <!-- Application History & Real-Time Pipeline Tracker -->
    <div class="oryx-portal-card">
      <div class="card-section-head">
        <div>
          <h3 class="section-title">Application Status Pipeline</h3>
          <p class="section-desc">Track status updates and review records of your submitted loan applications.</p>
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
        <h4 class="empty-title">No Pending Applications</h4>
        <p class="empty-desc">Your submitted applications will appear here with real-time status tracking.</p>
        <a href="apply.html" class="oryx-btn oryx-btn-primary">+ Apply for a New Loan</a>
      </div>

      <div id="appsListContainer" style="display:none;"></div>
    </div>

  </main>

  <!-- BESPOKE IN-DOM M-PESA STK PUSH REPAYMENT MODAL -->
  <div class="oryx-modal-backdrop" id="mpesaModalBackdrop" onclick="closeMpesaModal(event)">
    <div class="oryx-modal-card" onclick="event.stopPropagation()">
      <button type="button" class="modal-close-btn" onclick="closeMpesaModalDirect()">✕</button>
      
      <!-- Stage 1: Payment Form -->
      <div id="mpesaFormStage">
        <div style="text-align: center; margin-bottom: 20px;">
          <div style="width: 56px; height: 56px; border-radius: 50%; background: rgba(0, 210, 106, 0.15); border: 1.5px solid #00D26A; color: #00D26A; display: flex; align-items: center; justify-content: center; margin: 0 auto 12px; font-size: 24px;">
            💚
          </div>
          <div class="oryx-badge" style="background:rgba(0,210,106,0.15); color:#00D26A; border-color:#00D26A; margin-bottom:6px;">LIPA NA M-PESA ONLINE</div>
          <h3 style="font-size: 19px; font-weight: 700; color: var(--text-color);">Direct M-Pesa Repayment</h3>
          <p style="font-size: 12.5px; color: var(--text-muted); margin-top: 4px;">Paybill: <strong>522522</strong> &bull; Acc: <strong id="mpesaModalAccRef">ACC-LOAN-001</strong></p>
        </div>

        <form onsubmit="handleTriggerMpesaStk(event)">
          <div class="form-group">
            <label class="form-label">M-Pesa Registered Phone Number</label>
            <input type="tel" id="mpesaPhoneInput" class="form-control" placeholder="0712345678" required style="font-family:var(--font-mono); font-size:15px; font-weight:600;">
          </div>

          <div class="form-group">
            <label class="form-label">Repayment Amount (KES)</label>
            <input type="number" id="mpesaAmountInput" class="form-control" placeholder="23750" required min="100" style="font-family:var(--font-mono); font-size:16px; font-weight:700; color:var(--primary-color);">
          </div>

          <div style="display: flex; gap: 8px; margin-bottom: 18px;">
            <button type="button" class="oryx-btn oryx-btn-secondary" style="flex:1; font-size:11.5px; padding:6px;" onclick="setMpesaAmount(23750)">Full Installment (23.7K)</button>
            <button type="button" class="oryx-btn oryx-btn-secondary" style="flex:1; font-size:11.5px; padding:6px;" onclick="setMpesaAmount(10000)">Partial (10K)</button>
            <button type="button" class="oryx-btn oryx-btn-secondary" style="flex:1; font-size:11.5px; padding:6px;" onclick="setMpesaAmount(5000)">Partial (5K)</button>
          </div>

          <button type="submit" class="oryx-btn oryx-btn-mpesa" style="width: 100%; padding: 12px;" id="mpesaTriggerBtn">
            <span>⚡ Send STK Push to Phone</span>
          </button>
        </form>
      </div>

      <!-- Stage 2: STK Countdown & Processing Animation -->
      <div id="mpesaCountdownStage" style="display:none; text-align:center; padding: 20px 0;">
        <div style="width: 68px; height: 68px; border-radius: 50%; border: 3px solid #00D26A; border-top-color: transparent; display: inline-block; animation: spin 1s linear infinite; margin-bottom: 16px;"></div>
        <h3 style="font-size: 18px; font-weight: 700; color: var(--text-color); margin-bottom: 6px;">STK Push Sent to Handset</h3>
        <p style="font-size: 13px; color: var(--text-muted); line-height: 1.45;">Please check your phone (<strong id="mpesaTargetPhoneDisplay">0712345678</strong>) and enter your M-Pesa PIN to authorize payment.</p>
        
        <div style="font-family: var(--font-mono); font-size: 28px; font-weight: 800; color: var(--accent-emerald); margin: 16px 0;" id="stkTimerCount">15s</div>
        <p style="font-size: 11px; color: var(--text-dim);">Connecting to Safaricom Daraja M-Pesa Gateway...</p>
      </div>

      <!-- Stage 3: Instant Success Receipt -->
      <div id="mpesaSuccessStage" style="display:none; text-align:center; padding: 10px 0;">
        <div style="width: 64px; height: 64px; border-radius: 50%; background: rgba(0, 210, 106, 0.2); border: 2px solid #00D26A; color: #00D26A; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px; font-size: 28px;">
          ✓
        </div>
        <h3 style="font-size: 20px; font-weight: 700; color: var(--text-color); margin-bottom: 4px;">Payment Received!</h3>
        <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 16px;">Safaricom M-Pesa Ref: <strong id="mpesaReceiptRef" style="font-family:var(--font-mono); color:var(--primary-color);">QK98210492</strong></p>

        <div style="background:var(--bg-surface); border:1px dashed var(--border-color); border-radius:12px; padding:14px 18px; text-align:left; margin-bottom:20px; font-size:12.5px;">
          <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
            <span style="color:var(--text-muted);">Amount Paid:</span>
            <strong id="mpesaSuccessAmount" style="font-family:var(--font-mono); color:var(--accent-green);">KES 23,750.00</strong>
          </div>
          <div style="display:flex; justify-content:space-between; margin-bottom:6px;">
            <span style="color:var(--text-muted);">New Loan Balance:</span>
            <strong id="mpesaSuccessNewBal" style="font-family:var(--font-mono); color:var(--text-color);">KES 190,000.00</strong>
          </div>
          <div style="display:flex; justify-content:space-between;">
            <span style="color:var(--text-muted);">Status:</span>
            <span style="color:#00D26A; font-weight:700;">Cleared &bull; Instant Ledger Updated</span>
          </div>
        </div>

        <button type="button" class="oryx-btn oryx-btn-primary" style="width:100%;" onclick="closeMpesaModalDirect()">
          Done &amp; Return to Dashboard
        </button>
      </div>

    </div>
  </div>

  <style>
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
  </style>

  <script>
""" + auth_core_script + """

    let currentSession = null;
    let currentActiveLoan = null;

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

    function renderDashboardState() {
      if (!currentSession) return;

      // 1. Identification
      document.getElementById('heroAccountText').innerText = 'Account: ' + (currentSession.email || currentSession.phone);
      const displayName = currentSession.name || (currentSession.email ? currentSession.email.split('@')[0] : 'Borrower');
      document.querySelectorAll('#navUserPill span, #navUserPillMobile span').forEach(el => el.innerText = displayName);

      // 2. Active Loan Data
      currentActiveLoan = getUserActiveLoan(currentSession.userId);
      const loanCardEl = document.getElementById('activeLoanCardContent');

      if (currentActiveLoan && currentActiveLoan.balance > 0) {
        document.getElementById('statActiveLoans').innerText = '1';
        document.getElementById('statPrincipal').innerText = 'KES ' + Number(currentActiveLoan.principal).toLocaleString('en-US', {minimumFractionDigits: 2});
        document.getElementById('statOutstanding').innerText = 'KES ' + Number(currentActiveLoan.balance).toLocaleString('en-US', {minimumFractionDigits: 2});

        loanCardEl.innerHTML = `
          <div style="background:var(--bg-surface); border:1px solid var(--border-color); border-radius:12px; padding:20px; margin-bottom:16px;">
            <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap: 14px;">
              <div>
                <span class="hud-title">Facility Reference</span>
                <div style="font-family:var(--font-mono); font-weight:700; font-size:14px; color:var(--primary-color); margin-top:2px;">${currentActiveLoan.loanId}</div>
              </div>
              <div>
                <span class="hud-title">Facility Type</span>
                <div style="font-weight:700; font-size:14px; color:var(--text-color); margin-top:2px;">${currentActiveLoan.productName}</div>
              </div>
              <div>
                <span class="hud-title">Next Installment Due</span>
                <div style="font-family:var(--font-mono); font-weight:700; font-size:14px; color:var(--accent-amber); margin-top:2px;">${currentActiveLoan.nextDueDate}</div>
              </div>
              <div>
                <span class="hud-title">Installment Amount</span>
                <div style="font-family:var(--font-mono); font-weight:700; font-size:14px; color:var(--accent-green); margin-top:2px;">KES ${Number(currentActiveLoan.monthlyInstallment).toLocaleString('en-US', {minimumFractionDigits: 2})}</div>
              </div>
            </div>
          </div>

          <!-- Collapsible Repayment Schedule -->
          <div style="margin-top: 14px;">
            <button type="button" class="oryx-btn oryx-btn-secondary" style="width:100%; justify-content:space-between; font-size:12.5px; padding:8px 14px;" onclick="toggleAmortSchedule()">
              <span>📅 View 12-Month Amortization Breakdown</span>
              <span id="scheduleArrow">▼</span>
            </button>
            <div id="amortScheduleDrawer" style="display:none;" class="amort-table-wrap">
              <table class="amort-table">
                <thead>
                  <tr>
                    <th>Inst #</th>
                    <th>Due Date</th>
                    <th>Principal Component</th>
                    <th>Interest Component</th>
                    <th>Total Installment</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody id="scheduleRowsBody">
                  <tr>
                    <td>Inst 1 of 12</td>
                    <td>2026-08-15</td>
                    <td>KES 20,833.33</td>
                    <td>KES 2,916.67</td>
                    <td>KES 23,750.00</td>
                    <td><span style="color:#00D26A; font-weight:700;">Paid &check;</span></td>
                  </tr>
                  <tr>
                    <td>Inst 2 of 12</td>
                    <td>2026-09-15</td>
                    <td>KES 20,833.33</td>
                    <td>KES 2,916.67</td>
                    <td>KES 23,750.00</td>
                    <td><span style="color:#D97706; font-weight:700;">Upcoming ⏳</span></td>
                  </tr>
                  <tr>
                    <td>Inst 3 of 12</td>
                    <td>2026-10-15</td>
                    <td>KES 20,833.33</td>
                    <td>KES 2,916.67</td>
                    <td>KES 23,750.00</td>
                    <td><span style="color:var(--text-muted);">Scheduled</span></td>
                  </tr>
                  <tr>
                    <td>Inst 4 of 12</td>
                    <td>2026-11-15</td>
                    <td>KES 20,833.33</td>
                    <td>KES 2,916.67</td>
                    <td>KES 23,750.00</td>
                    <td><span style="color:var(--text-muted);">Scheduled</span></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        `;
      } else {
        document.getElementById('statActiveLoans').innerText = '0';
        document.getElementById('statPrincipal').innerText = 'KES 0.00';
        document.getElementById('statOutstanding').innerText = 'KES 0.00';

        loanCardEl.innerHTML = `
          <div class="oryx-empty-state" style="padding: 24px 10px;">
            <p style="font-size:13.5px; color:var(--text-muted); margin-bottom:12px;">You currently do not have any active loans running. Apply for a fast-track facility to receive instant disbursal.</p>
            <a href="apply.html" class="oryx-btn oryx-btn-primary">+ Apply for a New Facility</a>
          </div>
        `;
      }

      // 3. User Scoped Applications
      const userApps = getUserScopedApplications(currentSession.userId);
      if (userApps.length > 0) {
        document.getElementById('appsEmptyState').style.display = 'none';
        const listEl = document.getElementById('appsListContainer');
        listEl.style.display = 'block';
        listEl.innerHTML = '';

        userApps.forEach(app => {
          const card = document.createElement('div');
          card.className = 'app-item-card';
          card.innerHTML = `
            <div style="flex:1;">
              <div class="app-item-info">
                <div class="app-item-id">${app.id || 'ACC-LOAP-2026-001'}</div>
                <div class="app-item-prod">${app.productName || 'Working Capital Facility'}</div>
                <div class="app-item-meta">Applicant: ${app.fullName || currentSession.name} &bull; ${app.date || 'Today'} &bull; ${app.term || '6'} Months</div>
              </div>

              <!-- Animated Visual Pipeline -->
              <div class="pipeline-track">
                <div class="pipeline-node done">
                  <span class="pipeline-dot">✓</span>
                  <span>Submitted</span>
                </div>
                <div class="pipeline-line done"></div>
                <div class="pipeline-node done">
                  <span class="pipeline-dot">✓</span>
                  <span>KYC Verified</span>
                </div>
                <div class="pipeline-line done"></div>
                <div class="pipeline-node ${app.status === 'Sanctioned & Disbursed' ? 'done' : 'current'}">
                  <span class="pipeline-dot">${app.status === 'Sanctioned & Disbursed' ? '✓' : '⚡'}</span>
                  <span>${app.status === 'Sanctioned & Disbursed' ? 'Sanctioned' : 'Underwriting'}</span>
                </div>
                <div class="pipeline-line ${app.status === 'Sanctioned & Disbursed' ? 'done' : ''}"></div>
                <div class="pipeline-node ${app.status === 'Sanctioned & Disbursed' ? 'done' : ''}">
                  <span class="pipeline-dot">${app.status === 'Sanctioned & Disbursed' ? '✓' : '4'}</span>
                  <span>Disbursed</span>
                </div>
              </div>
            </div>
            
            <div class="app-item-right" style="margin-left: 20px;">
              <div class="app-item-amt">KES ${Number(app.amount || 250000).toLocaleString('en-US', {minimumFractionDigits: 2})}</div>
              <span class="app-item-badge ${app.status === 'Sanctioned & Disbursed' ? 'badge-approved' : 'badge-review'}">
                ${app.status === 'Sanctioned & Disbursed' ? '✓ Active & Disbursed' : '⚡ Under Review'}
              </span>
            </div>
          `;
          listEl.appendChild(card);
        });
      }
    }

    function toggleAmortSchedule() {
      const drawer = document.getElementById('amortScheduleDrawer');
      const arrow = document.getElementById('scheduleArrow');
      const isOpen = drawer.style.display === 'block';
      drawer.style.display = isOpen ? 'none' : 'block';
      arrow.innerText = isOpen ? '▼' : '▲';
    }

    function openMpesaModal() {
      const modal = document.getElementById('mpesaModalBackdrop');
      document.getElementById('mpesaFormStage').style.display = 'block';
      document.getElementById('mpesaCountdownStage').style.display = 'none';
      document.getElementById('mpesaSuccessStage').style.display = 'none';
      document.getElementById('mpesaPhoneInput').value = currentSession ? (currentSession.phone || '0712345678') : '0712345678';
      document.getElementById('mpesaAmountInput').value = currentActiveLoan ? currentActiveLoan.monthlyInstallment : '23750';
      modal.classList.add('active');
    }

    function setMpesaAmount(val) {
      document.getElementById('mpesaAmountInput').value = val;
    }

    function closeMpesaModal(e) {
      if (e.target.id === 'mpesaModalBackdrop') {
        closeMpesaModalDirect();
      }
    }

    function closeMpesaModalDirect() {
      document.getElementById('mpesaModalBackdrop').classList.remove('active');
    }

    function handleTriggerMpesaStk(e) {
      e.preventDefault();
      const phone = document.getElementById('mpesaPhoneInput').value.trim();
      const amt = Number(document.getElementById('mpesaAmountInput').value);

      document.getElementById('mpesaFormStage').style.display = 'none';
      document.getElementById('mpesaCountdownStage').style.display = 'block';
      document.getElementById('mpesaTargetPhoneDisplay').innerText = phone;

      let timer = 3;
      const countEl = document.getElementById('stkTimerCount');
      countEl.innerText = timer + 's';

      const interval = setInterval(() => {
        timer--;
        if (timer > 0) {
          countEl.innerText = timer + 's';
        } else {
          clearInterval(interval);
          completeMpesaPayment(amt);
        }
      }, 1000);
    }

    function completeMpesaPayment(amt) {
      document.getElementById('mpesaCountdownStage').style.display = 'none';
      document.getElementById('mpesaSuccessStage').style.display = 'block';

      const randomReceipt = 'QK' + Math.floor(10000000 + Math.random() * 90000000);
      document.getElementById('mpesaReceiptRef').innerText = randomReceipt;
      document.getElementById('mpesaSuccessAmount').innerText = 'KES ' + amt.toLocaleString('en-US', {minimumFractionDigits: 2});

      if (currentActiveLoan) {
        currentActiveLoan.balance = Math.max(0, currentActiveLoan.balance - amt);
        if (!currentActiveLoan.repayments) currentActiveLoan.repayments = [];
        currentActiveLoan.repayments.unshift({
          id: 'REP-' + Date.now(),
          date: new Date().toISOString().split('T')[0],
          amount: amt,
          ref: randomReceipt,
          method: 'M-Pesa STK Push'
        });
        saveUserActiveLoan(currentSession.userId, currentActiveLoan);
      }

      const newBal = currentActiveLoan ? currentActiveLoan.balance : 0;
      document.getElementById('mpesaSuccessNewBal').innerText = 'KES ' + Number(newBal).toLocaleString('en-US', {minimumFractionDigits: 2});

      renderDashboardState();
    }

    function printStatement() {
      window.print();
    }

    document.addEventListener('DOMContentLoaded', () => {
      currentSession = requireBorrowerAuth('index.html');
      if (!currentSession) return;
      renderDashboardState();
    });
  </script>
</body>
</html>
"""

    # 3. 4-STEP LOAN APPLICATION WIZARD WITH DROPZONES & DTI CREDIT SCORING (apply.html)
    apply_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Apply for a Loan — Oryx Fund</title>
  <meta name="description" content="Instant digital credit application portal for Oryx Fund with real-time underwriting scoring.">
  <link rel="icon" type="image/png" href="assets/images/oryx-mark-dark.png">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
""" + css_content + """
  </style>
</head>
<body >

""" + build_header("apply") + """

  <main class="oryx-portal-wrapper">

    <!-- Top Hero Card -->
    <div class="oryx-hero-card">
      <div class="hero-top-row">
        <div class="oryx-badge">LOAN APPLICATION</div>
        <span class="user-greeting" id="heroGreetingText">⚡ Instant Credit Decision</span>
      </div>
      <div class="hero-main-row">
        <div class="hero-title-box">
          <h1 class="oryx-title">Loan Application Form</h1>
          <p class="oryx-subtitle">Transparent financing for SME working capital, asset finance, and emergency bridging in Kenya.</p>
        </div>
      </div>
      
      <!-- 4-Step Indicator -->
      <div class="oryx-steps-container">
        <div class="oryx-step active" id="step-badge-1" onclick="goToStep(1)">
          <span class="step-num">1</span>
          <span class="step-label">KYC &amp; Documents</span>
        </div>
        <div class="step-divider" id="step-div-1"></div>
        <div class="oryx-step" id="step-badge-2" onclick="goToStep(2)">
          <span class="step-num">2</span>
          <span class="step-label">Facility Specs</span>
        </div>
        <div class="step-divider" id="step-div-2"></div>
        <div class="oryx-step" id="step-badge-3" onclick="goToStep(3)">
          <span class="step-num">3</span>
          <span class="step-label">Cashflow &amp; Scoring</span>
        </div>
        <div class="step-divider" id="step-div-3"></div>
        <div class="oryx-step" id="step-badge-4" onclick="goToStep(4)">
          <span class="step-num">4</span>
          <span class="step-label">Consent &amp; Submit</span>
        </div>
      </div>
    </div>

    <!-- Form Card -->
    <div class="oryx-portal-card" id="formCardWrapper">
      <form id="oryxLoanForm" onsubmit="return false;">

        <!-- STEP 1: Personal KYC & Document Dropzone -->
        <div id="step-1-content" class="wizard-step-pane">
          <div class="card-section-head">
            <div>
              <h3 class="section-title">1. Personal Identity &amp; Document Upload</h3>
              <p class="section-desc">Verify your national registration and upload supporting verification documents.</p>
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
              <label class="form-label">Primary Phone (M-Pesa Registered) <span class="req">*</span></label>
              <input type="tel" id="app_phone" class="form-control" placeholder="e.g. 0712345678">
            </div>
            <div class="form-group">
              <label class="form-label">Email Address <span class="req">*</span></label>
              <input type="email" id="app_email" class="form-control" placeholder="e.g. james@example.com">
            </div>
          </div>

          <!-- DOCUMENT UPLOAD DROPZONE -->
          <div class="card-section-head" style="margin-top:20px;">
            <div>
              <h4 style="font-size:14.5px; font-weight:700;">📂 Document Verification (National ID &amp; Statements)</h4>
              <p class="section-desc">Drag and drop your National ID card and 6-Month M-Pesa / Bank Statement PDF.</p>
            </div>
          </div>

          <div class="form-grid-2">
            <div class="oryx-dropzone" id="idDropzone" onclick="triggerFileSelect('idFileInput')">
              <input type="file" id="idFileInput" style="display:none;" onchange="handleFileSelected('idFileInput', 'idChipArea', 'National ID (Front &amp; Back)')">
              <div class="dropzone-icon">🪪</div>
              <div style="font-size:13px; font-weight:700; color:var(--text-color);">National ID (Front &amp; Back)</div>
              <div style="font-size:11.5px; color:var(--text-muted); margin-top:2px;">PDF, PNG, JPG up to 10MB</div>
              <div id="idChipArea"></div>
            </div>

            <div class="oryx-dropzone" id="stmtDropzone" onclick="triggerFileSelect('stmtFileInput')">
              <input type="file" id="stmtFileInput" style="display:none;" onchange="handleFileSelected('stmtFileInput', 'stmtChipArea', '6-Month M-Pesa Statement')">
              <div class="dropzone-icon">📊</div>
              <div style="font-size:13px; font-weight:700; color:var(--text-color);">6-Month M-Pesa / Bank Statement</div>
              <div style="font-size:11.5px; color:var(--text-muted); margin-top:2px;">PDF export from Safaricom/Bank</div>
              <div id="stmtChipArea"></div>
            </div>
          </div>

          <div style="display:flex; justify-content:flex-end; margin-top:24px;">
            <button type="button" class="oryx-btn oryx-btn-primary" onclick="goToStep(2)">Continue to Facility Specs &rarr;</button>
          </div>
        </div>

        <!-- STEP 2: Facility Specs, Calculator & Disbursal -->
        <div id="step-2-content" class="wizard-step-pane" style="display:none;">
          <div class="card-section-head">
            <div>
              <h3 class="section-title">2. Choose Facility &amp; Requested Principal</h3>
              <p class="section-desc">Select desired lending product. Real-time rates and estimates update instantly.</p>
            </div>
          </div>

          <label class="form-label" style="font-size:13.5px; margin-bottom:10px;">Select Facility Type <span class="req">*</span></label>
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
            <button type="button" class="oryx-btn oryx-btn-primary" onclick="goToStep(3)">Continue to Cashflow &amp; Scoring &rarr;</button>
          </div>
        </div>

        <!-- STEP 3: Cashflow & Live DTI Credit Scoring -->
        <div id="step-3-content" class="wizard-step-pane" style="display:none;">
          <div class="card-section-head">
            <div>
              <h3 class="section-title">3. Monthly Cashflow &amp; Real-Time Credit Score</h3>
              <p class="section-desc">Our algorithmic engine computes your Debt-to-Income (DTI) ratio live.</p>
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
              <input type="number" id="app_income" class="form-control" value="180000" oninput="updateDtiMeter()">
            </div>
          </div>

          <div class="form-grid-2">
            <div class="form-group">
              <label class="form-label">Monthly Debt Obligations (KES)</label>
              <input type="number" id="app_debt" class="form-control" value="25000" oninput="updateDtiMeter()">
            </div>
            <div class="form-group">
              <label class="form-label">Monthly Fixed Living Expenses (KES)</label>
              <input type="number" id="app_expenses" class="form-control" value="45000" oninput="updateDtiMeter()">
            </div>
          </div>

          <!-- REAL-TIME DTI & SCORING METER -->
          <div class="dti-meter-wrapper">
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <span style="font-size:12.5px; font-weight:700; color:var(--text-color);">⚡ Live Affordability Score</span>
              <span id="dtiScoreBadge" style="font-size:11px; font-weight:700; padding:3px 10px; border-radius:20px; background:#DCFCE7; color:#166534;">🟢 Prime Score (28% DTI)</span>
            </div>
            <div class="dti-bar-track">
              <div class="dti-bar-fill" id="dtiBarFill" style="width: 28%;"></div>
            </div>
            <div style="display:flex; justify-content:space-between; font-size:11px; color:var(--text-muted);">
              <span>Low Risk (&lt;35%)</span>
              <span id="dtiConfidenceText">Confidence: 96% Instant Approval</span>
              <span>High Risk (&gt;50%)</span>
            </div>
          </div>

          <div style="display:flex; justify-content:space-between; margin-top:28px;">
            <button type="button" class="oryx-btn oryx-btn-secondary" onclick="goToStep(2)">&larr; Back</button>
            <button type="button" class="oryx-btn oryx-btn-primary" onclick="goToStep(4)">Continue to Review &rarr;</button>
          </div>
        </div>

        <!-- STEP 4: Review, SMS Preview & Submit -->
        <div id="step-4-content" class="wizard-step-pane" style="display:none;">
          <div class="card-section-head">
            <div>
              <h3 class="section-title">4. Review Application &amp; Declarations</h3>
              <p class="section-desc">Verify facility specifications before final algorithmic submission.</p>
            </div>
          </div>

          <div style="background:var(--bg-surface); border:1px solid var(--border-color); border-radius:12px; padding:24px; margin-bottom:20px;">
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

          <!-- SMS NOTIFICATION PREVIEW -->
          <div style="background:rgba(0, 210, 106, 0.08); border:1px dashed #00D26A; border-radius:12px; padding:14px 18px; margin-bottom:20px;">
            <div style="display:flex; align-items:center; gap:8px; font-size:12px; font-weight:700; color:var(--text-color); margin-bottom:4px;">
              <span>💬 Live SMS Confirmation Preview</span>
            </div>
            <div style="font-family:var(--font-mono); font-size:11.5px; color:var(--text-muted);" id="smsPreviewText">
              "OryxFund: Dear Borrower, your application for KES 250,000 has been received. Priority underwriting review in progress."
            </div>
          </div>

          <div style="margin-bottom:24px;">
            <label style="display:flex; align-items:flex-start; gap:10px; cursor:pointer; font-size:13px; color:var(--text-color);">
              <input type="checkbox" id="consentCheck" checked style="margin-top:3px; accent-color:var(--accent-emerald);">
              <span>I certify all submitted information is accurate and authorize Oryx Fund Ltd to verify creditworthiness with licensed CRBs and process disbursal.</span>
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
      <div class="oryx-badge" style="background:rgba(0,210,106,0.15); border-color:#00D26A; color:#00D26A; margin-bottom:12px;">⚡ PRIORITY UNDERWRITING QUEUE</div>
      <h2 class="success-title">Loan Application Received!</h2>
      <p class="success-desc">Your application has been received and routed directly to the Institutional Underwriting Desk. You will receive an SMS alert upon approval.</p>
      
      <div class="app-ref-box">
        <span class="ref-label">Application Reference Code</span>
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

    function triggerFileSelect(id) {
      document.getElementById(id).click();
    }

    function handleFileSelected(inputId, chipAreaId, label) {
      const input = document.getElementById(inputId);
      const chipArea = document.getElementById(chipAreaId);
      if (input.files && input.files[0]) {
        const file = input.files[0];
        chipArea.innerHTML = `<span class="uploaded-file-chip">✓ ${file.name} (${(file.size / 1024).toFixed(0)} KB)</span>`;
      } else {
        chipArea.innerHTML = `<span class="uploaded-file-chip">✓ Verified ${label} (1.2 MB)</span>`;
      }
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

      if (step === 3) updateDtiMeter();
      if (step === 4) populateReview();

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

    function updateDtiMeter() {
      const income = Number(document.getElementById('app_income').value) || 1;
      const debt = Number(document.getElementById('app_debt').value) || 0;
      const expenses = Number(document.getElementById('app_expenses').value) || 0;

      const dti = Math.min(100, Math.round(((debt + expenses) / income) * 100));
      const fillEl = document.getElementById('dtiBarFill');
      const badgeEl = document.getElementById('dtiScoreBadge');
      const confEl = document.getElementById('dtiConfidenceText');

      fillEl.style.width = dti + '%';

      if (dti < 35) {
        badgeEl.className = 'app-item-badge badge-approved';
        badgeEl.innerText = '🟢 Prime Score (' + dti + '% DTI)';
        confEl.innerText = 'Confidence: 98% Instant Approval';
      } else if (dti < 50) {
        badgeEl.className = 'app-item-badge badge-review';
        badgeEl.innerText = '🟡 Standard Tier (' + dti + '% DTI)';
        confEl.innerText = 'Confidence: 85% Standard Approval';
      } else {
        badgeEl.className = 'app-item-badge';
        badgeEl.style.background = '#FEE2E2';
        badgeEl.style.color = '#991B1B';
        badgeEl.innerText = '🟠 High Leverage (' + dti + '% DTI)';
        confEl.innerText = 'Security / Guarantor Required';
      }
    }

    function populateReview() {
      const name = document.getElementById('app_fullname').value.trim() || (currentSession ? currentSession.name : 'Borrower');
      const id = document.getElementById('app_national_id').value.trim();
      const phone = document.getElementById('app_phone').value.trim();
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

      document.getElementById('smsPreviewText').innerText = `"OryxFund: Dear ${name}, your application for KES ${amt.toLocaleString()} has been received. Priority underwriting review in progress."`;
    }

    function submitApplication() {
      const name = document.getElementById('app_fullname').value.trim();
      const id = document.getElementById('app_national_id').value.trim();
      const phone = document.getElementById('app_phone').value.trim();
      const amt = parseInt(document.getElementById('amountSlider').value);
      const term = parseInt(document.getElementById('termSlider').value);
      const income = Number(document.getElementById('app_income').value) || 180000;
      const randomCode = 'ACC-LOAP-2026-' + Math.floor(10000 + Math.random() * 90000);

      const appData = {
        id: randomCode,
        fullName: name,
        nationalId: id,
        phone: phone,
        productName: selectedFacility,
        amount: amt,
        income: income,
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
      currentSession = requireBorrowerAuth('apply.html');
      if (!currentSession) return;

      const userRec = getUserRecord(currentSession.userId) || currentSession;
      if (userRec) {
        if (userRec.name) document.getElementById('app_fullname').value = userRec.name;
        if (userRec.nationalId) document.getElementById('app_national_id').value = userRec.nationalId;
        if (userRec.kraPin) document.getElementById('app_kra_pin').value = userRec.kraPin;
        if (userRec.phone) document.getElementById('app_phone').value = userRec.phone;
        if (userRec.email) document.getElementById('app_email').value = userRec.email;
      }

      const displayName = currentSession.name || (currentSession.email ? currentSession.email.split('@')[0] : 'Borrower');
      document.querySelectorAll('#navUserPill span, #navUserPillMobile span').forEach(el => el.innerText = displayName);

      updateCalculator();
    });
  </script>
</body>
</html>
"""

    # 4. MY ACCOUNT WITH PASSWORD CHANGE & 2FA SECURITY SUITE (my_account.html)
    account_html = """<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Account — Oryx Fund</title>
  <meta name="description" content="Manage borrower credentials, KYC verification status, password security, and active sessions.">
  <link rel="icon" type="image/png" href="assets/images/oryx-mark-dark.png">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
""" + css_content + """
  </style>
</head>
<body >

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
          <p class="oryx-subtitle">Manage verified personal identification, cryptographic security credentials, and active device sessions.</p>
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
            <label class="form-label">Primary Mobile Phone</label>
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

        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:20px;">
          <button type="button" class="oryx-btn oryx-btn-primary" onclick="saveProfileChanges()">Save Profile Updates</button>
          <button type="button" class="oryx-btn oryx-btn-secondary" onclick="openChangePasswordModal()">🔒 Change Password</button>
        </div>
      </div>

      <!-- Security & Session Suite -->
      <div class="oryx-portal-card">
        <div class="card-section-head">
          <div>
            <h3 class="section-title">Security &amp; Device Auth</h3>
            <p class="section-desc">Active credentials &bull; Device auth</p>
          </div>
        </div>

        <div style="margin-bottom:18px;">
          <div class="stat-label">Session Status</div>
          <div style="display:flex; align-items:center; gap:8px; margin-top:4px;">
            <span style="width:8px; height:8px; border-radius:50%; background:#00D26A; display:inline-block;"></span>
            <span style="font-weight:700; font-size:14px; color:var(--text-color);">Active &bull; Authenticated</span>
          </div>
        </div>

        <div style="margin-bottom:18px;">
          <div class="stat-label">Account Role</div>
          <div style="font-weight:700; font-size:14px; color:var(--text-color); margin-top:4px;">Registered Borrower (Standard)</div>
        </div>

        <div style="margin-bottom:18px; padding-top:14px; border-top:1px solid var(--border-light);">
          <div style="display:flex; justify-content:space-between; align-items:center;">
            <div>
              <div style="font-weight:700; font-size:13px; color:var(--text-color);">Two-Factor Auth (2FA)</div>
              <div style="font-size:11.5px; color:var(--text-muted);">SMS verification on login</div>
            </div>
            <input type="checkbox" id="twoFaToggle" onchange="toggle2Fa(this.checked)" checked style="accent-color:var(--accent-emerald); transform:scale(1.3); cursor:pointer;">
          </div>
        </div>

        <div style="border-top:1px solid var(--border-light); padding-top:20px; margin-top:20px;">
          <button type="button" class="oryx-btn" style="width:100%; background:transparent; border:1px solid #DC2626; color:#DC2626; font-weight:700; cursor:pointer;" onclick="logout()">
            Sign Out
          </button>
        </div>
      </div>

    </div>

  </main>

  <!-- CHANGE PASSWORD IN-DOM MODAL -->
  <div class="oryx-modal-backdrop" id="passModalBackdrop" onclick="closeChangePasswordModal(event)">
    <div class="oryx-modal-card" onclick="event.stopPropagation()">
      <button type="button" class="modal-close-btn" onclick="closeChangePasswordModalDirect()">✕</button>
      <h3 style="font-size:18px; font-weight:700; margin-bottom:4px;">🔒 Update Account Password</h3>
      <p style="font-size:12.5px; color:var(--text-muted); margin-bottom:18px;">Verify current password and create a new cryptographically hashed key.</p>

      <form onsubmit="handleChangePasswordSubmit(event)">
        <div class="form-group">
          <label class="form-label">Current Password</label>
          <input type="password" id="oldPassInput" class="form-control" placeholder="••••••••" required>
        </div>
        <div class="form-group">
          <label class="form-label">New Password (Min. 6 chars)</label>
          <input type="password" id="newPassInput" class="form-control" placeholder="Min. 6 characters" required minlength="6">
        </div>
        <div class="form-group">
          <label class="form-label">Confirm New Password</label>
          <input type="password" id="newPassConfirmInput" class="form-control" placeholder="Repeat new password" required minlength="6">
        </div>
        <div id="passModalAlert" class="status-alert" style="display:none; margin-bottom:14px;"></div>
        <button type="submit" class="oryx-btn oryx-btn-primary" style="width:100%; padding:11px;">Update Password Hash</button>
      </form>
    </div>
  </div>

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

    function toggle2Fa(enabled) {
      alert(enabled ? '✨ SMS Two-Factor Authentication (2FA) is now ACTIVE.' : 'Two-Factor Authentication (2FA) has been DISABLED.');
    }

    function openChangePasswordModal() {
      document.getElementById('passModalBackdrop').classList.add('active');
    }
    function closeChangePasswordModal(e) {
      if (e.target.id === 'passModalBackdrop') closeChangePasswordModalDirect();
    }
    function closeChangePasswordModalDirect() {
      document.getElementById('passModalBackdrop').classList.remove('active');
    }

    async function handleChangePasswordSubmit(e) {
      e.preventDefault();
      const oldPass = document.getElementById('oldPassInput').value;
      const newPass = document.getElementById('newPassInput').value;
      const newPassConf = document.getElementById('newPassConfirmInput').value;
      const alertEl = document.getElementById('passModalAlert');

      if (newPass !== newPassConf) {
        alertEl.className = 'status-alert error';
        alertEl.innerText = 'New passwords do not match.';
        alertEl.style.display = 'block';
        return;
      }

      const user = getUserRecord(currentSession.userId);
      const oldHash = await hashPassword(oldPass);

      if (user.passwordHash && user.passwordHash !== oldHash) {
        alertEl.className = 'status-alert error';
        alertEl.innerText = 'Incorrect current password.';
        alertEl.style.display = 'block';
        return;
      }

      user.passwordHash = await hashPassword(newPass);
      saveUserRecord(user);

      alertEl.className = 'status-alert success';
      alertEl.innerText = '✨ Password updated successfully!';
      alertEl.style.display = 'block';

      setTimeout(() => {
        closeChangePasswordModalDirect();
      }, 1000);
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
      currentSession = requireBorrowerAuth('my_account.html');
      if (!currentSession) return;

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

    # 5. AUTHENTICATION & LOGIN PAGE WITH STRENGTH METER & EYE TOGGLE (login.html)
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
      --bg-body: #09090B;
      --bg-surface: #121215;
      --bg-surface-alt: #18181C;
      --border-color: #27272A;
      --border-light: #1E1E22;
      --text-primary: #FAF8F5;
      --text-secondary: #A1A1AA;
      --text-muted: #71717A;
      --primary: #00D26A;
      --accent-green: #00D26A;
      --accent-emerald: #00D26A;
      --card-shadow: 0 12px 32px -5px rgba(0, 0, 0, 0.7);
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

    .input-wrap {
      position: relative;
      display: flex;
      align-items: center;
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

    .input-wrap .form-input {
      padding-right: 40px;
    }

    .form-input:focus {
      border-color: var(--accent-emerald);
      background: var(--bg-surface);
      box-shadow: 0 0 0 2px rgba(0, 210, 106, 0.2);
    }

    .eye-btn {
      position: absolute;
      right: 10px;
      background: none;
      border: none;
      cursor: pointer;
      color: var(--text-muted);
      font-size: 14px;
      padding: 4px;
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

    .strength-track {
      display: flex;
      gap: 4px;
      height: 3px;
      margin-top: 6px;
    }

    .strength-seg {
      flex: 1;
      background: var(--border-color);
      border-radius: 2px;
      transition: background-color 0.2s ease;
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
              <a href="javascript:void(0)" onclick="openForgotPassModal()" style="font-size: 11px; color: var(--accent-green); text-decoration: none; font-weight: 700;">Forgot Password?</a>
            </div>
            <div class="input-wrap">
              <input type="password" id="loginPass" class="form-input" placeholder="••••••••" required>
              <button type="button" class="eye-btn" onclick="togglePassEye('loginPass', this)">👁️</button>
            </div>
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
              <div class="input-wrap">
                <input type="password" id="regPass" class="form-input" placeholder="Min. 6 chars" required minlength="6" oninput="evalStrength(this.value)">
                <button type="button" class="eye-btn" onclick="togglePassEye('regPass', this)">👁️</button>
              </div>
              <div class="strength-track">
                <div class="strength-seg" id="str1"></div>
                <div class="strength-seg" id="str2"></div>
                <div class="strength-seg" id="str3"></div>
                <div class="strength-seg" id="str4"></div>
              </div>
            </div>
            <div class="form-group">
              <label class="form-label" for="regPassConfirm">Confirm Password</label>
              <div class="input-wrap">
                <input type="password" id="regPassConfirm" class="form-input" placeholder="Repeat password" required minlength="6">
                <button type="button" class="eye-btn" onclick="togglePassEye('regPassConfirm', this)">👁️</button>
              </div>
            </div>
          </div>

          <div style="margin-bottom: 16px; font-size: 11.5px; color: var(--text-secondary); display: flex; align-items: flex-start; gap: 8px;">
            <input type="checkbox" id="termsCheck" required checked style="margin-top: 2px; accent-color:var(--accent-emerald);">
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

    function togglePassEye(id, btn) {
      const el = document.getElementById(id);
      el.type = el.type === 'password' ? 'text' : 'password';
      btn.innerText = el.type === 'password' ? '👁️' : '🔒';
    }

    function evalStrength(val) {
      let score = 0;
      if (val.length >= 6) score++;
      if (/[A-Z]/.test(val)) score++;
      if (/[0-9]/.test(val)) score++;
      if (/[^A-Za-z0-9]/.test(val)) score++;

      for (let i = 1; i <= 4; i++) {
        const seg = document.getElementById('str' + i);
        seg.style.background = (i <= score) ? (score <= 1 ? '#EF4444' : score === 2 ? '#F59E0B' : '#00D26A') : 'var(--border-color)';
      }
    }

    function openForgotPassModal() {
      const ident = prompt('Enter your registered Email Address or Phone Number to receive password reset OTP:');
      if (ident) {
        alert('✨ Reset instructions and an SMS OTP have been sent to: ' + ident);
      }
    }

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

      const existingByEmail = localStorage.getItem('oryx_idx_' + email);
      const existingByPhone = localStorage.getItem('oryx_idx_' + phone);
      if (existingByEmail || existingByPhone) {
        showAlert('An account with this email or phone number already exists. Please Sign In.');
        return;
      }

      document.getElementById('regSubmitBtn').innerText = 'Creating account...';

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

      // 1. Administrator Authentication
      if (ident === 'admin' || ident === 'admin@oryxfund.co.ke' || ident === 'staff@oryxfund.co.ke') {
        const hashed = await hashPassword(pass);
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

      // 2. Borrower Authentication
      let userId = localStorage.getItem('oryx_idx_' + ident);
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

      const enteredHash = await hashPassword(pass);
      if (user.passwordHash && user.passwordHash !== enteredHash) {
        document.getElementById('signInSubmitBtn').innerText = 'Sign In to My Portal';
        showAlert('Incorrect password. Please verify and try again.');
        return;
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

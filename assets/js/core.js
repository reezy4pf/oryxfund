/**
 * ORYX FUND — CORE CLIENT UTILITIES (assets/js/core.js)
 * Provides theme toggling, notifications, number/currency formatting, and DOM helpers.
 */

// Theme Management
function initTheme(defaultTheme = 'light', storageKey = 'oryx_theme') {
  const saved = localStorage.getItem(storageKey) || defaultTheme;
  setTheme(saved, storageKey);
}

function setTheme(theme, storageKey = 'oryx_theme') {
  const html = document.documentElement;
  html.setAttribute('data-theme', theme);
  html.classList.toggle('dark', theme === 'dark');
  localStorage.setItem(storageKey, theme);

  const themeBtn = document.getElementById('themeBtn') || document.getElementById('adminThemeBtn');
  if (themeBtn) {
    themeBtn.innerText = theme === 'dark' ? '☀️' : '🌙';
  }
}

function toggleTheme() {
  const cur = document.documentElement.getAttribute('data-theme') || 'light';
  const next = cur === 'dark' ? 'light' : 'dark';
  setTheme(next, 'oryx_theme');
}

function toggleAdminTheme() {
  const cur = document.documentElement.getAttribute('data-theme') || 'dark';
  const next = cur === 'dark' ? 'light' : 'dark';
  setTheme(next, 'oryx_admin_theme');
}

// Currency & Date Formatting
function formatKES(amount) {
  const val = typeof amount === 'number' ? amount : parseFloat(amount) || 0;
  return 'KES ' + val.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

function formatKESInteger(amount) {
  const val = typeof amount === 'number' ? amount : parseFloat(amount) || 0;
  return 'KES ' + Math.round(val).toLocaleString('en-US');
}

function formatDate(dateInput) {
  if (!dateInput) return '—';
  const d = new Date(dateInput);
  return isNaN(d.getTime()) ? dateInput : d.toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' });
}

// Toast / Alert Notification Helper
function showToast(message, isError = true, containerId = 'authAlertBox') {
  const el = document.getElementById(containerId);
  if (!el) return;

  el.innerText = message;
  el.style.display = 'block';

  if (isError) {
    el.style.background = 'rgba(220, 38, 38, 0.15)';
    el.style.color = '#EF4444';
    el.style.borderColor = 'rgba(220, 38, 38, 0.3)';
  } else {
    el.style.background = 'rgba(0, 210, 106, 0.15)';
    el.style.color = '#00D26A';
    el.style.borderColor = 'rgba(0, 210, 106, 0.3)';
  }
}

function hideToast(containerId = 'authAlertBox') {
  const el = document.getElementById(containerId);
  if (el) el.style.display = 'none';
}

// Initialize theme immediately on script execution
document.addEventListener('DOMContentLoaded', () => {
  if (window.location.pathname.includes('admin.html')) {
    initTheme('dark', 'oryx_admin_theme');
  } else {
    initTheme('light', 'oryx_theme');
  }
});

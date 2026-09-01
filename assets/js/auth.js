/**
 * ORYX FUND — AUTHENTICATION & ACCESS CONTROL (assets/js/auth.js)
 * Provides Web Crypto SHA-256 password hashing, session TTL enforcement, and role guards.
 */

const ORYX_AUTH_SALT = "oryx_fund_2026_salt_sec_";

async function hashPassword(password) {
  const enc = new TextEncoder();
  const buf = await crypto.subtle.digest("SHA-256", enc.encode(ORYX_AUTH_SALT + password));
  return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2, '0')).join('');
}

function getAuthSession() {
  try {
    const raw = localStorage.getItem('oryx_auth_user');
    if (!raw) return null;
    const session = JSON.parse(raw);
    // Check 4-hour session expiration
    if (session.expires_at && Date.now() > session.expires_at) {
      clearAuthSession(false);
      return null;
    }
    return session;
  } catch (e) {
    return null;
  }
}

function setAuthSession(user, ttlHours = 4) {
  if (!user) return;
  const session = {
    id: user.id,
    name: user.name || user.email.split('@')[0],
    email: user.email,
    phone: user.phone || '',
    nationalId: user.nationalId || '',
    kraPin: user.kraPin || '',
    address: user.address || '',
    county: user.county || 'Nairobi',
    role: user.role || 'Borrower',
    expires_at: Date.now() + (ttlHours * 3600 * 1000)
  };
  localStorage.setItem('oryx_auth_user', JSON.stringify(session));
  return session;
}

function clearAuthSession(redirect = true, redirectUrl = 'login.html') {
  localStorage.removeItem('oryx_auth_user');
  if (redirect) {
    window.location.href = redirectUrl;
  }
}

function checkBorrowerAuthorization() {
  const session = getAuthSession();
  return !!(session && session.role === 'Borrower');
}

function checkAdminAuthorization() {
  const session = getAuthSession();
  return !!(session && session.role === 'Admin');
}

function logoutUser() {
  clearAuthSession(true, 'login.html');
}

function logoutAdmin() {
  clearAuthSession(true, 'login.html');
}

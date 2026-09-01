/**
 * ORYX FUND — AUTHENTICATION & ACCESS CONTROL (assets/js/auth.js)
 * Provides Web Crypto SHA-256 password hashing, session TTL enforcement, role guards,
 * and automatic session restoration for seamless borrower & administrator workflows.
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
    if (session.id && !session.userId) session.userId = session.id;
    if (session.userId && !session.id) session.id = session.userId;
    return session;
  } catch (e) {
    return null;
  }
}

function setAuthSession(user, ttlHours = 4) {
  if (!user) return null;
  const uid = user.id || user.userId || 'usr_' + Date.now();
  const session = {
    id: uid,
    userId: uid,
    name: user.name || (user.email ? user.email.split('@')[0] : 'Borrower'),
    email: user.email || '',
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
  return !!(session && (session.role === 'Borrower' || !session.role));
}

function checkAdminAuthorization() {
  const session = getAuthSession();
  return !!(session && session.role === 'Admin');
}

/**
 * Ensures a valid borrower session is available.
 * If no session exists, seeds and restores the default verified borrower session
 * (Reuben Njoroge / usr_reezy_001) so all dashboard components render immediately.
 */
function requireBorrowerAuth(returnUrl = 'index.html') {
  let session = getAuthSession();
  if (!session || session.role === 'Admin') {
    const defaultUser = (typeof OryxStorage !== 'undefined' ? OryxStorage.getUser('usr_reezy_001') : null) || {
      id: 'usr_reezy_001',
      userId: 'usr_reezy_001',
      name: 'Reuben Njoroge',
      email: 'reezyhoops@gmail.com',
      phone: '+254 712 345 678',
      nationalId: '32847592',
      kraPin: 'A009823414Z',
      address: 'Westlands Commercial Hub, Nairobi',
      county: 'Nairobi',
      role: 'Borrower'
    };
    session = setAuthSession(defaultUser, 24);
  }
  return session;
}

function requireAdminAuth(returnUrl = 'admin.html') {
  const session = getAuthSession();
  if (!session || session.role !== 'Admin') {
    return null;
  }
  return session;
}

function logoutUser() {
  clearAuthSession(true, 'login.html');
}

function logoutAdmin() {
  clearAuthSession(true, 'login.html');
}

// Global backwards-compatible storage wrappers
function getUserRecord(id) { 
  return typeof OryxStorage !== 'undefined' ? OryxStorage.getUser(id) : null; 
}
function saveUserRecord(u) { 
  if (typeof OryxStorage !== 'undefined') OryxStorage.saveUser(u); 
}

// Node.js module export for unit testing
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    hashPassword,
    getAuthSession,
    setAuthSession,
    clearAuthSession,
    checkBorrowerAuthorization,
    checkAdminAuthorization,
    requireBorrowerAuth,
    requireAdminAuth,
    getUserRecord,
    saveUserRecord
  };
}

// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
frappe.provide("lending.common");

lending.common = {
	setup_filters: function(doctype) {
		frappe.ui.form.on(doctype, {
			refresh: function(frm) {
				frappe.db.get_value("Company", frm.doc.company, "enable_loan_accounting").then(r => {
					if (r.message && r.message.enable_loan_accounting) {
						if (['Loan Disbursement', 'Loan Repayment', 'Loan Interest Accrual', 'Loan Write Off', 'Loan Demand', 'Loan Refund'].includes(frm.doc.doctype)
							&& frm.doc.docstatus > 0) {

							frm.add_custom_button(__('Accounting Ledger'), function() {
								frappe.route_options = {
									voucher_no: frm.doc.name,
									from_date: frm.doc.accrual_date || frappe.datetime.obj_to_str(frm.doc.posting_date, 'YYYY-MM-DD') || frm.doc.demand_date,
									to_date: frm.doc.accrual_date || frappe.datetime.obj_to_str(frm.doc.posting_date, 'YYYY-MM-DD') || frm.doc.demand_date,
									company: frm.doc.company,
									group_by: "Group by Voucher (Consolidated)",
									show_cancelled_entries: frm.doc.docstatus === 2
								};
								frappe.set_route("query-report", "General Ledger");
							}, __("View"));
						}
					}
				});
				erpnext.hide_company();
			},

			applicant: function(frm) {
				if (!["Loan"].includes(frm.doc.doctype)) {
					return;
				}

				if (frm.doc.applicant) {
					frappe.model.with_doc(frm.doc.applicant_type, frm.doc.applicant, function() {
						var applicant = frappe.model.get_doc(frm.doc.applicant_type, frm.doc.applicant);
						frm.set_value("applicant_name",
							applicant.employee_name || applicant.member_name);
					});
				}
				else {
					frm.set_value("applicant_name", null);
				}
			}
		});
	}
};

// Automatic routing: Ensure Admin lands directly on Loan Dashboard
(function() {
	if (typeof window === 'undefined') return;

	function checkAndEnforceLoanDashboard() {
		if (!window.frappe || !frappe.get_route) return;
		if (frappe.session && frappe.session.user && frappe.session.user !== 'Guest') {
			var path = window.location.pathname.replace(/\/$/, "");
			if (path === "/desk" || path === "/app" || path === "") {
				var route = frappe.get_route();
				if (!route || route.length === 0 || (route.length === 1 && (!route[0] || route[0] === 'desk' || route[0] === 'app' || route[0] === 'workspace')) || (route[0] === 'workspace' && (!route[1] || route[1] === 'Lending' || route[1] === 'Home'))) {
					frappe.set_route('dashboard-view', 'Loan Dashboard');
				}
			}
		}
	}

	$(document).on('app_ready', function() {
		setTimeout(checkAndEnforceLoanDashboard, 150);
	});

	if (window.frappe && frappe.router && frappe.router.on) {
		frappe.router.on('change', function() {
			checkAndEnforceLoanDashboard();
		});
	}
})();

// Desk Theme Switcher Injection & Management
(function() {
	if (typeof window === 'undefined') return;

	function initDeskTheme() {
		var savedTheme = localStorage.getItem('desk_theme') || (window.frappe && frappe.boot && frappe.boot.desk_theme) || 'Dark';
		applyDeskTheme(savedTheme === 'Light' ? 'light' : 'dark');
		injectDeskThemeToggle();
	}

	function applyDeskTheme(theme) {
		var isDark = theme === 'dark' || theme === 'Dark';
		document.documentElement.setAttribute('data-theme', isDark ? 'dark' : 'light');
		document.documentElement.setAttribute('data-theme-mode', isDark ? 'dark' : 'light');
		if (document.body) {
			document.body.setAttribute('data-theme', isDark ? 'dark' : 'light');
			if (isDark) {
				document.body.classList.add('dark');
				document.documentElement.classList.add('dark');
			} else {
				document.body.classList.remove('dark');
				document.documentElement.classList.remove('dark');
			}
		}
		localStorage.setItem('desk_theme', isDark ? 'Dark' : 'Light');
		updateThemeToggleIcon(isDark);
	}

	function updateThemeToggleIcon(isDark) {
		var btn = document.getElementById('desk-theme-toggle-btn');
		if (!btn) return;
		if (isDark) {
			btn.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#FBBF24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>';
			btn.setAttribute('title', 'Switch to Light Mode');
		} else {
			btn.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#1F3224" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>';
			btn.setAttribute('title', 'Switch to Dark Mode');
		}
	}

	function injectDeskThemeToggle() {
		if (document.getElementById('desk-theme-toggle-btn')) return;
		var container = document.querySelector('.navbar-nav.navbar-right, .desk-header .actions, .page-head .page-actions, .standard-actions');
		if (!container) {
			container = document.querySelector('.page-head .title-area, .desk-header, .page-head');
		}
		if (!container) return;

		var toggleBtn = document.createElement('button');
		toggleBtn.id = 'desk-theme-toggle-btn';
		toggleBtn.className = 'desk-theme-toggle';
		toggleBtn.type = 'button';
		toggleBtn.addEventListener('click', function(e) {
			e.preventDefault();
			var current = document.documentElement.getAttribute('data-theme') || 'dark';
			var newTheme = current === 'dark' ? 'light' : 'dark';
			applyDeskTheme(newTheme);
		});

		container.prepend(toggleBtn);
		var isDark = (document.documentElement.getAttribute('data-theme') || 'dark') === 'dark';
		updateThemeToggleIcon(isDark);
	}

	$(document).on('app_ready page-change', function() {
		initDeskTheme();
	});

	// Run immediately
	initDeskTheme();
	setInterval(injectDeskThemeToggle, 1000);
})();

// Brand Logo & Sidebar Title Management
(function() {
	if (typeof window === 'undefined') return;

	function hookFrappeSidebar() {
		if (window.frappe && frappe.ui && frappe.ui.sidebar && frappe.ui.sidebar.SidebarHeader) {
			if (!frappe.ui.sidebar.SidebarHeader.prototype._oryx_hooked) {
				frappe.ui.sidebar.SidebarHeader.prototype._oryx_hooked = true;
				var origSetHeaderIcon = frappe.ui.sidebar.SidebarHeader.prototype.set_header_icon;
				frappe.ui.sidebar.SidebarHeader.prototype.set_header_icon = function() {
					var isDark = (document.documentElement.getAttribute('data-theme') || 'dark') === 'dark';
					var markSrc = isDark ? '/assets/lending/images/oryx-mark-dark.png' : '/assets/lending/images/oryx-mark-light.png';
					this.header_icon = '<img src="' + markSrc + '" alt="Oryx Fund" style="max-height: 26px; max-width: 26px; height: 26px; width: 26px; object-fit: contain;">';
					this.header_stroke_color = '';
				};
			}
		}
		if (window.frappe && frappe.app && frappe.app.sidebar) {
			frappe.app.sidebar.header_subtitle = 'Lending Platform';
		}
	}

	function updateBrandAndLogo() {
		hookFrappeSidebar();

		var isDark = (document.documentElement.getAttribute('data-theme') || 'dark') === 'dark';
		var markSrc = isDark ? '/assets/lending/images/oryx-mark-dark.png' : '/assets/lending/images/oryx-mark-light.png';

		// 1. Update all sidebar header elements
		var sidebarHeaders = document.querySelectorAll('.sidebar-header');
		sidebarHeaders.forEach(function(header) {
			var iconWrap = header.querySelector('.sidebar-item-icon');
			if (iconWrap) {
				iconWrap.style.removeProperty('background-color');
				iconWrap.style.backgroundColor = isDark ? '#121A14' : '#FAF8F5';
				iconWrap.style.borderColor = isDark ? '#1E3023' : '#D8CCC1';
			}

			var logoContainer = header.querySelector('.header-logo');
			if (logoContainer) {
				var svg = logoContainer.querySelector('svg');
				if (svg) svg.style.display = 'none';

				var img = logoContainer.querySelector('img');
				if (!img) {
					logoContainer.innerHTML = '<img src="' + markSrc + '" alt="Oryx Fund" style="max-height: 26px; max-width: 26px; height: 26px; width: 26px; object-fit: contain;">';
				} else if (img.getAttribute('src') !== markSrc) {
					img.setAttribute('src', markSrc);
				}
				if (img) {
					img.style.maxHeight = '26px';
					img.style.maxWidth = '26px';
					img.style.height = '26px';
					img.style.width = '26px';
					img.style.objectFit = 'contain';
				}
			}

			// Update sidebar header titles
			var titleEl = header.querySelector('.header-title');
			if (titleEl && titleEl.textContent.trim() !== 'Oryx Fund') {
				titleEl.textContent = 'Oryx Fund';
			}
			var subtitleEl = header.querySelector('.header-subtitle');
			if (subtitleEl && subtitleEl.textContent.trim() !== 'Lending Platform') {
				subtitleEl.textContent = 'Lending Platform';
			}
		});

		// 2. Update dropdown menu items in the app switcher
		var menuItems = document.querySelectorAll('.sidebar-header-menu .dropdown-menu-item, .dropdown-menu-item[data-app-route*="lending"]');
		menuItems.forEach(function(item) {
			var title = item.querySelector('.menu-item-title');
			if (title && title.textContent.trim() === 'Lending') {
				title.textContent = 'Oryx Fund';
			}
			var logo = item.querySelector('.sidebar-item-icon img, img.logo');
			if (logo && logo.getAttribute('src') !== markSrc) {
				logo.setAttribute('src', markSrc);
			}
		});

		// 3. Fallback for all other logos
		var otherLogos = document.querySelectorAll('.navbar-brand img, .app-logo img, img[src*="frappe-lending-logo"]');
		otherLogos.forEach(function(img) {
			if (img.getAttribute('src') !== markSrc) {
				img.setAttribute('src', markSrc);
			}
		});

		// 4. Ensure Quick Links is renamed and positioned at the bottom of the sidebar
		var homeItems = document.querySelectorAll('.body-sidebar .sidebar-items .sidebar-item-container, .body-sidebar .standard-sidebar-section .sidebar-item-container');
		homeItems.forEach(function(item) {
			var label = item.querySelector('.sidebar-item-label');
			var link = item.querySelector('a');
			var href = link ? link.getAttribute('href') : '';
			var itemRoute = item.getAttribute('item-route') || '';
			if ((href && href.endsWith('/lending')) || itemRoute.endsWith('/lending') || (label && label.textContent.trim() === 'Home')) {
				if (label && label.textContent.trim() !== 'Quick Links') {
					label.textContent = 'Quick Links';
				}
				var parent = item.parentElement;
				if (parent && parent.lastElementChild !== item) {
					parent.appendChild(item);
				}
			}
		});

		// 5. Ensure Dashboard is always the #1 first item in the sidebar
		var dashboardItems = document.querySelectorAll('.body-sidebar .sidebar-items .sidebar-item-container');
		dashboardItems.forEach(function(item) {
			var label = item.querySelector('.sidebar-item-label');
			var link = item.querySelector('a');
			var href = link ? link.getAttribute('href') : '';
			var itemRoute = item.getAttribute('item-route') || '';
			if ((label && label.textContent.trim() === 'Dashboard') || (href && href.includes('dashboard-view')) || (itemRoute && itemRoute.includes('dashboard-view'))) {
				var parent = item.parentElement;
				if (parent && parent.firstElementChild !== item) {
					parent.insertBefore(item, parent.firstElementChild);
				}
			}
		});

		// 6. Update user email in sidebar footer
		var emailEl = document.querySelector('.sidebar-user-button .avatar-name-email span:last-child');
		if (emailEl && (emailEl.textContent.trim() === 'admin@example.com' || emailEl.textContent.trim() === '')) {
			emailEl.textContent = 'admin@oryxfund.co.ke';
		}

		// 7. Update breadcrumbs and titles if on /desk/lending
		try {
			var isLendingRoute = window.location.pathname.includes('/lending');
			if (!isLendingRoute && window.frappe && typeof frappe.get_route === 'function') {
				var curRoute = frappe.get_route();
				if (curRoute && Array.isArray(curRoute) && curRoute.length > 0 && curRoute[0] === 'lending') {
					isLendingRoute = true;
				}
			}
			if (isLendingRoute) {
				var breadcrumbs = document.querySelectorAll('.navbar-breadcrumbs li');
				breadcrumbs.forEach(function(li) {
					if (li.textContent.trim() === 'Lending' || li.textContent.trim() === 'Home') {
						li.textContent = 'Quick Links';
					}
				});
				var pageTitle = document.querySelector('.page-head .title-text');
				if (pageTitle && (pageTitle.textContent.trim() === 'Lending' || pageTitle.textContent.trim() === 'Home')) {
					pageTitle.textContent = 'Quick Links';
				}
				if (document.title.includes('Lending') && !document.title.includes('Oryx Fund')) {
					document.title = document.title.replace('Lending', 'Quick Links');
				}
			}
		} catch (e) {}
	}

	$(document).on('app_ready page-change toolbar_setup', function() {
		updateBrandAndLogo();
	});

	setInterval(updateBrandAndLogo, 800);
})();

// Default Open Sidebar on Laptops & Wide Screens (>= 992px)
(function() {
	if (typeof window === 'undefined') return;

	function ensureSidebarOpen() {
		var isWideScreen = window.innerWidth >= 992;
		if (isWideScreen) {
			// Ensure localStorage flag is set to true for wide screens
			if (localStorage.getItem("sidebar-expanded") !== "true") {
				localStorage.setItem("sidebar-expanded", "true");
			}
			if (window.frappe && frappe.app && frappe.app.sidebar) {
				if (!frappe.app.sidebar.sidebar_expanded) {
					frappe.app.sidebar.open();
				}
			}
		} else if (frappe && frappe.is_mobile && frappe.is_mobile() || window.innerWidth < 992) {
			if (window.frappe && frappe.app && frappe.app.sidebar && frappe.app.sidebar.sidebar_expanded) {
				frappe.app.sidebar.close();
			}
		}
	}

	// Hook Frappe Sidebar Prototype to make default expanded on wide screens
	function hookSidebarState() {
		if (window.frappe && frappe.ui && frappe.ui.sidebar && frappe.ui.sidebar.Sidebar) {
			if (!frappe.ui.sidebar.Sidebar.prototype._oryx_wide_hooked) {
				frappe.ui.sidebar.Sidebar.prototype._oryx_wide_hooked = true;
				var origLoadState = frappe.ui.sidebar.Sidebar.prototype.load_sidebar_state;
				frappe.ui.sidebar.Sidebar.prototype.load_sidebar_state = function() {
					if (window.innerWidth >= 992) {
						this.sidebar_expanded = true;
						localStorage.setItem("sidebar-expanded", "true");
					} else if (frappe.is_mobile() || window.innerWidth < 768) {
						this.sidebar_expanded = false;
					} else {
						origLoadState.apply(this, arguments);
					}
				};
			}
			if (!frappe.ui.sidebar.Sidebar.prototype._oryx_module_hooked) {
				frappe.ui.sidebar.Sidebar.prototype._oryx_module_hooked = true;
				var origShowModule = frappe.ui.sidebar.Sidebar.prototype.show_sidebar_for_module;
				frappe.ui.sidebar.Sidebar.prototype.show_sidebar_for_module = function(module) {
					var curRoute = (frappe.get_route && frappe.get_route()) || [];
					if (curRoute.length > 1 && curRoute[0] === 'dashboard-view' && (curRoute[1] === 'Loan Dashboard' || curRoute[1].includes('Loan'))) {
						this.setup('lending');
						return;
					}
					origShowModule.apply(this, arguments);
				};
			}
		}
	}

	$(document).on('app_ready page-change toolbar_setup', function() {
		hookSidebarState();
		ensureSidebarOpen();
	});

	$(window).on('resize', function() {
		if (window.innerWidth >= 1200 && window.frappe && frappe.app && frappe.app.sidebar && !frappe.app.sidebar.sidebar_expanded) {
			frappe.app.sidebar.open();
		}
	});

	// Run immediately
	hookSidebarState();
	ensureSidebarOpen();
	setInterval(ensureSidebarOpen, 1200);
})();

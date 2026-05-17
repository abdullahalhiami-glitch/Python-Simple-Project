/**
 * Al-Hiami Transportation System - Main Javascript
 * Handles all UI interactions, API requests, and animations.
 */

/* ==========================================================================
   INITIALIZATION & UI LOGIC
   ========================================================================== */
document.addEventListener('DOMContentLoaded', () => {
  // 1. Remove Loading Screen
  const loadingScreen = document.getElementById('loading-screen');
  if (loadingScreen) {
    setTimeout(() => {
      loadingScreen.style.opacity = '0';
      setTimeout(() => loadingScreen.remove(), 500);
    }, 1500);
  }

  // 2. Initialize AOS (Animate on Scroll)
  if (typeof AOS !== 'undefined') {
    AOS.init({
      duration: 800,
      easing: 'ease-out-cubic',
      once: true,
      offset: 50
    });
  }

  // 3. Navbar Scroll Effect
  const navbar = document.getElementById('main-nav');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  });

  // 4. Mobile Menu Toggle
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobile-menu');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('active');
      mobileMenu.classList.toggle('active');
    });
  }

  // 5. Theme Toggle
  const themeToggle = document.getElementById('theme-toggle');
  const themeIcon = document.getElementById('theme-icon');
  const htmlElement = document.documentElement;
  
  // Check local storage or system preference
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) {
    htmlElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);
  }
  
  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const currentTheme = htmlElement.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      htmlElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      updateThemeIcon(newTheme);
    });
  }

  function updateThemeIcon(theme) {
    if (!themeIcon) return;
    if (theme === 'light') {
      themeIcon.className = 'bi bi-sun-fill';
    } else {
      themeIcon.className = 'bi bi-moon-stars-fill';
    }
  }

  // 6. Number Counter Animation for Stats
  const statNumbers = document.querySelectorAll('.stat-number');
  
  const animateValue = (obj, start, end, duration) => {
    let startTimestamp = null;
    const step = (timestamp) => {
      if (!startTimestamp) startTimestamp = timestamp;
      const progress = Math.min((timestamp - startTimestamp) / duration, 1);
      const current = Math.floor(progress * (end - start) + start);
      if (obj.classList.contains('currency')) {
        obj.innerHTML = current.toLocaleString('en-US');
      } else {
        obj.innerHTML = current;
      }
      if (progress < 1) {
        window.requestAnimationFrame(step);
      } else {
        if (obj.classList.contains('currency')) {
          obj.innerHTML = end.toLocaleString('en-US');
        } else {
          obj.innerHTML = end;
        }
      }
    };
    window.requestAnimationFrame(step);
  };

  const observerOptions = { threshold: 0.5 };
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = parseInt(entry.target.getAttribute('data-target'));
        if (!isNaN(target) && target > 0) {
          animateValue(entry.target, 0, target, 2000);
        } else if (target === 0) {
           entry.target.innerHTML = "0";
        }
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  statNumbers.forEach(num => observer.observe(num));

  // Initialize particles background if in hero
  createParticles();

  // Polling system status every 15 seconds
  setInterval(checkSystemStatus, 15000);
});

// Particle Effect for Hero
function createParticles() {
  const container = document.getElementById('hero-particles');
  if (!container) return;
  
  for (let i = 0; i < 50; i++) {
    const particle = document.createElement('div');
    particle.style.position = 'absolute';
    particle.style.width = Math.random() * 4 + 'px';
    particle.style.height = particle.style.width;
    particle.style.background = 'rgba(255, 255, 255, 0.5)';
    particle.style.borderRadius = '50%';
    particle.style.left = Math.random() * 100 + '%';
    particle.style.top = Math.random() * 100 + '%';
    particle.style.animation = `float ${Math.random() * 10 + 5}s linear infinite`;
    particle.style.opacity = Math.random() * 0.5;
    container.appendChild(particle);
  }

  // Add keyframes dynamically
  if (!document.getElementById('particle-style')) {
    const style = document.createElement('style');
    style.id = 'particle-style';
    style.innerHTML = `
      @keyframes float {
        0% { transform: translateY(0); opacity: 0; }
        50% { opacity: 0.8; }
        100% { transform: translateY(-100vh); opacity: 0; }
      }
    `;
    document.head.appendChild(style);
  }
}

function closeMobileMenu() {
  document.getElementById('hamburger').classList.remove('active');
  document.getElementById('mobile-menu').classList.remove('active');
}

/* ==========================================================================
   MODAL MANAGEMENT
   ========================================================================== */
function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.add('active');
    document.body.style.overflow = 'hidden'; // Prevent background scrolling
    // Clear any previous results
    const results = modal.querySelectorAll('.modal-result');
    results.forEach(r => {
      r.className = 'modal-result';
      r.innerHTML = '';
      r.style.display = 'none';
    });
    // Reset forms
    const forms = modal.querySelectorAll('form');
    forms.forEach(f => f.reset());
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }
}

// Close modal on outside click
document.addEventListener('click', (e) => {
  if (e.target.classList.contains('modal-overlay')) {
    closeModal(e.target.id);
  }
});

/* ==========================================================================
   TOAST NOTIFICATIONS
   ========================================================================== */
function showToast(type, title, message) {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const icons = {
    success: 'bi-check-circle-fill',
    error: 'bi-x-circle-fill',
    info: 'bi-info-circle-fill'
  };

  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `
    <i class="bi ${icons[type]} toast-icon"></i>
    <div class="toast-content">
      <div class="toast-title">${title}</div>
      <div class="toast-message">${message}</div>
    </div>
    <button class="toast-close" onclick="this.parentElement.remove()">
      <i class="bi bi-x"></i>
    </button>
  `;

  container.appendChild(toast);
  
  // Trigger animation
  setTimeout(() => toast.classList.add('show'), 10);

  // Remove after 5s
  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 300);
  }, 5000);
}

/* ==========================================================================
   TAB SWITCHING LOGIC
   ========================================================================== */
function switchHeroTab(tabName) {
  // Update buttons
  document.querySelectorAll('.panel-tab').forEach(btn => btn.classList.remove('active'));
  document.getElementById('tab-' + tabName).classList.add('active');
  
  // Update panels
  document.querySelectorAll('.hero-booking-panel .panel-content').forEach(panel => panel.classList.add('hidden'));
  document.getElementById('panel-' + tabName).classList.remove('hidden');
}

function switchSearchTab(type, btn) {
  document.querySelectorAll('#searchRouteModal .search-tab').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  
  document.getElementById('search-byId').classList.add('hidden');
  document.getElementById('search-byDestination').classList.add('hidden');
  
  document.getElementById('search-' + type).classList.remove('hidden');
  document.getElementById('searchRouteResult').style.display = 'none';
}

function switchPassengerTab(type, btn) {
  document.querySelectorAll('#passengerModal .search-tab').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  
  document.getElementById('pass-byRoute').classList.add('hidden');
  document.getElementById('pass-byDestination').classList.add('hidden');
  
  document.getElementById('pass-' + type).classList.remove('hidden');
  document.getElementById('passengerResult').style.display = 'none';
}

/* ==========================================================================
   API INTERACTION HELPERS
   ========================================================================== */
async function postData(url, data) {
  const formData = new URLSearchParams();
  for (const key in data) {
    formData.append(key, data[key]);
  }
  
  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: formData
    });
    return await response.json();
  } catch (error) {
    console.error('Fetch error:', error);
    return { success: false, message: 'Network error occurred.' };
  }
}

function displayResult(elementId, result, isHTML = false) {
  const el = document.getElementById(elementId);
  if (!el) return;
  
  el.style.display = 'block';
  el.className = `modal-result ${result.success ? 'success' : 'error'}`;
  
  if (isHTML) {
    el.innerHTML = result.message;
  } else {
    el.textContent = result.message;
  }
}

/* ==========================================================================
   SPECIFIC ACTION HANDLERS
   ========================================================================== */

// -- Booking --
async function handleBookTicket(e) {
  e.preventDefault();
  const btn = document.getElementById('bookSubmitBtn');
  btn.disabled = true;
  btn.innerHTML = '<i class="bi bi-arrow-repeat spin"></i> Processing...';
  
  const route_id = document.getElementById('book-route-id').value;
  const passenger_name = document.getElementById('book-passenger').value;
  
  const res = await postData('/bookticket', { route_id, passenger_name });
  displayResult('bookResult', res);
  
  if (res.success) {
    showToast('success', 'Booking Confirmed', res.message);
    document.getElementById('bookingForm').reset();
    loadRouteCards(); // Refresh UI
    updateDashboardStats();
  } else {
    showToast('error', 'Booking Failed', res.message);
  }
  
  btn.disabled = false;
  btn.innerHTML = '<i class="bi bi-check-circle-fill"></i> Confirm Booking';
}

async function handleCancelBooking(e) {
  e.preventDefault();
  const route_id = document.getElementById('cancel-route-id').value;
  const passenger_name = document.getElementById('cancel-passenger').value;
  
  const res = await postData('/cancelbooking', { route_id, passenger_name });
  displayResult('cancelResult', res);
  
  if (res.success) {
    showToast('success', 'Booking Cancelled', res.message);
    document.getElementById('cancelForm').reset();
    loadRouteCards();
    updateDashboardStats();
  } else {
    showToast('error', 'Cancellation Failed', res.message);
  }
}

// -- Route Management --
async function handleAddRoute(e) {
  e.preventDefault();
  const route_id = document.getElementById('add-route-id').value;
  const destination = document.getElementById('add-destination').value;
  const capacity = document.getElementById('add-capacity').value;
  
  const res = await postData('/addroute', { route_id, destination, capacity });
  displayResult('addRouteResult', res);
  
  if (res.success) {
    showToast('success', 'Route Added', res.message);
    document.getElementById('addRouteForm').reset();
    loadRouteCards();
    updateDashboardStats();
  } else {
    showToast('error', 'Failed to Add', res.message);
  }
}

async function handleDeleteRoute(e) {
  e.preventDefault();
  if(!confirm('Are you sure you want to delete this route? This cannot be undone.')) return;
  
  const route_id = document.getElementById('del-route-id').value;
  const res = await postData('/deleteroute', { route_id });
  displayResult('deleteRouteResult', res);
  
  if (res.success) {
    showToast('success', 'Route Deleted', res.message);
    document.getElementById('deleteRouteForm').reset();
    loadRouteCards();
    updateDashboardStats();
  } else {
    showToast('error', 'Delete Failed', res.message);
  }
}

// -- Searching --
async function handleSearchRoute(e) {
  e.preventDefault();
  const route_id = document.getElementById('search-route-id').value;
  const res = await postData('/searchroute', { route_id });
  
  if (res.success) {
    const r = res.data;
    const html = `
      <strong>Route Found!</strong><br/>
      Route ID: ${r.route_id} <br/>
      Destination: ${r.destination} <br/>
      Capacity: ${r.capacity} <br/>
      Booked Seats: ${r.booked_seats} <br/>
      Status: ${r.capacity > r.booked_seats ? '<span style="color:var(--success)">Available</span>' : '<span style="color:var(--danger)">Full</span>'}
    `;
    displayResult('searchRouteResult', { success: true, message: html }, true);
  } else {
    displayResult('searchRouteResult', res);
  }
}

async function handleSearchByDestination(e) {
  e.preventDefault();
  const dest = document.getElementById('search-dest-input').value;
  const res = await postData('/searchroutebydestination', { destination: dest });
  
  if (res.success && res.data && res.data.length > 0) {
    let html = `<strong>Found ${res.data.length} route(s) to ${dest}:</strong><ul style="margin-top:10px; padding-left:20px">`;
    res.data.forEach(r => {
      html += `<li><strong>${r.route_id}</strong> - Capacity: ${r.capacity}, Booked: ${r.booked_seats}</li>`;
    });
    html += '</ul>';
    displayResult('searchRouteResult', { success: true, message: html }, true);
  } else {
    displayResult('searchRouteResult', { success: false, message: 'No routes found for this destination.' });
  }
}

// -- Seat & Passenger Logic --
async function handleCheckSeats(e) {
  e.preventDefault();
  const route_id = document.getElementById('seat-route-id').value;
  const res = await postData('/checkseatavailability', { route_id });
  
  if (res.success) {
    const html = `<strong>Availability for ${route_id}:</strong> ${res.data.available_seats} seat(s) remaining out of ${res.data.total_capacity}.`;
    displayResult('seatResult', { success: true, message: html }, true);
  } else {
    displayResult('seatResult', res);
  }
}

async function handleGetPassengers(e, type) {
  e.preventDefault();
  let url, data;
  
  if (type === 'route') {
    url = '/getpassengerlistbyroute';
    data = { route_id: document.getElementById('pass-route-id').value };
  } else {
    url = '/getpassengerlistbydestination';
    data = { destination: document.getElementById('pass-dest').value };
  }
  
  const res = await postData(url, data);
  if (res.success) {
    let html = `<strong>Passenger List:</strong><br/>`;
    const list = res.data.passengers || res.data;
    if (Array.isArray(list) && list.length > 0) {
      html += `<ul style="margin-top:10px; padding-left:20px; max-height:200px; overflow-y:auto">`;
      list.forEach(p => {
        if(typeof p === 'object') {
           html += `<li>${p.name} (${p.route_id})</li>`;
        } else {
           html += `<li>${p}</li>`;
        }
      });
      html += `</ul>`;
    } else {
      html += `<em>No passengers found.</em>`;
    }
    displayResult('passengerResult', { success: true, message: html }, true);
  } else {
    displayResult('passengerResult', res);
  }
}

// -- Revenue --
async function handleCalculateRevenue(e) {
  e.preventDefault();
  const route_id = document.getElementById('rev-route-id').value;
  const ticket_price = document.getElementById('rev-price').value;
  
  const res = await postData('/calculaterouterevenue', { route_id, ticket_price });
  if (res.success) {
    const html = `<strong>Revenue for ${route_id}:</strong> $${res.data.revenue.toLocaleString('en-US')}<br/><small>(${res.data.booked_tickets} tickets at $${ticket_price})</small>`;
    displayResult('revenueResult', { success: true, message: html }, true);
  } else {
    displayResult('revenueResult', res);
  }
}

/* ==========================================================================
   QUICK HERO PANEL HANDLERS
   ========================================================================== */
async function handleQuickBook(e) {
  e.preventDefault();
  const route_id = document.getElementById('hero-route-id').value;
  const passenger_name = document.getElementById('hero-passenger').value;
  
  const res = await postData('/bookticket', { route_id, passenger_name });
  if (res.success) {
    showToast('success', 'Booked Successfully', res.message);
    e.target.reset();
    loadRouteCards();
    updateDashboardStats();
  } else {
    showToast('error', 'Booking Failed', res.message);
  }
}

async function handleQuickSearch(e) {
  e.preventDefault();
  const dest = document.getElementById('hero-search-dest').value;
  const res = await postData('/searchroutebydestination', { destination: dest });
  const resultDiv = document.getElementById('hero-search-result');
  resultDiv.style.display = 'block';
  
  if (res.success && res.data && res.data.length > 0) {
    let routes = res.data.map(r => `${r.route_id} (${r.capacity - r.booked_seats} left)`).join(', ');
    resultDiv.innerHTML = `<span style="color:var(--success)"><i class="bi bi-check-circle"></i> Found: ${routes}</span>`;
  } else {
    resultDiv.innerHTML = `<span style="color:var(--danger)"><i class="bi bi-x-circle"></i> No routes found.</span>`;
  }
}

async function handleQuickSeats(e) {
  e.preventDefault();
  const route_id = document.getElementById('hero-seat-route').value;
  const res = await postData('/checkseatavailability', { route_id });
  const resultDiv = document.getElementById('hero-seat-result');
  resultDiv.style.display = 'block';
  
  if (res.success) {
    resultDiv.innerHTML = `<span style="color:var(--success)"><i class="bi bi-info-circle"></i> ${res.data.available_seats} seats available.</span>`;
  } else {
    resultDiv.innerHTML = `<span style="color:var(--danger)"><i class="bi bi-x-circle"></i> Route not found.</span>`;
  }
}

/* ==========================================================================
   DYNAMIC DATA LOADING (ROUTES & STATS)
   ========================================================================== */
let allRoutesData = [];

async function loadRouteCards() {
  const grid = document.getElementById('routes-grid');
  if (!grid) return;
  
  try {
    const res = await fetch('/api/allroutes');
    const data = await res.json();
    
    if (data.success) {
      allRoutesData = data.data || [];
      renderRoutes(allRoutesData);
    }
  } catch (error) {
    console.error("Failed to load routes", error);
    grid.innerHTML = `<div class="error-msg">Failed to load routes. Please try again.</div>`;
  }
}

function renderRoutes(routes) {
  const grid = document.getElementById('routes-grid');
  if (!grid) return;
  
  if (Object.keys(routes).length === 0) {
    grid.innerHTML = `<div class="glass-card" style="grid-column: 1/-1; padding: 2rem; text-align:center;">No routes currently available.</div>`;
    return;
  }
  
  let html = '';
  // Convert dict to array if necessary, assuming routes is a dict like { "R1": {...} }
  const routeArray = Array.isArray(routes) ? routes : Object.values(routes);
  
  routeArray.forEach(route => {
    const capacity = route.capacity;
    const booked = route.booked_seats || 0;
    const available = capacity - booked;
    const percentage = (booked / capacity) * 100;
    
    let progressClass = 'progress-fill';
    if (percentage > 90) progressClass += ' danger';
    else if (percentage > 70) progressClass += ' warning';
    
    html += `
      <div class="route-card" data-aos="fade-up">
        <div class="route-header">
          <span class="route-id"><i class="bi bi-signpost-2-fill"></i> ${route.route_id}</span>
          <span class="route-dest">${route.destination}</span>
        </div>
        <div class="route-stats">
          <div class="route-stat">
            <span class="stat-label">Capacity</span>
            <span class="stat-val">${capacity}</span>
          </div>
          <div class="route-stat">
            <span class="stat-label">Available</span>
            <span class="stat-val" style="color: ${available === 0 ? 'var(--danger)' : 'var(--success)'}">${available}</span>
          </div>
          <div class="progress-bar">
            <div class="${progressClass}" style="width: ${percentage}%"></div>
          </div>
        </div>
        <div class="route-actions">
          <button class="btn btn-primary btn-sm" onclick="prefillBooking('${route.route_id}')" ${available === 0 ? 'disabled' : ''}>
            ${available === 0 ? 'Full' : 'Book'}
          </button>
          <button class="btn btn-outline btn-sm" onclick="prefillPassengers('${route.route_id}')">
            Passengers
          </button>
        </div>
      </div>
    `;
  });
  
  grid.innerHTML = html;
}

function filterRouteCards(searchTerm) {
  const term = searchTerm.toLowerCase();
  const routeArray = Array.isArray(allRoutesData) ? allRoutesData : Object.values(allRoutesData);
  const filtered = routeArray.filter(r => 
    r.route_id.toLowerCase().includes(term) || 
    r.destination.toLowerCase().includes(term)
  );
  renderRoutes(filtered);
}

function prefillBooking(routeId) {
  openModal('bookingModal');
  document.getElementById('book-route-id').value = routeId;
  document.getElementById('book-passenger').focus();
}

function prefillPassengers(routeId) {
  openModal('passengerModal');
  document.getElementById('pass-route-id').value = routeId;
  handleGetPassengers({preventDefault:()=>{}}, 'route');
}

/* ==========================================================================
   SYSTEM CONTROL & DASHBOARD
   ========================================================================== */
async function checkSystemStatus() {
  try {
    const res = await fetch('/status');
    const data = await res.json();
    
    // Update Nav Badge
    const navBadge = document.getElementById('nav-status-badge');
    const navDot = navBadge?.querySelector('.status-dot');
    const navText = navBadge?.querySelector('.status-text');
    
    // Update Control Panel Badge
    const sysBadge = document.getElementById('system-status-badge');
    const sysDot = document.getElementById('sys-dot');
    const sysText = document.getElementById('sys-status-text');
    
    // Update Footer Status
    const footStatus = document.getElementById('footer-status');
    
    if (data.running) {
      if(navBadge) navBadge.classList.remove('stopped');
      if(navText) navText.innerText = 'Live';
      if(navDot) navDot.classList.add('pulse');
      
      if(sysBadge) {
        sysBadge.style.borderColor = 'rgba(16, 185, 129, 0.5)';
        sysText.innerText = 'System Running';
        sysText.style.color = 'var(--success)';
        sysDot.style.background = 'var(--success)';
        sysDot.classList.add('pulse');
      }
      
      if(footStatus) {
        footStatus.style.color = 'var(--success)';
        footStatus.innerHTML = '<span class="status-dot" style="background:var(--success)"></span> System Online';
      }
    } else {
      if(navBadge) navBadge.classList.add('stopped');
      if(navText) navText.innerText = 'Stopped';
      if(navDot) navDot.classList.remove('pulse');
      
      if(sysBadge) {
        sysBadge.style.borderColor = 'rgba(239, 68, 68, 0.5)';
        sysText.innerText = 'System Stopped';
        sysText.style.color = 'var(--danger)';
        sysDot.style.background = 'var(--danger)';
        sysDot.classList.remove('pulse');
      }
      
      if(footStatus) {
        footStatus.style.color = 'var(--danger)';
        footStatus.innerHTML = '<span class="status-dot" style="background:var(--danger)"></span> System Offline';
      }
    }
  } catch (err) {
    console.error("Error checking system status", err);
  }
}

async function handleExit() {
  if(!confirm("Are you sure you want to stop the system? This will disable all new operations.")) return;
  const res = await postData('/exit', {});
  if (res.success) {
    showToast('error', 'System Stopped', 'The transportation system has been halted.');
    checkSystemStatus();
  }
}

async function handleRestart() {
  const res = await postData('/restart', {});
  if (res.success) {
    showToast('success', 'System Restarted', 'The transportation system is now running.');
    checkSystemStatus();
  }
}

async function updateDashboardStats() {
  try {
    const res = await fetch('/api/statistics');
    const data = await res.json();
    if (data.success && data.data) {
      const s = data.data;
      document.getElementById('stat-routes').innerText = s.total_routes;
      document.getElementById('stat-dests').innerText = s.total_destinations;
      document.getElementById('stat-bookings').innerText = s.total_bookings;
      document.getElementById('stat-revenue').innerText = s.total_revenue.toLocaleString('en-US');
    }
  } catch (e) {
    console.error("Failed to update stats", e);
  }
}

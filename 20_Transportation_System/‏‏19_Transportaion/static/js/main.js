// ===== HERO SLIDER =====
document.addEventListener('DOMContentLoaded', () => {
  const slides = document.querySelectorAll('.hero-slide');
  const indicators = document.querySelectorAll('.hero-indicators button');
  let current = 0;
  let timer;

  function goToSlide(idx) {
    slides.forEach(s => s.classList.remove('active'));
    indicators.forEach(b => b.classList.remove('active'));
    current = idx;
    slides[current].classList.add('active');
    indicators[current].classList.add('active');
  }

  function nextSlide() { goToSlide((current + 1) % slides.length); }

  if (slides.length > 0) {
    timer = setInterval(nextSlide, 5000);
    indicators.forEach((btn, i) => {
      btn.addEventListener('click', () => { clearInterval(timer); goToSlide(i); timer = setInterval(nextSlide, 5000); });
    });
  }

  // ===== NAVBAR SCROLL =====
  const nav = document.querySelector('.navbar');
  if (nav) {
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 50);
    });
  }

  // ===== HAMBURGER =====
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('navLinks');
  if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => navLinks.classList.toggle('open'));
    navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => navLinks.classList.remove('open')));
  }

  // ===== SCROLL ANIMATIONS =====
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.1 });
  document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));

  // ===== LOAD ROUTES =====
  loadRoutes();
  loadRouteSelects();
});

// ===== TOAST SYSTEM =====
function showToast(msg, type = 'info') {
  let container = document.querySelector('.toast-container');
  if (!container) { container = document.createElement('div'); container.className = 'toast-container'; document.body.appendChild(container); }
  const icons = { success: '✅', error: '❌', info: 'ℹ️' };
  const toast = document.createElement('div');
  toast.className = `toast ${type}`;
  toast.innerHTML = `<span class="toast-icon">${icons[type]}</span><span>${msg}</span>`;
  container.appendChild(toast);
  setTimeout(() => { toast.style.opacity = '0'; toast.style.transform = 'translateX(60px)'; setTimeout(() => toast.remove(), 400); }, 4000);
}

// ===== LOAD ROUTES INTO CARDS =====
async function loadRoutes() {
  const grid = document.getElementById('routesGrid');
  if (!grid) return;
  try {
    const res = await fetch('/availableroutes');
    const routes = await res.json();
    grid.innerHTML = '';
    if (routes.length === 0) {
      grid.innerHTML = '<p style="text-align:center;color:var(--text-muted);grid-column:1/-1;">No routes available yet. Add one below!</p>';
      return;
    }
    routes.forEach(r => {
      const total = r.Capacity + r.Booked.length;
      const bookedPct = total > 0 ? (r.Booked.length / total) * 100 : 0;
      const fillClass = bookedPct > 75 ? 'high' : bookedPct > 40 ? 'medium' : 'low';
      const statusClass = r.Capacity > 0 ? 'available' : 'full';
      const statusText = r.Capacity > 0 ? `${r.Capacity} seats left` : 'Fully Booked';
      const card = document.createElement('div');
      card.className = 'route-card fade-up visible';
      card.innerHTML = `
        <div class="route-card-header">
          <span class="route-id">${r.Route_Id}</span>
          <span class="route-status ${statusClass}">
            <span style="width:6px;height:6px;border-radius:50%;background:currentColor;"></span>
            ${statusText}
          </span>
        </div>
        <div class="route-destination">📍 ${r.Destination}</div>
        <div class="route-meta">
          <span class="route-meta-item">🪑 Capacity: ${total}</span>
          <span class="route-meta-item">👥 Booked: ${r.Booked.length}</span>
        </div>
        <div class="capacity-bar"><div class="capacity-fill ${fillClass}" style="width:${bookedPct}%"></div></div>
        <div class="route-card-actions">
          <button class="btn btn-primary btn-sm" onclick="openBookModal('${r.Route_Id}','${r.Destination}')">🎫 Book</button>
          <button class="btn btn-outline btn-sm" onclick="viewPassengers('${r.Route_Id}')">👥 View</button>
        </div>`;
      grid.appendChild(card);
    });
    updateStats(routes);
  } catch (e) { showToast('Failed to load routes', 'error'); }
}

function updateStats(routes) {
  const totalEl = document.getElementById('statRoutes');
  const destEl = document.getElementById('statDestinations');
  const seatsEl = document.getElementById('statSeats');
  if (totalEl) totalEl.textContent = routes.length;
  if (destEl) destEl.textContent = [...new Set(routes.map(r => r.Destination))].length;
  if (seatsEl) seatsEl.textContent = routes.reduce((s, r) => s + r.Capacity, 0);
}

// ===== POPULATE SELECT DROPDOWNS =====
async function loadRouteSelects() {
  try {
    const res = await fetch('/availableroutes');
    const routes = await res.json();
    document.querySelectorAll('.route-select').forEach(sel => {
      const current = sel.value;
      sel.innerHTML = '<option value="">Select a route...</option>';
      routes.forEach(r => {
        sel.innerHTML += `<option value="${r.Route_Id}">${r.Route_Id} — ${r.Destination}</option>`;
      });
      if (current) sel.value = current;
    });
  } catch (e) { /* silent */ }
}

// ===== BOOK TICKET =====
function openBookModal(routeId, dest) {
  const sel = document.getElementById('bookRouteId');
  if (sel) sel.value = routeId;
  const section = document.getElementById('bookingSection');
  if (section) section.scrollIntoView({ behavior: 'smooth', block: 'center' });
  document.getElementById('bookPassenger')?.focus();
}

async function bookTicket() {
  const routeId = document.getElementById('bookRouteId').value;
  const name = document.getElementById('bookPassenger').value.trim();
  if (!routeId || !name) { showToast('Please select a route and enter your name', 'error'); return; }
  try {
    const data = new FormData();
    data.append('route_id', routeId);
    data.append('passenger_name', name);
    const res = await fetch('/bookticket', { method: 'POST', body: data });
    const json = await res.json();
    showToast(json.message, res.ok ? 'success' : 'error');
    document.getElementById('bookPassenger').value = '';
    loadRoutes(); loadRouteSelects();
  } catch (e) { showToast('Booking failed', 'error'); }
}

// ===== CANCEL BOOKING =====
async function cancelBooking() {
  const routeId = document.getElementById('cancelRouteId').value;
  const name = document.getElementById('cancelPassenger').value.trim();
  if (!routeId || !name) { showToast('Please select a route and enter passenger name', 'error'); return; }
  try {
    const data = new FormData();
    data.append('route_id', routeId);
    data.append('passenger_name', name);
    const res = await fetch('/cancelbooking', { method: 'POST', body: data });
    const json = await res.json();
    showToast(json.message, res.ok ? 'success' : 'error');
    document.getElementById('cancelPassenger').value = '';
    loadRoutes(); loadRouteSelects();
  } catch (e) { showToast('Cancellation failed', 'error'); }
}

// ===== ADD ROUTE =====
async function addRoute() {
  const id = document.getElementById('newRouteId').value.trim();
  const dest = document.getElementById('newDest').value.trim();
  const cap = document.getElementById('newCapacity').value;
  if (!id || !dest || !cap) { showToast('Please fill all fields', 'error'); return; }
  try {
    const data = new FormData();
    data.append('route_id', id);
    data.append('destination', dest);
    data.append('capacity', cap);
    const res = await fetch('/addroute', { method: 'POST', body: data });
    const json = await res.json();
    showToast(json.message, res.ok ? 'success' : 'error');
    if (res.ok) {
      document.getElementById('newRouteId').value = '';
      document.getElementById('newDest').value = '';
      document.getElementById('newCapacity').value = '';
    }
    loadRoutes(); loadRouteSelects();
  } catch (e) { showToast('Failed to add route', 'error'); }
}

// ===== SEARCH =====
async function searchRoute() {
  const q = document.getElementById('searchInput').value.trim();
  const box = document.getElementById('searchResults');
  if (!q) { showToast('Enter a Route ID or Destination', 'error'); return; }
  box.innerHTML = '<p style="color:var(--text-muted);">Searching...</p>';
  try {
    // Try route ID first
    let data = new FormData(); data.append('route_id', q);
    let res = await fetch('/searchroute', { method: 'POST', body: data });
    if (res.ok) {
      const r = await res.json();
      const total = r.Capacity + r.Booked.length;
      box.innerHTML = `<div class="result-item"><strong>${r.Route_Id}</strong> → ${r.Destination}</div>
        <div class="result-item">Capacity: ${total} | Available: ${r.Capacity} | Booked: ${r.Booked.length}</div>
        <div class="result-item">Passengers: ${r.Booked.length > 0 ? r.Booked.join(', ') : 'None'}</div>`;
      return;
    }
    // Try destination
    data = new FormData(); data.append('destination', q);
    res = await fetch('/searchroutebydestination', { method: 'POST', body: data });
    if (res.ok) {
      const json = await res.json();
      if (json.routes && json.routes.length > 0) {
        box.innerHTML = json.routes.map(r => {
          const total = r.Capacity + r.Booked.length;
          return `<div class="result-item"><strong>${r.Route_Id}</strong> → ${r.Destination} | Available: ${r.Capacity}/${total}</div>`;
        }).join('');
        return;
      }
    }
    box.innerHTML = '<p style="color:var(--danger);">No results found.</p>';
  } catch (e) { box.innerHTML = '<p style="color:var(--danger);">Search failed.</p>'; }
}

// ===== VIEW PASSENGERS =====
async function viewPassengers(routeId) {
  if (!routeId) {
    const sel = document.getElementById('passengerRouteId');
    if (sel) routeId = sel.value;
  }
  if (!routeId) { showToast('Select a route', 'error'); return; }
  const box = document.getElementById('passengerResults');
  if (!box) return;
  try {
    const data = new FormData(); data.append('route_id', routeId);
    const res = await fetch('/getpassengerlist', { method: 'POST', body: data });
    const json = await res.json();
    const list = json.passenger_list;
    if (Array.isArray(list) && list.length > 0) {
      box.innerHTML = list.map((p, i) => `<div class="result-item">${i + 1}. ${p}</div>`).join('');
    } else {
      box.innerHTML = '<p style="color:var(--text-muted);">No passengers booked on this route yet.</p>';
    }
    const section = document.getElementById('passengerSection');
    if (section) section.scrollIntoView({ behavior: 'smooth', block: 'center' });
    // Update select
    const sel = document.getElementById('passengerRouteId');
    if (sel) sel.value = routeId;
  } catch (e) { showToast('Failed to load passengers', 'error'); }
}

// ===== SMOOTH SCROLL =====
function scrollToSection(id) {
  const el = document.getElementById(id);
  if (el) el.scrollIntoView({ behavior: 'smooth' });
}

// ===== CONTACT FORM =====
function submitContact(e) {
  e.preventDefault();
  showToast('Message sent successfully! We will get back to you soon.', 'success');
  e.target.reset();
}

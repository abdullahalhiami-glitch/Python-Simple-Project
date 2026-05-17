const App = (() => {
    const state = {
        stats: null,
        charts: {},
        routes: []
    };

    const qs = (selector, root = document) => root.querySelector(selector);
    const qsa = (selector, root = document) => [...root.querySelectorAll(selector)];

    function getInitialStats() {
        const node = qs("#initialStats");
        if (!node) return null;
        try {
            return JSON.parse(node.textContent);
        } catch {
            return null;
        }
    }

    function toast(message, type = "success") {
        const stack = qs("#toastStack");
        if (!stack || !window.bootstrap) {
            console[type === "error" ? "error" : "log"](message);
            return;
        }
        const id = `toast-${Date.now()}`;
        const color = type === "error" ? "text-bg-danger" : "text-bg-dark";
        stack.insertAdjacentHTML("beforeend", `
            <div id="${id}" class="toast ${color}" role="status" aria-live="polite" aria-atomic="true">
                <div class="toast-header">
                    <strong class="me-auto">Al-Hiami Transportation</strong>
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                <div class="toast-body">${escapeHtml(message)}</div>
            </div>
        `);
        const el = qs(`#${id}`);
        const instance = new bootstrap.Toast(el, { delay: 4200 });
        instance.show();
        el.addEventListener("hidden.bs.toast", () => el.remove());
    }

    function addNotice(message, type = "online") {
        const list = qs("#notificationList");
        if (!list) return;
        list.insertAdjacentHTML("afterbegin", `
            <article class="notice-item">
                <span class="notice-status ${type}"></span>
                <div>
                    <strong>${escapeHtml(message)}</strong>
                    <p>${new Date().toLocaleTimeString()}</p>
                </div>
            </article>
        `);
    }

    function escapeHtml(value) {
        return String(value ?? "")
            .replaceAll("&", "&amp;")
            .replaceAll("<", "&lt;")
            .replaceAll(">", "&gt;")
            .replaceAll('"', "&quot;")
            .replaceAll("'", "&#039;");
    }

    async function api(endpoint, options = {}) {
        const requestOptions = {
            method: options.method || "GET",
            headers: { "X-Requested-With": "fetch" }
        };
        if (options.body) requestOptions.body = options.body;
        const response = await fetch(endpoint, requestOptions);
        const payload = await response.json().catch(() => ({
            success: false,
            message: "Invalid server response.",
            data: null
        }));
        if (!response.ok || !payload.success) {
            throw payload;
        }
        return payload;
    }

    function setLoading(form, isLoading) {
        const button = qs("button[type='submit']", form);
        if (!button) return;
        button.disabled = isLoading;
        button.classList.toggle("is-loading", isLoading);
    }

    function renderResult(container, payload) {
        if (!container) return;
        container.classList.add("is-visible");
        container.innerHTML = `<pre>${escapeHtml(JSON.stringify(payload, null, 2))}</pre>`;
    }

    function renderRouteCards(routes = [], target = qs("#routeFeed")) {
        if (!target) return;
        if (!routes.length) {
            target.innerHTML = `<article class="swiper-slide route-card"><h3>No routes yet</h3><p>Add a route to start operations.</p></article>`;
            return;
        }
        target.innerHTML = routes.map(route => {
            const booked = route.Booked ? route.Booked.length : route.Booked_Count || 0;
            const total = Number(route.Total_Capacity || route.Capacity || 0);
            const percent = total ? Math.min((booked / total) * 100, 100) : 0;
            return `
                <article class="swiper-slide route-card">
                    <div class="route-card-top">
                        <span>${escapeHtml(route.Route_Id)}</span>
                        <small>${escapeHtml(route.Available_Capacity ?? route.Capacity)} seats open</small>
                    </div>
                    <h3>${escapeHtml(route.Destination)}</h3>
                    <div class="capacity-line"><span style="width:${percent}%"></span></div>
                    <p>${booked} booked of ${total} seats</p>
                    <button class="btn btn-soft w-100" data-route-book="${escapeHtml(route.Route_Id)}">Book ${escapeHtml(route.Route_Id)}</button>
                </article>
            `;
        }).join("");
        initSwiper();
    }

    function renderRouteRows(routes = [], target = qs("#routesTableBody")) {
        if (!target) return;
        if (!routes.length) {
            target.innerHTML = `<tr><td colspan="7">No routes available.</td></tr>`;
            return;
        }
        target.innerHTML = routes.map(route => {
            const booked = route.Booked ? route.Booked.length : route.Booked_Count || 0;
            const price = Number(route.Ticket_Price || 0);
            return `
                <tr>
                    <td>${escapeHtml(route.Route_Id)}</td>
                    <td>${escapeHtml(route.Destination)}</td>
                    <td>${escapeHtml(route.Total_Capacity)}</td>
                    <td>${escapeHtml(route.Available_Capacity ?? route.Capacity)}</td>
                    <td>${booked}</td>
                    <td>${booked * price}</td>
                    <td><button class="btn btn-soft btn-sm" data-route-book="${escapeHtml(route.Route_Id)}">Book</button></td>
                </tr>
            `;
        }).join("");
    }

    function renderDestinations(destinations = [], target = qs("#destinationList")) {
        if (!target) return;
        target.innerHTML = destinations.length
            ? destinations.map(destination => `<span>${escapeHtml(destination)}</span>`).join("")
            : `<span>No destinations</span>`;
    }

    function updateCounters(stats) {
        qsa(".counter").forEach(counter => {
            const key = counter.dataset.stat;
            const value = key && stats[key] !== undefined
                ? stats[key]
                : Number(counter.dataset.count || counter.textContent || 0);
            counter.dataset.count = value;
            animateCounter(counter, value);
        });
    }

    function animateCounter(element, toValue) {
        const target = Number(toValue || 0);
        if (window.gsap) {
            const data = { value: Number(element.textContent) || 0 };
            gsap.to(data, {
                value: target,
                duration: 0.85,
                ease: "power2.out",
                onUpdate: () => {
                    element.textContent = Number.isInteger(target)
                        ? Math.round(data.value)
                        : data.value.toFixed(1);
                }
            });
        } else {
            element.textContent = target;
        }
    }

    function buildCharts(stats) {
        if (!window.Chart || !stats) return;
        const routes = stats.routes || [];
        const labels = routes.map(route => route.Route_Id);
        const revenue = routes.map(route => (route.Booked?.length || 0) * Number(route.Ticket_Price || 0));
        const bookings = routes.map(route => route.Booked?.length || 0);
        const destinations = routes.map(route => route.Destination);

        const chartOptions = {
            responsive: true,
            plugins: { legend: { labels: { color: getTextColor() } } },
            scales: {
                x: { ticks: { color: getMutedColor() }, grid: { color: "rgba(255,255,255,.08)" } },
                y: { ticks: { color: getMutedColor() }, grid: { color: "rgba(255,255,255,.08)" } }
            }
        };

        createOrUpdateChart("homeRevenueChart", {
            type: "line",
            data: {
                labels,
                datasets: [
                    { label: "Revenue", data: revenue, borderColor: "#27d5ff", backgroundColor: "rgba(39,213,255,.18)", tension: 0.35, fill: true },
                    { label: "Bookings", data: bookings, borderColor: "#3be29a", backgroundColor: "rgba(59,226,154,.12)", tension: 0.35 }
                ]
            },
            options: chartOptions
        });

        createOrUpdateChart("revenueChart", {
            type: "bar",
            data: {
                labels,
                datasets: [{ label: "Revenue by route", data: revenue, backgroundColor: ["#2f7cff", "#27d5ff", "#3be29a", "#ffd166", "#ff5c7a"] }]
            },
            options: chartOptions
        });

        createOrUpdateChart("destinationChart", {
            type: "doughnut",
            data: {
                labels: destinations,
                datasets: [{ label: "Bookings", data: bookings, backgroundColor: ["#2f7cff", "#27d5ff", "#3be29a", "#ffd166", "#ff5c7a"] }]
            },
            options: { responsive: true, plugins: { legend: { labels: { color: getTextColor() } } } }
        });
    }

    function createOrUpdateChart(canvasId, config) {
        const canvas = qs(`#${canvasId}`);
        if (!canvas) return;
        if (state.charts[canvasId]) state.charts[canvasId].destroy();
        state.charts[canvasId] = new Chart(canvas, config);
    }

    function getTextColor() {
        return getComputedStyle(document.documentElement).getPropertyValue("--text").trim();
    }

    function getMutedColor() {
        return getComputedStyle(document.documentElement).getPropertyValue("--muted").trim();
    }

    async function refreshStats(silent = false) {
        try {
            const payload = await api("/systemstatistics");
            state.stats = payload.data;
            state.routes = payload.data.routes || [];
            renderRouteCards(state.routes.filter(route => Number(route.Available_Capacity) > 0));
            renderRouteRows(state.routes);
            renderDestinations(payload.data.destinations || []);
            updateCounters(payload.data);
            buildCharts(payload.data);
            if (!silent) toast("Dashboard refreshed.");
        } catch (err) {
            toast(err.message || "Unable to refresh statistics.", "error");
        }
    }

    async function refreshStatus() {
        try {
            const payload = await api("/status");
            const running = payload.data.running;
            const text = running ? "Running" : "Exited";
            qsa("#footerStatus, #dashboardStatus, #heroStatus").forEach(node => {
                if (node) node.textContent = text;
            });
            qsa(".status-pulse").forEach(node => node.classList.toggle("offline", !running));
        } catch {
            qsa(".status-pulse").forEach(node => node.classList.add("offline"));
        }
    }

    function attachForms() {
        qsa(".ajax-form").forEach(form => {
            form.addEventListener("submit", async event => {
                event.preventDefault();
                setLoading(form, true);
                const result = qs("[data-result]", form);
                try {
                    const payload = await api(form.dataset.endpoint, {
                        method: "POST",
                        body: new FormData(form)
                    });
                    renderResult(result, payload);
                    toast(payload.message || "Request completed.");
                    addNotice(payload.message || "Request completed.", "online");
                    if (form.dataset.refresh === "true") {
                        await refreshStats(true);
                        await refreshStatus();
                    }
                } catch (err) {
                    renderResult(result, err);
                    toast(err.message || "Request failed.", "error");
                    addNotice(err.message || "Request failed.", "error");
                } finally {
                    setLoading(form, false);
                }
            });
        });
    }

    function attachActionButtons() {
        document.addEventListener("click", async event => {
            const bookButton = event.target.closest("[data-route-book]");
            if (bookButton) {
                const routeId = bookButton.dataset.routeBook;
                const input = qs("#modalBook-route_id");
                if (input) input.value = routeId;
                if (window.bootstrap) bootstrap.Modal.getOrCreateInstance(qs("#modalBook")).show();
                return;
            }

            const getButton = event.target.closest("[data-get]");
            if (getButton) {
                await handleButtonRequest(getButton, "GET", getButton.dataset.get);
                return;
            }

            const postButton = event.target.closest("[data-post]");
            if (postButton) {
                await handleButtonRequest(postButton, "POST", postButton.dataset.post);
            }
        });
    }

    async function handleButtonRequest(button, method, endpoint) {
        const originalText = button.innerHTML;
        button.disabled = true;
        button.innerHTML = "Loading...";
        const result = qs("#systemResult");
        try {
            const payload = await api(endpoint, { method });
            const target = button.dataset.renderTarget ? qs(button.dataset.renderTarget) : null;
            renderTarget(target, payload);
            renderResult(result, payload);
            toast(payload.message || "Request completed.");
            addNotice(payload.message || "Request completed.", "online");
            if (button.dataset.refresh === "true" || endpoint === "/systemstatistics") {
                await refreshStats(true);
                await refreshStatus();
            }
        } catch (err) {
            renderResult(result, err);
            toast(err.message || "Request failed.", "error");
            addNotice(err.message || "Request failed.", "error");
        } finally {
            button.disabled = false;
            button.innerHTML = originalText;
            if (window.lucide) lucide.createIcons();
        }
    }

    function renderTarget(target, payload) {
        if (!target) return;
        if (target.id === "routeFeed") {
            renderRouteCards(payload.data || [], target);
        } else if (target.id === "routesTableBody") {
            renderRouteRows(payload.data || [], target);
        } else if (target.id === "destinationList") {
            renderDestinations(payload.data || [], target);
        } else if (target.id === "dashboardRoot") {
            refreshStats(true);
        } else {
            target.textContent = JSON.stringify(payload.data, null, 2);
        }
    }

    function attachSearch() {
        const search = qs("#routeTableSearch");
        if (!search) return;
        search.addEventListener("input", () => {
            const term = search.value.trim().toLowerCase();
            const filtered = (state.routes || []).filter(route =>
                route.Route_Id.toLowerCase().includes(term) ||
                route.Destination.toLowerCase().includes(term)
            );
            renderRouteRows(filtered);
        });
    }

    function attachContactForm() {
        const form = qs("#contactForm");
        if (!form) return;
        form.addEventListener("submit", event => {
            event.preventDefault();
            toast("Message prepared for dispatch. Contact form mockup completed.");
            addNotice("Contact request captured.", "online");
            form.reset();
        });
    }

    function initTheme() {
        const saved = localStorage.getItem("alhiami-theme");
        if (saved) document.documentElement.dataset.theme = saved;
        const toggle = qs("#themeToggle");
        if (!toggle) return;
        toggle.addEventListener("click", () => {
            const next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
            document.documentElement.dataset.theme = next;
            localStorage.setItem("alhiami-theme", next);
            buildCharts(state.stats);
            if (window.lucide) lucide.createIcons();
        });
    }

    function initSwiper() {
        if (!window.Swiper || !qs(".route-swiper")) return;
        if (state.routeSwiper) state.routeSwiper.destroy(true, true);
        state.routeSwiper = new Swiper(".route-swiper", {
            slidesPerView: 1,
            spaceBetween: 16,
            pagination: { el: ".swiper-pagination", clickable: true },
            breakpoints: {
                720: { slidesPerView: 2 },
                1100: { slidesPerView: 3 }
            }
        });
    }

    function initMotion() {
        if (window.AOS) AOS.init({ duration: 700, once: true, offset: 80 });
        if (window.gsap) {
            gsap.from(".app-navbar", { y: -24, opacity: 0, duration: 0.7, ease: "power2.out" });
            gsap.from(".hero-section h1", { y: 28, opacity: 0, duration: 0.85, delay: 0.15, ease: "power3.out" });
        }
        qsa(".counter").forEach(counter => animateCounter(counter, Number(counter.dataset.count || 0)));
    }

    function hideLoader() {
        const loader = qs("#appLoader");
        if (!loader) return;
        setTimeout(() => loader.classList.add("is-hidden"), 450);
    }

    function init() {
        state.stats = getInitialStats();
        if (state.stats) {
            state.routes = state.stats.routes || [];
            buildCharts(state.stats);
        }
        initTheme();
        attachForms();
        attachActionButtons();
        attachSearch();
        attachContactForm();
        initSwiper();
        initMotion();
        refreshStatus();
        setInterval(refreshStatus, 12000);
        if (window.lucide) lucide.createIcons();
        hideLoader();
    }

    return { init, refreshStats };
})();

document.addEventListener("DOMContentLoaded", App.init);

document.addEventListener('DOMContentLoaded', () => {
    // Smooth Scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Dashboard Tabs Logic
    const actionBtns = document.querySelectorAll('.action-btn');
    const panes = document.querySelectorAll('.pane');

    actionBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all
            actionBtns.forEach(b => b.classList.remove('active'));
            panes.forEach(p => p.classList.remove('active'));

            // Add active class to clicked
            btn.classList.add('active');
            const targetId = btn.getAttribute('data-target');
            document.getElementById(targetId).classList.add('active');
        });
    });

    // Helper: Show Feedback Message
    const showFeedback = (elementId, message, isSuccess) => {
        const el = document.getElementById(elementId);
        el.textContent = message;
        el.className = `form-feedback ${isSuccess ? 'success' : 'error'}`;
        
        // Auto hide after 5 seconds
        setTimeout(() => {
            el.style.display = 'none';
            el.className = 'form-feedback';
        }, 5000);
    };

    // Load Available Routes
    const loadRoutesBtn = document.getElementById('loadRoutesBtn');
    const routesGrid = document.getElementById('routesGrid');

    if (loadRoutesBtn) {
        loadRoutesBtn.addEventListener('click', async () => {
            loadRoutesBtn.textContent = 'Loading...';
            try {
                const response = await fetch('/availableroutes');
                const data = await response.json();
                
                routesGrid.innerHTML = ''; // Clear existing
                
                if (data.length === 0) {
                    routesGrid.innerHTML = '<div class="placeholder-text">No routes currently available.</div>';
                } else {
                    data.forEach(route => {
                        const card = document.createElement('div');
                        card.className = 'route-card';
                        card.innerHTML = `
                            <div class="route-card-id">${route.Route_Id}</div>
                            <div class="route-card-dest">${route.Destination}</div>
                            <div class="route-card-seats">Available Seats: <strong>${route.Capacity}</strong></div>
                        `;
                        routesGrid.appendChild(card);
                    });
                }
            } catch (err) {
                routesGrid.innerHTML = '<div class="placeholder-text" style="color:var(--danger)">Error loading routes. Make sure the server is running.</div>';
            }
            loadRoutesBtn.textContent = 'Refresh Routes';
        });
    }

    // Search Route Logic
    const searchForm = document.getElementById('searchForm');
    const searchResults = document.getElementById('searchResults');

    if (searchForm) {
        searchForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const dest = document.getElementById('searchDest').value;
            const formData = new FormData();
            formData.append('destination', dest);

            try {
                const response = await fetch('/searchroutebydestination', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();
                
                searchResults.innerHTML = '';
                
                if (data.routes && data.routes.length > 0) {
                    const grid = document.createElement('div');
                    grid.className = 'routes-grid';
                    data.routes.forEach(route => {
                        grid.innerHTML += `
                            <div class="route-card">
                                <div class="route-card-id">${route.Route_Id}</div>
                                <div class="route-card-dest">${route.Destination}</div>
                                <div class="route-card-seats">Capacity: ${route.Capacity}</div>
                            </div>
                        `;
                    });
                    searchResults.appendChild(grid);
                } else {
                    searchResults.innerHTML = `<div class="form-feedback error">No routes found for destination "${dest}".</div>`;
                }
            } catch (err) {
                searchResults.innerHTML = `<div class="form-feedback error">Error searching for route.</div>`;
            }
        });
    }

    // Book Ticket Logic
    const bookForm = document.getElementById('bookForm');
    if (bookForm) {
        bookForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const routeId = document.getElementById('bookRouteId').value;
            const passengerName = document.getElementById('passengerName').value;
            
            const formData = new FormData();
            formData.append('route_id', routeId);
            formData.append('passenger_name', passengerName);

            try {
                const response = await fetch('/bookticket', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();
                
                if (response.ok && data.message && !data.message.toLowerCase().includes('error') && !data.message.toLowerCase().includes('not found') && !data.message.toLowerCase().includes('already')) {
                     showFeedback('bookResult', data.message, true);
                     bookForm.reset();
                     // Trigger refresh of routes if open
                     if (document.getElementById('view-routes').classList.contains('active')) {
                         loadRoutesBtn.click();
                     }
                } else {
                     showFeedback('bookResult', data.message || "Booking failed", false);
                }
            } catch (err) {
                showFeedback('bookResult', "Connection error", false);
            }
        });
    }

    // Cancel Ticket Logic
    const cancelForm = document.getElementById('cancelForm');
    if (cancelForm) {
        cancelForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const routeId = document.getElementById('cancelRouteId').value;
            const passengerName = document.getElementById('cancelPassengerName').value;
            
            const formData = new FormData();
            formData.append('route_id', routeId);
            formData.append('passenger_name', passengerName);

            try {
                const response = await fetch('/cancelbooking', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();
                
                if (response.ok && data.message && !data.message.toLowerCase().includes('not found') && !data.message.toLowerCase().includes('no booking')) {
                     showFeedback('cancelResult', data.message, true);
                     cancelForm.reset();
                     // Trigger refresh of routes if open
                     if (document.getElementById('view-routes').classList.contains('active')) {
                         loadRoutesBtn.click();
                     }
                } else {
                     showFeedback('cancelResult', data.message || "Cancellation failed", false);
                }
            } catch (err) {
                showFeedback('cancelResult', "Connection error", false);
            }
        });
    }
});

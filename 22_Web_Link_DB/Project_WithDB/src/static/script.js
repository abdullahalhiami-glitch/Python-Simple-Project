const API_BASE = '';

// DOM Elements
const restaurantGrid = document.getElementById('restaurantGrid');
const searchInput = document.getElementById('searchInput');
const topRatedInput = document.getElementById('topRatedInput');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    fetchAllRestaurants();
    setupStarRating();
});

// Toast Notification
function showToast(message, type = 'success') {
    const container = document.getElementById('toastContainer');
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    
    const icon = type === 'success' ? 'ri-checkbox-circle-fill' : 'ri-error-warning-fill';
    const color = type === 'success' ? 'var(--success)' : 'var(--danger)';
    
    toast.innerHTML = `<i class="${icon}" style="color: ${color}; font-size: 1.25rem;"></i><span>${message}</span>`;
    
    container.appendChild(toast);
    
    // Animate in
    setTimeout(() => toast.classList.add('show'), 10);
    
    // Remove after 3s
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// Modals
function openModal(id) {
    document.getElementById(id).classList.add('active');
}

function closeModal(id) {
    document.getElementById(id).classList.remove('active');
    
    // Reset specific inputs
    if(id === 'addRestaurantModal') {
        document.getElementById('addName').value = '';
        document.getElementById('addCuisine').value = '';
    } else if(id === 'addRatingModal') {
        document.getElementById('ratingValue').value = '0';
        document.querySelectorAll('.star-rating i').forEach(s => {
            s.classList.replace('ri-star-fill', 'ri-star-line');
            s.classList.remove('active');
        });
    } else if(id === 'updateCuisineModal') {
        document.getElementById('updateCuisineInput').value = '';
    }
}

// Close modals on outside click
document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', (e) => {
        if(e.target === overlay) {
            closeModal(overlay.id);
        }
    });
});

// Star Rating Setup
function setupStarRating() {
    const stars = document.querySelectorAll('.star-rating i');
    const ratingInput = document.getElementById('ratingValue');
    // Using simple approach since direction might affect index
    stars.forEach((star, index) => {
        star.addEventListener('click', function() {
            const val = this.getAttribute('data-value');
            ratingInput.value = val;
            
            stars.forEach(s => {
                s.classList.remove('active');
                s.classList.replace('ri-star-fill', 'ri-star-line');
            });
            
            for(let i=0; i<val; i++) {
                stars[i].classList.add('active');
                stars[i].classList.replace('ri-star-line', 'ri-star-fill');
            }
        });

        star.addEventListener('mouseover', function() {
            const val = this.getAttribute('data-value');
            stars.forEach((s, i) => {
                if(i < val) {
                    s.classList.replace('ri-star-line', 'ri-star-fill');
                } else {
                    if(!s.classList.contains('active')) {
                        s.classList.replace('ri-star-fill', 'ri-star-line');
                    }
                }
            });
        });

        star.parentElement.addEventListener('mouseleave', function() {
            const val = ratingInput.value;
            stars.forEach((s, i) => {
                if(i < val) {
                    s.classList.replace('ri-star-line', 'ri-star-fill');
                } else {
                    s.classList.replace('ri-star-fill', 'ri-star-line');
                }
            });
        });
    });
}

// API Calls
async function fetchAllRestaurants() {
    try {
        const response = await fetch(`${API_BASE}/restaurants`);
        const data = await response.json();
        renderRestaurants(data.result);
    } catch (error) {
        showToast('فشل في تحميل المطاعم', 'error');
    }
}

async function handleSearch(event) {
    if (event.key === 'Enter') {
        const cuisine = searchInput.value.trim();
        if(!cuisine) {
            fetchAllRestaurants();
            return;
        }
        
        try {
            const response = await fetch(`${API_BASE}/restaurants/search?cuisine=${encodeURIComponent(cuisine)}`);
            const data = await response.json();
            if(data.error) throw new Error(data.error);
            renderRestaurants(data.result);
        } catch (error) {
            showToast(error.message || 'فشل في البحث', 'error');
        }
    }
}

async function fetchTopRated() {
    const minRating = topRatedInput.value;
    if(!minRating) return;

    try {
        const response = await fetch(`${API_BASE}/restaurants/top?min_rating=${minRating}`);
        const data = await response.json();
        if(data.error) throw new Error(data.error);
        renderRestaurants(data.result);
    } catch (error) {
        showToast(error.message || 'فشل في التصفية', 'error');
    }
}

async function submitAddRestaurant() {
    const name = document.getElementById('addName').value.trim();
    const cuisine = document.getElementById('addCuisine').value.trim();

    if(!name || !cuisine) {
        showToast('الرجاء تعبئة جميع الحقول', 'error');
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/restaurants`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, cuisine })
        });
        const data = await response.json();
        
        if(data.error) throw new Error(data.error);
        
        showToast(data.result);
        closeModal('addRestaurantModal');
        fetchAllRestaurants();
    } catch (error) {
        showToast(error.message || 'فشل في الإضافة', 'error');
    }
}

async function deleteRestaurant(name) {
    if(!confirm(`هل أنت متأكد من حذف ${name}؟`)) return;

    try {
        const response = await fetch(`${API_BASE}/restaurants/${encodeURIComponent(name)}`, {
            method: 'DELETE'
        });
        const data = await response.json();
        if(data.error) throw new Error(data.error);
        
        showToast(data.result);
        fetchAllRestaurants();
    } catch (error) {
        showToast(error.message || 'فشل في الحذف', 'error');
    }
}

function openUpdateModal(name, currentCuisine) {
    document.getElementById('updateRestaurantName').value = name;
    document.getElementById('updateCuisineInput').value = currentCuisine;
    openModal('updateCuisineModal');
}

async function submitUpdateCuisine() {
    const name = document.getElementById('updateRestaurantName').value;
    const cuisine = document.getElementById('updateCuisineInput').value.trim();

    if(!cuisine) {
        showToast('نوع الطعام لا يمكن أن يكون فارغاً', 'error');
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/restaurants/${encodeURIComponent(name)}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cuisine })
        });
        const data = await response.json();
        
        if(data.error) throw new Error(data.error);
        
        showToast(data.result);
        closeModal('updateCuisineModal');
        fetchAllRestaurants();
    } catch (error) {
        showToast(error.message || 'فشل في التحديث', 'error');
    }
}

function openRatingModal(name) {
    document.getElementById('ratingRestaurantName').value = name;
    openModal('addRatingModal');
}

async function submitRating() {
    const name = document.getElementById('ratingRestaurantName').value;
    const rating = parseFloat(document.getElementById('ratingValue').value);

    if(!rating || rating === 0) {
        showToast('الرجاء اختيار تقييم', 'error');
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/restaurants/${encodeURIComponent(name)}/rating`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ rating })
        });
        const data = await response.json();
        
        if(data.error) throw new Error(data.error);
        
        showToast(data.result);
        closeModal('addRatingModal');
        fetchAllRestaurants();
    } catch (error) {
        showToast(error.message || 'فشل في تقييم المطعم', 'error');
    }
}

async function viewInfo(name) {
    try {
        const response = await fetch(`${API_BASE}/restaurants/${encodeURIComponent(name)}`);
        const data = await response.json();
        
        if(data.error) throw new Error(data.error);
        
        let infoStr = data.result; // Expected string e.g. "Cuisine: xyz, Ratings: [1, 2]"
        
        const avgResp = await fetch(`${API_BASE}/restaurants/${encodeURIComponent(name)}/average`);
        const avgData = await avgResp.json();
        let avgRatingStr = (typeof avgData.result === 'number') ? avgData.result : avgData.result;

        document.getElementById('infoTitle').textContent = name;
        document.getElementById('infoBody').innerHTML = `
            <div class="info-details">
                <p style="margin-bottom: 1rem; line-height: 1.5" dir="ltr">${infoStr}</p>
                <p><strong>متوسط التقييم:</strong> ${avgRatingStr}</p>
            </div>
        `;
        
        openModal('infoModal');
    } catch (error) {
        showToast(error.message || 'فشل في جلب البيانات', 'error');
    }
}

// Render Data
function renderRestaurants(data) {
    restaurantGrid.innerHTML = '';
    
    let items = [];
    if (typeof data === 'string') {
        // e.g. "No restaurants found..."
        restaurantGrid.innerHTML = `
            <div class="empty-state">
                <i class="ri-error-warning-line"></i>
                <h3>ملاحظة</h3>
                <p>${data}</p>
            </div>
        `;
        return;
    }

    if (Array.isArray(data)) {
        // data could be from search: ["Name1", "Name2"]
        // or top rated: [["Name1", 4.5], ["Name2", 4.0]]
        items = data.map(item => {
            if (Array.isArray(item)) {
                return { name: item[0], avgRating: item[1] };
            } else if (typeof item === 'string') {
                return { name: item };
            }
            return item;
        });
    } else if (typeof data === 'object') {
        // from get_all_restaurants: {"Name": {"cuisine": "x", "ratings": []}}
        items = Object.keys(data).map(key => ({
            name: key,
            cuisine: data[key].cuisine,
            ratings: data[key].ratings
        }));
    }

    if (items.length === 0) {
        restaurantGrid.innerHTML = `
            <div class="empty-state">
                <i class="ri-restaurant-line"></i>
                <h3>لا توجد مطاعم</h3>
                <p>جرب البحث بكلمة أخرى أو أضف مطعماً جديداً.</p>
            </div>
        `;
        return;
    }

    items.forEach(async (rest) => {
        let name = rest.name;
        let cuisine = rest.cuisine || 'غير محدد'; // Because search/top return different data shape
        let avgRating = rest.avgRating !== undefined ? rest.avgRating : '-';
        
        const card = document.createElement('div');
        card.className = 'restaurant-card';
        
        // Fetch average rating if not available
        if (avgRating === '-') {
            try {
                const avgResp = await fetch(`${API_BASE}/restaurants/${encodeURIComponent(name)}/average`);
                const avgData = await avgResp.json();
                if (typeof avgData.result === 'number') {
                    avgRating = avgData.result;
                }
            } catch(e) {}
        }
        
        // Fetch cuisine info if not available
        if (cuisine === 'غير محدد') {
            try {
                const infoResp = await fetch(`${API_BASE}/restaurants/${encodeURIComponent(name)}`);
                const infoData = await infoResp.json();
                if (typeof infoData.result === 'string') {
                    const match = infoData.result.match(/Cuisine:\s*([^,]+)/);
                    if (match) cuisine = match[1];
                }
            } catch(e) {}
        }

        // Escape string quotes for inline handlers
        const safeName = name.replace(/'/g, "\\'");
        const safeCuisine = cuisine.replace(/'/g, "\\'");

        card.innerHTML = `
            <div class="card-header" onclick="viewInfo('${safeName}')" style="cursor: pointer;">
                <div>
                    <h3 class="card-title">${name}</h3>
                    <span class="card-cuisine">${cuisine}</span>
                </div>
                <div class="card-rating">
                    <i class="ri-star-fill"></i> <span style="margin-right: 4px;">${avgRating}</span>
                </div>
            </div>
            <div class="card-actions" onclick="event.stopPropagation()">
                <button class="icon-btn" title="إضافة تقييم" onclick="openRatingModal('${safeName}')">
                    <i class="ri-star-line"></i>
                </button>
                <button class="icon-btn" title="تحديث نوع الطعام" onclick="openUpdateModal('${safeName}', '${safeCuisine}')">
                    <i class="ri-edit-line"></i>
                </button>
                <button class="icon-btn danger" title="حذف المطعم" onclick="deleteRestaurant('${safeName}')">
                    <i class="ri-delete-bin-line"></i>
                </button>
            </div>
        `;
        
        restaurantGrid.appendChild(card);
    });
}

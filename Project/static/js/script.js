// --- Hero Slider Animation ---
const slides = document.querySelectorAll('.slide');
let currentSlide = 0;

function nextSlide() {
    slides[currentSlide].classList.remove('active');
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add('active');
}
setInterval(nextSlide, 5000);

// --- Navbar Scroll Effect ---
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
        document.querySelectorAll('.navbar .nav-links a').forEach(a => a.style.color = '#fff');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// --- API Interactions ---
const API_BASE = '/restaurants';

// Fetch and display all restaurants on load
document.addEventListener('DOMContentLoaded', loadAllRestaurants);

async function loadAllRestaurants() {
    try {
        const response = await fetch(API_BASE);
        const data = await response.json();
        if (data.result) {
            renderRestaurants(data.result);
        } else {
            showToast('خطأ في تحميل البيانات', 'error');
        }
    } catch (err) {
        showToast('خطأ في الاتصال بالخادم', 'error');
    }
}

function renderRestaurants(restaurantsStr) {
    const grid = document.getElementById('restaurantsGrid');
    grid.innerHTML = '';
    
    if (typeof restaurantsStr === 'string' && !restaurantsStr.startsWith('{') && !restaurantsStr.startsWith('[')) {
        // If it's a raw string like python print output
        grid.innerHTML = `<div class="restaurant-card" style="grid-column: 1 / -1;"><div class="card-content"><p>${restaurantsStr}</p></div></div>`;
        return;
    }

    let resObj = restaurantsStr;
    try {
        if (typeof restaurantsStr === 'string') {
            // Replace single quotes with double quotes just in case it's stringified python dict
            resObj = JSON.parse(restaurantsStr.replace(/'/g, '"'));
        }
    } catch (e) {
        // Could not parse
    }

    let entries = [];
    if (Array.isArray(resObj)) {
        entries = resObj;
    } else if (typeof resObj === 'object') {
        entries = Object.keys(resObj).map(key => {
            return {
                name: key,
                cuisine: resObj[key].cuisine || resObj[key], // fallback
                ...resObj[key]
            }
        });
    }

    if (entries.length === 0) {
        grid.innerHTML = `<div class="restaurant-card" style="grid-column: 1 / -1; text-align: center;"><div class="card-content"><h3>لا توجد مطاعم حالياً</h3></div></div>`;
        return;
    }

    entries.forEach(async (rest) => {
        // Fetch average rating if not provided
        let avgRating = '-';
        try {
            const avgRes = await fetch(`${API_BASE}/${rest.name}/average`);
            const avgData = await avgRes.json();
            if(avgData.result && typeof avgData.result === 'number') {
                avgRating = avgData.result.toFixed(1);
            } else if(typeof avgData.result === 'string') {
                const match = avgData.result.match(/\d+(\.\d+)?/);
                if (match) avgRating = parseFloat(match[0]).toFixed(1);
            }
        } catch(e) {}

        const card = document.createElement('div');
        card.className = 'restaurant-card';
        card.innerHTML = `
            <div class="card-img-placeholder">
                <i class="fa-solid fa-utensils"></i>
            </div>
            <div class="card-content">
                <h3 class="card-title">
                    ${rest.name}
                    <span class="rating-badge"><i class="fa-solid fa-star"></i> ${avgRating}</span>
                </h3>
                <p class="card-cuisine"><i class="fa-solid fa-bowl-food"></i> المطبخ: ${rest.cuisine}</p>
                <div class="card-actions">
                    <button class="btn btn-small btn-info" onclick="viewInfo('${rest.name}')"><i class="fa-solid fa-circle-info"></i> تفاصيل</button>
                    <button class="btn btn-small btn-warning" onclick="openRatingModal('${rest.name}')"><i class="fa-solid fa-star"></i> تقييم</button>
                    <button class="btn btn-small btn-primary" onclick="openUpdateModal('${rest.name}', '${rest.cuisine}')"><i class="fa-solid fa-pen"></i> تعديل</button>
                    <button class="btn btn-small btn-danger" onclick="deleteRestaurant('${rest.name}')"><i class="fa-solid fa-trash"></i> حذف</button>
                </div>
            </div>
        `;
        grid.appendChild(card);
    });
}

// Search
async function searchRestaurants() {
    const cuisine = document.getElementById('searchCuisine').value.trim();
    if (!cuisine) return loadAllRestaurants();
    
    try {
        const response = await fetch(`${API_BASE}/search?cuisine=${cuisine}`);
        const data = await response.json();
        if (data.result) {
            renderRestaurants(data.result);
        } else {
            showToast('لم يتم العثور على نتائج', 'error');
        }
    } catch (err) {
        showToast('خطأ في البحث', 'error');
    }
}

// Filter
async function filterTopRated() {
    const minRating = document.getElementById('minRating').value || 1;
    try {
        const response = await fetch(`${API_BASE}/top?min_rating=${minRating}`);
        const data = await response.json();
        if (data.result) {
            renderRestaurants(data.result);
        } else {
            showToast('لا توجد مطاعم بهذا التقييم', 'error');
        }
    } catch (err) {
        showToast('خطأ في الفلترة', 'error');
    }
}

// View Info
async function viewInfo(name) {
    try {
        const response = await fetch(`${API_BASE}/${name}`);
        const data = await response.json();
        if (data.result) {
            let info = typeof data.result === 'object' ? JSON.stringify(data.result, null, 2) : data.result;
            alert(`تفاصيل ${name}:\n${info}`);
        }
    } catch (err) {
        showToast('خطأ في جلب التفاصيل', 'error');
    }
}

// Add Restaurant
async function addRestaurant(e) {
    e.preventDefault();
    const name = document.getElementById('addName').value;
    const cuisine = document.getElementById('addCuisine').value;
    
    try {
        const response = await fetch(API_BASE, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, cuisine })
        });
        const data = await response.json();
        if (response.ok) {
            showToast('تمت إضافة المطعم بنجاح', 'success');
            closeModal('addRestaurantModal');
            document.getElementById('addRestaurantForm').reset();
            loadAllRestaurants();
        } else {
            showToast(data.error || 'حدث خطأ', 'error');
        }
    } catch (err) {
        showToast('خطأ في الاتصال', 'error');
    }
}

// Add Rating
function openRatingModal(name) {
    document.getElementById('ratingRestaurantName').textContent = name;
    document.getElementById('ratingNameInput').value = name;
    openModal('addRatingModal');
}

async function addRating(e) {
    e.preventDefault();
    const name = document.getElementById('ratingNameInput').value;
    const rating = parseFloat(document.getElementById('ratingValue').value);
    
    try {
        const response = await fetch(`${API_BASE}/${name}/rating`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ rating })
        });
        const data = await response.json();
        if (response.ok) {
            showToast('تم إضافة التقييم بنجاح', 'success');
            closeModal('addRatingModal');
            document.getElementById('addRatingForm').reset();
            loadAllRestaurants(); 
        } else {
            showToast(data.error || 'حدث خطأ', 'error');
        }
    } catch (err) {
        showToast('خطأ في الاتصال', 'error');
    }
}

// Update Cuisine
function openUpdateModal(name, currentCuisine) {
    document.getElementById('updateRestaurantName').textContent = name;
    document.getElementById('updateNameInput').value = name;
    document.getElementById('newCuisineValue').value = currentCuisine;
    openModal('updateCuisineModal');
}

async function updateCuisine(e) {
    e.preventDefault();
    const name = document.getElementById('updateNameInput').value;
    const cuisine = document.getElementById('newCuisineValue').value;
    
    try {
        const response = await fetch(`${API_BASE}/${name}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cuisine })
        });
        const data = await response.json();
        if (response.ok) {
            showToast('تم تحديث المطبخ بنجاح', 'success');
            closeModal('updateCuisineModal');
            loadAllRestaurants();
        } else {
            showToast(data.error || 'حدث خطأ', 'error');
        }
    } catch (err) {
        showToast('خطأ في الاتصال', 'error');
    }
}

// Delete
async function deleteRestaurant(name) {
    if (!confirm(`هل أنت متأكد من حذف مطعم ${name}؟`)) return;
    
    try {
        const response = await fetch(`${API_BASE}/${name}`, {
            method: 'DELETE'
        });
        const data = await response.json();
        if (response.ok) {
            showToast('تم الحذف بنجاح', 'success');
            loadAllRestaurants();
        } else {
            showToast(data.error || 'حدث خطأ', 'error');
        }
    } catch (err) {
        showToast('خطأ في الاتصال', 'error');
    }
}

// Modals Management
function openModal(id) { document.getElementById(id).style.display = 'block'; }
function closeModal(id) { document.getElementById(id).style.display = 'none'; }
window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = 'none';
    }
}

// Toast
function showToast(message, type = 'success') {
    const toast = document.getElementById('toast');
    toast.innerHTML = type === 'success' 
        ? `<i class="fa-solid fa-check-circle"></i> ${message}`
        : `<i class="fa-solid fa-circle-exclamation"></i> ${message}`;
    toast.className = `toast show ${type}`;
    setTimeout(() => { toast.classList.remove('show'); }, 3000);
}

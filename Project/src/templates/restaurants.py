# restaurants.py

# قاموس لتخزين بيانات المطاعم
directory = {}

def add_restaurant(name, cuisine_type):
    """إضافة مطعم جديد"""
    if name in directory:
        return f"Restaurant '{name}' already exists."
    directory[name] = {"cuisine": cuisine_type, "ratings": []}
    return f"Restaurant '{name}' added successfully."

def add_rating(name, rating_value):
    """إضافة تقييم جديد للقائمة"""
    if name not in directory:
        return f"Restaurant '{name}' not found."
    try:
        rating_value = float(rating_value)
        if not (0 <= rating_value <= 5):
            return "Rating must be between 0 and 5."
        directory[name]["ratings"].append(rating_value)
        return f"Rating added to restaurant '{name}' successfully."
    except ValueError:
        return "Invalid rating value."

def get_restaurant_info(name):
    """عرض نوع المطعم وتقييماته"""
    if name not in directory:
        return f"Restaurant '{name}' not found."
    info = directory[name]
    return f"Cuisine: {info['cuisine']}, Ratings: {info['ratings']}"

def calculate_average_rating(name):
    """تُرجع متوسط تقييم المطعم من 5"""
    if name not in directory:
        return f"Restaurant '{name}' not found."
    ratings = directory[name]["ratings"]
    if not ratings:
        return "No ratings for this restaurant yet."
    avg = sum(ratings) / len(ratings)
    return round(avg, 2)

def search_by_cuisine(cuisine_type):
    """تُرجع المطاعم من فئة معينة"""
    found = [name for name, info in directory.items() if info["cuisine"].lower() == cuisine_type.lower()]
    if not found:
        return f"No restaurants found for cuisine '{cuisine_type}'."
    return found

def get_top_rated_restaurants(min_rating):
    """تُرجع المطاعم التي متوسطها أعلى من رقم محدد"""
    try:
        min_rating = float(min_rating)
    except ValueError:
        return "Invalid rating value."
    
    top_rated = []
    for name in directory:
        avg = calculate_average_rating(name)
        if isinstance(avg, (int, float)) and avg >= min_rating:
            top_rated.append((name, avg))
            
    if not top_rated:
        return f"No restaurants found with average rating >= {min_rating}."
    return top_rated

def update_restaurant_cuisine(name, new_cuisine):
    """تعديل نوع المطعم"""
    if name not in directory:
        return f"Restaurant '{name}' not found."
    directory[name]["cuisine"] = new_cuisine
    return f"Restaurant '{name}' cuisine updated to '{new_cuisine}' successfully."

def delete_restaurant(name):
    """شطب المطعم من الدليل"""
    if name in directory:
        del directory[name]
        return f"Restaurant '{name}' deleted successfully."
    return f"Restaurant '{name}' not found."

def get_all_restaurants():
    """إرجاع جميع المطاعم في الدليل"""
    if not directory:
        return "No restaurants found in the directory."
    return directory

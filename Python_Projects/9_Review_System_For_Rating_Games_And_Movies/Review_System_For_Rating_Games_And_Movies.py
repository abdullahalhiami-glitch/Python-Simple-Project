data = {}

def add_item(name):
    if name not in data:
        data[name] = {"rating_sum": 0, "reviews_count": 0}

def add_review(name, rating):
    if name in data and 1 <= rating <= 5:
        data[name]["rating_sum"] += rating
        data[name]["reviews_count"] += 1

def get_average_rating(name):
    if name in data and data[name]["reviews_count"] > 0:
        return data[name]["rating_sum"] / data[name]["reviews_count"]
    return 0

def get_all_items():
    return list(data.keys())

def get_top_rated_item():
    if not data:
        return None
    top = max(data, key=lambda x: get_average_rating(x))
    return top

def get_items_with_no_reviews():
    return [name for name in data if data[name]["reviews_count"] == 0]

def reset_reviews(name):
    if name in data:
        data[name]["rating_sum"] = 0
        data[name]["reviews_count"] = 0

def delete_item(name):
    if name in data:
        del data[name]
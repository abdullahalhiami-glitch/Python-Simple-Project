'''
Docstring for Restaurant
'''
#a dictionary that stores our data for the restaurabt
dictionary = {}

def add_restaurant(name, cuisine_type):
    # "add new restaurant"
    if name in dictionary:
        return f"Restaurant '{name}' already exits."
    dictionary[name] = {"cuisine": cuisine_type, "ratings": []}
    return f"Restaurant '{name}' added successfully."

def add_rating(name, rating_value):
    #adding a new rating to a list inside a restaurant name
    if name not in dictionary:
        return f"Restaurant '{name}' not found."
    try:
        rating_value = float(rating_value)
        if not (0 <= rating_value <= 5):
            return f"Rating must be between 0 and 5."
        dictionary[name]["ratings"].append(rating_value)
        return f"Rating added to restaurant '{name}' successfully."
    except ValueError:
        return "Invaild rating value"
    
def get_restaurant_info(name):
    #show the type of restaurnat and its infromation
    if name not in dictionary:
        return f"Restaurant '{name}' not found."
    info = dictionary[name]
    return f"Cuisine: {info['cuisine']}, Ratings: {info['ratings']}"

def calculate_average_rating(name):
    #returns the average of the restaurant rating
    if name not in dictionary:
        return f"Restaurant '{name}' not found."
    ratings = dictionary[name]["ratings"]
    if not ratings:
        return "No ratings for this restaurant yet, zero rated star."
    avg = sum(ratings) / len(ratings)
    return round(avg, 2)

# def search_by_cuisine(cuisine_type):
#     if cuisine_type not in dictionary:
#         return f"Cuisine type '{cuisine_type}' not found."
#     cuisine_list = []
#     cuisine_list.append(dictionary["cuisine"])
#     return cuisine_list

def search_by_cuisine(cuisine_type):
    find = [name for name, info in dictionary.items() if info["cuisine"].lower() == cuisine_type.lower()]
    if not find:
        return f"No restaurant found for this cuisine '{cuisine_type}'."
    return find

def get_top_rated_restaurants(min_rating): 
    try:
        min_rating = float(min_rating)
    except ValueError:
        return "Invaild rating value."
    top_rated = []
    for name in dictionary:
        avg = calculate_average_rating(name)
        if isinstance(avg, (int,float)) and avg >= min_rating:
            top_rated.append((name,avg))
    if not top_rated:
        return f'No restaurant not found with an average rating of {min_rating} or higher.'
    return top_rated

def update_restaurants_cuisine(name, new_cuisine):
    if name not in dictionary:
        return f"Restaurant '{name}' not found."
    ratings = dictionary[name]["ratings"]

#deletes a restaurant from the system
def delete_restaurants(name):
    if name not in dictionary:
        return f"Restaurant '{name}' not found."
    del dictionary[name]
    return f"Restaurant '{name}' deleted successfully."

#prints all the restaurant names in the system
def list_all_restaurants():
    if not dictionary:
        return "No restaurants in the system."
    return list(dictionary.keys())

#searches for a restaurant by name and returns its information
def search_restaurant(name):
    if name not in dictionary:
        return f"Restaurant '{name}' not found."
    return dictionary[name]

#add a client to the system
def add_client(name, contact_info):
    if name in dictionary:
        return f"Client '{name}' already exists."
    dictionary[name] = {"contact_info": contact_info}
    return f"Client '{name}' added successfully."

#favorite restaurant for a client
def add_favorite_restaurant(client_name, restaurant_name):
    if client_name not in dictionary:
        return f"Client '{client_name}' not found."
    if restaurant_name not in dictionary:
        return f"Restaurant '{restaurant_name}' not found."
    if "favorites" not in dictionary[client_name]:
        dictionary[client_name]["favorites"] = []
    dictionary[client_name]["favorites"].append(restaurant_name)
    return f"Restaurant '{restaurant_name}' added to client '{client_name}' favorites successfully."

#client's favorite restaurant list
def get_favorite_restaurants(client_name):
    if client_name not in dictionary:
        return f"Client '{client_name}' not found."
    if "favorites" not in dictionary[client_name]:
        return f"Client '{client_name}' has no favorite restaurants."
    return dictionary[client_name]["favorites"]

#client's contact information
def get_client_contact_info(client_name):   
    if client_name not in dictionary:
        return f"Client '{client_name}' not found."
    return dictionary[client_name].get("contact_info", "No contact information available.")

#client can update their contact information
def update_client_contact_info(client_name, new_contact_info):
    if client_name not in dictionary:
        return f"Client '{client_name}' not found."
    dictionary[client_name]["contact_info"] = new_contact_info
    return f"Client '{client_name}' contact information updated successfully."

#view all clients in the system
def list_all_clients():
    clients = [name for name in dictionary if "contact_info" in dictionary[name]]
    if not clients:
        return "No clients in the system."
    return clients

#view client's rating history for a specific restaurant
def get_client_rating_history(client_name, restaurant_name):
    if client_name not in dictionary:
        return f"Client '{client_name}' not found."
    if restaurant_name not in dictionary:
        return f"Restaurant '{restaurant_name}' not found."
    ratings = dictionary[restaurant_name]["ratings"]
    if not ratings:
        return f"Client '{client_name}' has no rating history for restaurant '{restaurant_name}'."
    return ratings

#client can remove a restaurant from their favorites
def remove_favorite_restaurant(client_name, restaurant_name):
    if client_name not in dictionary:
        return f"Client '{client_name}' not found."
    if restaurant_name not in dictionary:
        return f"Restaurant '{restaurant_name}' not found."
    if "favorites" not in dictionary[client_name] or restaurant_name not in dictionary[client_name]["favorites"]:
        return f"Restaurant '{restaurant_name}' is not in client '{client_name}' favorites."
    dictionary[client_name]["favorites"].remove(restaurant_name)
    return f"Restaurant '{restaurant_name}' removed from client '{client_name}' favorites successfully."

#client can delete their account from the system
def delete_client_account(client_name): 
    if client_name not in dictionary:
        return f"Client '{client_name}' not found."
    del dictionary[client_name]
    return f"Client '{client_name}' account deleted successfully."


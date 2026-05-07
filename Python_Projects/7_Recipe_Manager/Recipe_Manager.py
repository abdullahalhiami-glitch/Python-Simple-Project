# Recipe Manager Application

recipes = {}  # Dictionary to store recipes: {"name": {"ingredients": [], "time": int}}

def add_recipe(name, ingredients_list, time_minutes):
    if name not in recipes:
        recipes[name] = {"ingredients": ingredients_list, "time": time_minutes}
    else:
        print(f"Recipe '{name}' already exists.")

def get_all_recipes():
    return list(recipes.keys())

def get_recipe_details(name):
    return recipes.get(name, None)

def search_by_ingredient(ingredient):
    result = []
    for recipe_name, details in recipes.items():
        if ingredient in details["ingredients"]:
            result.append(recipe_name)
    return result

def get_quick_recipes(max_time):
    result = []
    for recipe_name, details in recipes.items():
        if details["time"] < max_time:
            result.append(recipe_name)
    return result

def add_ingredient_to_recipe(recipe_name, new_ingredient):
    if recipe_name in recipes:
        recipes[recipe_name]["ingredients"].append(new_ingredient)
    else:
        print(f"Recipe '{recipe_name}' does not exist.")

def update_recipe_time(recipe_name, new_time):
    if recipe_name in recipes:
        recipes[recipe_name]["time"] = new_time
    else:
        print(f"Recipe '{recipe_name}' does not exist.")

def delete_recipe(recipe_name):
    if recipe_name in recipes:
        del recipes[recipe_name]
    else:
        print(f"Recipe '{recipe_name}' does not exist.")
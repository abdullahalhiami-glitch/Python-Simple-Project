'''
Docstring for 8_Lesson_Dictionaries.Practice_Dictionaries.3_A_Simple_Inventory_System
'''
#this program counts and updates the storehouse of the products that are inside it and the new products that have arrived

product_names_and_quantities = {
    "Apples":23,
    "Milk":10,
    "Rice":65,
    "Oranges":32,
    "Sweets":6,
    "Honey":15,
    "Jam":6,
    "IceCream":885,
    "Biscuits":55,
    "Chocolate":88,
    "Cookies":7,
    "Cake":79,
    "Cornflakes":52
    }
new_products = ["Apples","Apples","Sugar", "Cumin", "Vinegar", "Ketchup", "Mustard", "Salt", "IceCream", "Biscuits", "Chocolate", "Cake"]


for product in new_products:
    if product in product_names_and_quantities.keys():
        product_names_and_quantities[product] += 1
    elif product not in product_names_and_quantities.keys():
        product_names_and_quantities.update({product:1})
      
print(product_names_and_quantities)

for key,value in product_names_and_quantities.items():
    print(f"Product is {key}: and the count is {value}")


# Cafe POS System

# Data structures
menu = {
    "Coffee": 5.00,
    "Tea": 3.00,
    "Juice": 4.00,
    "Soda": 2.50
}

current_order = []

def get_menu():
    """Returns the menu of drinks and their prices."""
    return menu

def add_to_order(item_name, qty):
    """Adds the drink and quantity to the current order list."""
    if item_name in menu:
        current_order.append({"item": item_name, "qty": qty, "price": menu[item_name]})
    else:
        print("Item not in menu")

def remove_from_order(item_name):
    """Removes a drink from the current order if canceled."""
    for order in current_order:
        if order["item"] == item_name:
            current_order.remove(order)
            break

def get_current_order():
    """Returns the contents of the current order."""
    return current_order

def calculate_subtotal():
    """Calculates the subtotal before tax."""
    subtotal = 0.0
    for order in current_order:
        subtotal += order["qty"] * order["price"]
    return subtotal

def calculate_tax(subtotal, tax_rate):
    """Calculates the tax amount based on subtotal and tax rate."""
    return subtotal * tax_rate

def generate_invoice(subtotal, tax):
    """Returns a final dictionary with subtotal, tax, and total amount for the invoice."""
    total = subtotal + tax
    return {"subtotal": subtotal, "tax": tax, "total": total}

def clear_order():
    """Clears the current order list for a new customer."""
    current_order.clear()
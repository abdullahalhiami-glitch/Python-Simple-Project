cart = {
    "Laptop": {
        "price": 1000,
        "qty": 1
    }
}


def add_item_to_cart(name, price, qty):
    """Add a product or increase its quantity if already present."""
    if name in cart:
        cart[name]["qty"] += qty
    else:
        cart[name] = {"price": price, "qty": qty}


def update_item_qty(name, new_qty):
    """Update the quantity of a product directly."""
    if name in cart:
        if new_qty > 0:
            cart[name]["qty"] = new_qty
        else:
            cart.pop(name, None)


def remove_item_from_cart(name):
    """Remove a product completely from the cart."""
    cart.pop(name, None)


def get_cart_contents():
    """Return the contents of the cart."""
    return cart.copy()


def calculate_cart_total():
    """Calculate the total cost of the cart."""
    return sum(item["price"] * item["qty"] for item in cart.values())


def apply_coupon(total, discount_percentage):
    """Return the amount after applying a discount percentage."""
    discount = total * discount_percentage / 100
    return total - discount


def get_item_count():
    """Return the total number of pieces in the cart."""
    return sum(item["qty"] for item in cart.values())


def empty_cart():
    """Empty the cart."""
    cart.clear()

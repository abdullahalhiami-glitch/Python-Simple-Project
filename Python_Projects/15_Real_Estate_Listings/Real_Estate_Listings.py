properties = []


def add_property(prop_id, prop_type, price):
    """Register a new property in the system."""
    if any(prop["id"] == prop_id for prop in properties):
        raise ValueError(f"Property with id {prop_id} already exists.")
    properties.append({
        "id": prop_id,
        "type": prop_type,
        "price": price,
        "status": "Available",
    })


def get_all_properties():
    """Return all properties."""
    return list(properties)


def get_available_properties():
    """Return only properties that are available."""
    return [prop for prop in properties if prop["status"] == "Available"]


def rent_property(prop_id):
    """Mark a property as rented."""
    for prop in properties:
        if prop["id"] == prop_id:
            if prop["status"] != "Available":
                raise ValueError(f"Property {prop_id} is not available for rent.")
            prop["status"] = "Rented"
            return prop
    raise ValueError(f"Property with id {prop_id} not found.")


def search_by_max_price(budget_limit):
    """Return properties within the customer budget."""
    return [prop for prop in properties if prop["price"] <= budget_limit]


def search_by_type(prop_type):
    """Filter properties by type."""
    return [prop for prop in properties if prop["type"].lower() == prop_type.lower()]


def update_property_price(prop_id, new_price):
    """Update the price of an existing property."""
    for prop in properties:
        if prop["id"] == prop_id:
            prop["price"] = new_price
            return prop
    raise ValueError(f"Property with id {prop_id} not found.")


def remove_property(prop_id):
    """Remove a property from the system."""
    for index, prop in enumerate(properties):
        if prop["id"] == prop_id:
            return properties.pop(index)
    raise ValueError(f"Property with id {prop_id} not found.")

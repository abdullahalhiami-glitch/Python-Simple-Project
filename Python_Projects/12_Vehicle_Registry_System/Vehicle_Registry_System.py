vehicle_registry = {
    "1234-A": {
        "owner": "Ahmed",
        "model": "Toyota",
        "violations": 0,
    }
}


def register_vehicle(plate_number, owner, model):
    if plate_number in vehicle_registry:
        raise ValueError(f"Vehicle with plate {plate_number} already registered.")
    vehicle_registry[plate_number] = {
        "owner": owner,
        "model": model,
        "violations": 0,
    }


def get_vehicle_info(plate_number):
    if plate_number not in vehicle_registry:
        return None
    return vehicle_registry[plate_number].copy()


def update_vehicle_owner(plate_number, new_owner):
    if plate_number not in vehicle_registry:
        raise KeyError(f"Vehicle with plate {plate_number} not found.")
    vehicle_registry[plate_number]["owner"] = new_owner


def add_traffic_violation(plate_number, amount):
    if plate_number not in vehicle_registry:
        raise KeyError(f"Vehicle with plate {plate_number} not found.")
    if amount < 0:
        raise ValueError("Violation amount must be non-negative.")
    vehicle_registry[plate_number]["violations"] += amount


def get_total_violations(plate_number):
    if plate_number not in vehicle_registry:
        return None
    return vehicle_registry[plate_number]["violations"]


def pay_violation(plate_number, amount):
    if plate_number not in vehicle_registry:
        raise KeyError(f"Vehicle with plate {plate_number} not found.")
    if amount < 0:
        raise ValueError("Payment amount must be non-negative.")
    current = vehicle_registry[plate_number]["violations"]
    vehicle_registry[plate_number]["violations"] = max(0, current - amount)


def get_vehicles_with_violations():
    return [plate for plate, data in vehicle_registry.items() if data.get("violations", 0) > 0]


def search_vehicles_by_model(model):
    return [plate for plate, data in vehicle_registry.items() if data.get("model") == model]

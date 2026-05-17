"""
Transportation domain module for Al-Hiami Transportation.

The public function names intentionally match the original course project so
app.py can keep the existing route structure while gaining validation,
persistence, and safer booking behavior.
"""

from __future__ import annotations

import copy
import json
import re
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_FILE = DATA_DIR / "routes.json"
BACKUP_FILE = DATA_DIR / "routes.backup.json"
DEFAULT_TICKET_PRICE = 100
MAX_CAPACITY = 500


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _default_routes() -> list[dict]:
    return [
        {
            "Route_Id": "R1",
            "Destination": "Sana'a",
            "Total_Capacity": 30,
            "Available_Capacity": 30,
            "Capacity": 30,
            "Booked": [],
            "Ticket_Price": DEFAULT_TICKET_PRICE,
            "Created_At": _utc_now(),
            "Updated_At": _utc_now(),
        },
        {
            "Route_Id": "R2",
            "Destination": "Aden",
            "Total_Capacity": 42,
            "Available_Capacity": 42,
            "Capacity": 42,
            "Booked": [],
            "Ticket_Price": 120,
            "Created_At": _utc_now(),
            "Updated_At": _utc_now(),
        },
        {
            "Route_Id": "R3",
            "Destination": "Ibb",
            "Total_Capacity": 28,
            "Available_Capacity": 28,
            "Capacity": 28,
            "Booked": [],
            "Ticket_Price": 85,
            "Created_At": _utc_now(),
            "Updated_At": _utc_now(),
        },
        {
            "Route_Id": "R4",
            "Destination": "Taiz",
            "Total_Capacity": 36,
            "Available_Capacity": 36,
            "Capacity": 36,
            "Booked": [],
            "Ticket_Price": 95,
            "Created_At": _utc_now(),
            "Updated_At": _utc_now(),
        },
    ]


transportation_data: list[dict] = []


def _clean_text(value: object) -> str:
    return str(value or "").strip()


def _safe_route(route: dict) -> dict:
    safe = copy.deepcopy(route)
    booked = safe.get("Booked") or []
    safe["Booked"] = list(booked)
    safe["Booked_Count"] = len(booked)
    safe["Capacity"] = safe.get("Available_Capacity", safe.get("Capacity", 0))
    return safe


def _normalize_route(route: dict) -> dict:
    route_id = _clean_text(route.get("Route_Id") or route.get("route_id"))
    destination = _clean_text(route.get("Destination") or route.get("destination"))
    booked = route.get("Booked") or route.get("booked") or []
    if not isinstance(booked, list):
        booked = []
    booked = [_clean_text(name) for name in booked if _clean_text(name)]

    capacity_source = route.get("Total_Capacity", route.get("total_capacity"))
    if capacity_source is None:
        capacity_source = route.get("Capacity", route.get("capacity", 30))
    try:
        total_capacity = int(capacity_source)
    except (TypeError, ValueError):
        total_capacity = 30
    total_capacity = min(max(total_capacity, 1), MAX_CAPACITY)

    available_source = route.get("Available_Capacity", route.get("available_capacity"))
    if available_source is None:
        available_capacity = total_capacity - len(booked)
    else:
        try:
            available_capacity = int(available_source)
        except (TypeError, ValueError):
            available_capacity = total_capacity - len(booked)

    available_capacity = min(max(total_capacity - len(booked), 0), total_capacity)

    try:
        ticket_price = int(route.get("Ticket_Price", DEFAULT_TICKET_PRICE))
    except (TypeError, ValueError):
        ticket_price = DEFAULT_TICKET_PRICE

    return {
        "Route_Id": route_id,
        "Destination": destination,
        "Total_Capacity": total_capacity,
        "Available_Capacity": available_capacity,
        "Capacity": available_capacity,
        "Booked": booked,
        "Ticket_Price": max(ticket_price, 0),
        "Created_At": route.get("Created_At") or _utc_now(),
        "Updated_At": route.get("Updated_At") or _utc_now(),
    }


def _replace_data(routes: list[dict]) -> None:
    transportation_data.clear()
    seen_routes: set[str] = set()
    seen_destinations: set[str] = set()

    for raw_route in routes:
        route = _normalize_route(raw_route)
        route_key = route["Route_Id"].lower()
        destination_key = route["Destination"].lower()
        if not route["Route_Id"] or not route["Destination"]:
            continue
        if route_key in seen_routes or destination_key in seen_destinations:
            continue
        seen_routes.add(route_key)
        seen_destinations.add(destination_key)
        transportation_data.append(route)


def load_transportation_data() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists():
        _replace_data(_default_routes())
        save_transportation_data()
        return

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            payload = json.load(file)
        routes = payload.get("routes", payload) if isinstance(payload, dict) else payload
        if not isinstance(routes, list):
            raise ValueError("routes.json must contain a route list")
        _replace_data(routes)
        if not transportation_data:
            raise ValueError("routes.json contains no valid routes")
    except Exception:
        if BACKUP_FILE.exists():
            with BACKUP_FILE.open("r", encoding="utf-8") as file:
                payload = json.load(file)
            routes = payload.get("routes", payload) if isinstance(payload, dict) else payload
            _replace_data(routes)
        else:
            _replace_data(_default_routes())
        save_transportation_data()


def save_transportation_data() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "updated_at": _utc_now(),
        "routes": [_safe_route(route) for route in transportation_data],
    }

    if DATA_FILE.exists():
        shutil.copy2(DATA_FILE, BACKUP_FILE)

    with tempfile.NamedTemporaryFile(
        "w", delete=False, dir=DATA_DIR, encoding="utf-8", suffix=".tmp"
    ) as temp_file:
        json.dump(payload, temp_file, indent=2, ensure_ascii=False)
        temp_name = temp_file.name

    Path(temp_name).replace(DATA_FILE)


def validate_route_id(route_id: object) -> str:
    value = _clean_text(route_id).upper()
    if not value:
        raise ValueError("Route ID is required.")
    if not re.fullmatch(r"[A-Z0-9_-]{1,20}", value):
        raise ValueError("Route ID may contain letters, numbers, hyphens, and underscores only.")
    return value


def validate_destination(destination: object) -> str:
    value = _clean_text(destination)
    if not value:
        raise ValueError("Destination is required.")
    if len(value) < 2 or len(value) > 80:
        raise ValueError("Destination must be between 2 and 80 characters.")
    if any(char in value for char in "<>{}[]"):
        raise ValueError("Destination contains unsupported characters.")
    return value


def validate_capacity(capacity: object) -> int:
    try:
        value = int(capacity)
    except (TypeError, ValueError):
        raise ValueError("Capacity must be a whole number.")
    if value < 1 or value > MAX_CAPACITY:
        raise ValueError(f"Capacity must be between 1 and {MAX_CAPACITY}.")
    return value


def validate_passenger_name(passenger_name: object) -> str:
    value = _clean_text(passenger_name)
    if not value:
        raise ValueError("Passenger name is required.")
    if len(value) < 2 or len(value) > 80:
        raise ValueError("Passenger name must be between 2 and 80 characters.")
    if any(char in value for char in "<>{}[]"):
        raise ValueError("Passenger name contains unsupported characters.")
    return value


def find_route(route_id: object) -> dict | None:
    route_id = _clean_text(route_id).upper()
    for route in transportation_data:
        if route["Route_Id"].upper() == route_id:
            return _safe_route(route)
    return None


def _find_route_ref(route_id: object) -> dict | None:
    route_id = _clean_text(route_id).upper()
    for route in transportation_data:
        if route["Route_Id"].upper() == route_id:
            return route
    return None


def find_destination(destination: object) -> dict | None:
    destination = _clean_text(destination).lower()
    for route in transportation_data:
        if route["Destination"].lower() == destination:
            return _safe_route(route)
    return None


def add_route(route_id: object, destination: object, capacity: object) -> str:
    route_id = validate_route_id(route_id)
    destination = validate_destination(destination)
    capacity = validate_capacity(capacity)

    if find_route(route_id):
        return f"Route {route_id} already exists."
    if find_destination(destination):
        return f"Destination {destination} already exists."

    transportation_data.append(
        {
            "Route_Id": route_id,
            "Destination": destination,
            "Total_Capacity": capacity,
            "Available_Capacity": capacity,
            "Capacity": capacity,
            "Booked": [],
            "Ticket_Price": DEFAULT_TICKET_PRICE,
            "Created_At": _utc_now(),
            "Updated_At": _utc_now(),
        }
    )
    save_transportation_data()
    return f"Route {route_id} added successfully."


def update_route(route_id: object, destination: object | None = None, capacity: object | None = None) -> str:
    route_id = validate_route_id(route_id)
    route = _find_route_ref(route_id)
    if not route:
        return "Route not found."

    if destination is not None and _clean_text(destination):
        new_destination = validate_destination(destination)
        existing = find_destination(new_destination)
        if existing and existing["Route_Id"].upper() != route_id.upper():
            return f"Destination {new_destination} already exists."
        route["Destination"] = new_destination

    if capacity is not None and _clean_text(capacity):
        new_capacity = validate_capacity(capacity)
        booked_count = len(route.get("Booked", []))
        if new_capacity < booked_count:
            return f"Capacity cannot be less than current bookings ({booked_count})."
        route["Total_Capacity"] = new_capacity
        route["Available_Capacity"] = new_capacity - booked_count
        route["Capacity"] = route["Available_Capacity"]

    route["Updated_At"] = _utc_now()
    save_transportation_data()
    return f"Route {route_id} updated successfully."


def delete_route(route_id: object) -> str:
    route_id = validate_route_id(route_id)
    route = _find_route_ref(route_id)
    if not route:
        return "Route not found."
    transportation_data.remove(route)
    save_transportation_data()
    return f"Route {route_id} deleted successfully."


def get_available_routes() -> list[dict]:
    return [_safe_route(route) for route in transportation_data if route["Available_Capacity"] > 0]


def book_ticket(route_id: object, passenger_name: object) -> str:
    route_id = validate_route_id(route_id)
    passenger_name = validate_passenger_name(passenger_name)
    route = _find_route_ref(route_id)
    if not route:
        return "Route not found."
    if any(name.lower() == passenger_name.lower() for name in route["Booked"]):
        return f"{passenger_name} already booked."
    if route["Available_Capacity"] <= 0:
        return "No seats available."

    route["Booked"].append(passenger_name)
    route["Available_Capacity"] = max(route["Total_Capacity"] - len(route["Booked"]), 0)
    route["Capacity"] = route["Available_Capacity"]
    route["Updated_At"] = _utc_now()
    save_transportation_data()
    return f"Booking confirmed for {passenger_name} on route {route_id}."


def cancel_booking(route_id: object, passenger_name: object) -> str:
    route_id = validate_route_id(route_id)
    passenger_name = validate_passenger_name(passenger_name)
    route = _find_route_ref(route_id)
    if not route:
        return "Route not found."

    matched_name = next((name for name in route["Booked"] if name.lower() == passenger_name.lower()), None)
    if not matched_name:
        return f"{passenger_name} has no booking."

    route["Booked"].remove(matched_name)
    route["Available_Capacity"] = min(route["Total_Capacity"] - len(route["Booked"]), route["Total_Capacity"])
    route["Capacity"] = route["Available_Capacity"]
    route["Updated_At"] = _utc_now()
    save_transportation_data()
    return f"Booking cancelled for {matched_name}."


def check_seat_availability(route_id: object) -> int | str:
    route = find_route(route_id)
    if not route:
        return "Route not found."
    return route["Available_Capacity"]


def get_passenger_list(route_id: object) -> list[str] | str:
    route = find_route(route_id)
    if not route:
        return "Route not found."
    return route["Booked"]


def get_passenger_list_by_destination(destination: object) -> list[str] | str:
    destination = validate_destination(destination)
    route = find_destination(destination)
    if not route:
        return "Destination not found."
    return route["Booked"]


def get_passenger_list_by_route(route_id: object) -> list[str] | str:
    return get_passenger_list(route_id)


def calculate_route_revenue(route_id: object, ticket_price: object | None = None) -> dict | str:
    route = find_route(route_id)
    if not route:
        return "Route not found."
    price = route["Ticket_Price"] if ticket_price in (None, "") else validate_capacity(ticket_price)
    bookings = len(route["Booked"])
    return {
        "route_id": route["Route_Id"],
        "destination": route["Destination"],
        "ticket_price": price,
        "bookings": bookings,
        "revenue": bookings * price,
    }


def search_route_by_destination(destination: object) -> list[dict]:
    destination = validate_destination(destination).lower()
    return [
        _safe_route(route)
        for route in transportation_data
        if destination in route["Destination"].lower()
    ]


def view_all_destinations() -> list[str]:
    return [route["Destination"] for route in transportation_data]


def view_all_routes() -> list[dict]:
    return [_safe_route(route) for route in transportation_data]


def get_route_summary(route_id: object) -> dict | str:
    route = find_route(route_id)
    if not route:
        return "Route not found."
    booked_count = len(route["Booked"])
    utilization = round((booked_count / route["Total_Capacity"]) * 100, 2) if route["Total_Capacity"] else 0
    revenue = booked_count * route["Ticket_Price"]
    return {
        "route_id": route["Route_Id"],
        "destination": route["Destination"],
        "total_capacity": route["Total_Capacity"],
        "available_capacity": route["Available_Capacity"],
        "booked_count": booked_count,
        "utilization": utilization,
        "ticket_price": route["Ticket_Price"],
        "revenue": revenue,
        "passengers": route["Booked"],
    }


def get_total_routes() -> int:
    return len(transportation_data)


def get_total_destinations() -> int:
    return len(set(route["Destination"].lower() for route in transportation_data))


def get_total_bookings() -> int:
    return sum(len(route["Booked"]) for route in transportation_data)


def get_system_statistics() -> dict:
    routes = view_all_routes()
    total_capacity = sum(route["Total_Capacity"] for route in routes)
    available_capacity = sum(route["Available_Capacity"] for route in routes)
    booked = get_total_bookings()
    revenue = sum(len(route["Booked"]) * route["Ticket_Price"] for route in routes)
    utilization = round((booked / total_capacity) * 100, 2) if total_capacity else 0
    summaries = [get_route_summary(route["Route_Id"]) for route in routes]
    return {
        "total_routes": get_total_routes(),
        "total_destinations": get_total_destinations(),
        "total_bookings": booked,
        "total_capacity": total_capacity,
        "available_capacity": available_capacity,
        "revenue": revenue,
        "utilization": utilization,
        "routes": routes,
        "route_summaries": summaries,
        "destinations": view_all_destinations(),
    }


def reset_transportation_data() -> str:
    _replace_data(_default_routes())
    save_transportation_data()
    return "Transportation data reset successfully."


def print_all_routes() -> None:
    print(transportation_data)


load_transportation_data()

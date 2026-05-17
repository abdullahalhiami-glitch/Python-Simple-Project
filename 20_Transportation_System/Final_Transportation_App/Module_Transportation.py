"""
Module_Transportation.py
========================
Al-Hiami Transportation System — Core Data & Business Logic Module

This module manages all transportation data, route operations, bookings,
passenger tracking, revenue calculations, and data persistence.
"""

import json
import os
import threading
from datetime import datetime

# ─────────────────────────────────────────────
#  CONFIGURATION
# ─────────────────────────────────────────────

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "routes.json")
TICKET_PRICE = 50  # Default price per ticket in USD

# Thread lock for safe concurrent access
_lock = threading.Lock()

# ─────────────────────────────────────────────
#  SEED DATA
# ─────────────────────────────────────────────

_DEFAULT_DATA = [
    {"Route_Id": "R1", "Destination": "Sana'a",   "Capacity": 30, "Total_Capacity": 30, "Booked": []},
    {"Route_Id": "R2", "Destination": "Aden",      "Capacity": 25, "Total_Capacity": 25, "Booked": []},
    {"Route_Id": "R3", "Destination": "Taiz",      "Capacity": 20, "Total_Capacity": 20, "Booked": []},
    {"Route_Id": "R4", "Destination": "Hodeidah",  "Capacity": 20, "Total_Capacity": 20, "Booked": []},
    {"Route_Id": "R5", "Destination": "Mukalla",   "Capacity": 15, "Total_Capacity": 15, "Booked": []},
]

# ─────────────────────────────────────────────
#  PERSISTENCE LAYER
# ─────────────────────────────────────────────

def _ensure_data_dir():
    """Create the data directory if it does not exist."""
    data_dir = os.path.dirname(DATA_FILE)
    os.makedirs(data_dir, exist_ok=True)


def save_data():
    """Persist current transportation_data to JSON file."""
    try:
        _ensure_data_dir()
        with _lock:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(transportation_data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"[WARNING] Could not save data: {e}")


def load_data():
    """Load transportation_data from JSON file, or return seed data."""
    global transportation_data
    _ensure_data_dir()
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                loaded = json.load(f)
            # Back-fill Total_Capacity for legacy records
            for route in loaded:
                if "Total_Capacity" not in route:
                    route["Total_Capacity"] = route["Capacity"] + len(route.get("Booked", []))
            transportation_data = loaded
            return
        except Exception as e:
            print(f"[WARNING] Could not load data: {e}")
    # Fallback to seed data
    transportation_data = [dict(r) for r in _DEFAULT_DATA]
    save_data()


# ─────────────────────────────────────────────
#  IN-MEMORY STORE (populated by load_data)
# ─────────────────────────────────────────────

transportation_data = [dict(r) for r in _DEFAULT_DATA]
load_data()  # Load persisted data on import


# ─────────────────────────────────────────────
#  VALIDATION HELPERS
# ─────────────────────────────────────────────

def validate_route_id(route_id):
    """Return (True, '') or (False, error_message)."""
    if not route_id or not str(route_id).strip():
        return False, "Route ID cannot be empty."
    if len(str(route_id).strip()) > 20:
        return False, "Route ID must be 20 characters or fewer."
    return True, ""


def validate_destination(destination):
    """Return (True, '') or (False, error_message)."""
    if not destination or not str(destination).strip():
        return False, "Destination cannot be empty."
    if len(str(destination).strip()) > 100:
        return False, "Destination name must be 100 characters or fewer."
    return True, ""


def validate_capacity(capacity):
    """Return (True, '') or (False, error_message)."""
    try:
        cap = int(capacity)
    except (TypeError, ValueError):
        return False, "Capacity must be a valid integer."
    if cap < 1:
        return False, "Capacity must be at least 1."
    if cap > 200:
        return False, "Capacity must not exceed 200."
    return True, ""


def validate_passenger_name(name):
    """Return (True, '') or (False, error_message)."""
    if not name or not str(name).strip():
        return False, "Passenger name cannot be empty."
    if len(str(name).strip()) > 100:
        return False, "Passenger name must be 100 characters or fewer."
    return True, ""


# ─────────────────────────────────────────────
#  CORE FUNCTIONS
# ─────────────────────────────────────────────

def find_route(route_id):
    """Return a route dict by Route_Id, or None."""
    rid = str(route_id).strip().upper() if route_id else None
    for route in transportation_data:
        if route["Route_Id"].upper() == rid:
            return route
    return None


def find_destination(destination):
    """Return the first route dict matching the destination, or None."""
    if not destination:
        return None
    dest = str(destination).strip().lower()
    for route in transportation_data:
        if route["Destination"].lower() == dest:
            return route
    return None


def add_route(route_id, destination, capacity):
    """Add a new route. Returns a result dict with success/message."""
    ok, err = validate_route_id(route_id)
    if not ok:
        return {"success": False, "message": err}

    ok, err = validate_destination(destination)
    if not ok:
        return {"success": False, "message": err}

    ok, err = validate_capacity(capacity)
    if not ok:
        return {"success": False, "message": err}

    rid = str(route_id).strip().upper()
    dest = str(destination).strip()
    cap = int(capacity)

    if find_route(rid):
        return {"success": False, "message": f"Route {rid} already exists."}

    if find_destination(dest):
        return {"success": False, "message": f"Destination '{dest}' is already assigned to another route."}

    route_data = {
        "Route_Id": rid,
        "Destination": dest,
        "Capacity": cap,
        "Total_Capacity": cap,
        "Booked": []
    }
    with _lock:
        transportation_data.append(route_data)
    save_data()
    return {"success": True, "message": f"Route {rid} to '{dest}' added successfully.", "data": route_data}


def delete_route(route_id):
    """Delete a route by ID. Returns result dict."""
    global transportation_data
    ok, err = validate_route_id(route_id)
    if not ok:
        return {"success": False, "message": err}

    rid = str(route_id).strip().upper()
    route = find_route(rid)
    if not route:
        return {"success": False, "message": f"Route {rid} not found."}

    with _lock:
        transportation_data = [r for r in transportation_data if r["Route_Id"].upper() != rid]
    save_data()
    return {"success": True, "message": f"Route {rid} deleted successfully."}


def update_route(route_id, destination=None, capacity=None):
    """Update destination and/or capacity of an existing route."""
    ok, err = validate_route_id(route_id)
    if not ok:
        return {"success": False, "message": err}

    rid = str(route_id).strip().upper()
    route = find_route(rid)
    if not route:
        return {"success": False, "message": f"Route {rid} not found."}

    if destination is not None:
        ok, err = validate_destination(destination)
        if not ok:
            return {"success": False, "message": err}
        route["Destination"] = str(destination).strip()

    if capacity is not None:
        ok, err = validate_capacity(capacity)
        if not ok:
            return {"success": False, "message": err}
        new_cap = int(capacity)
        booked_count = len(route["Booked"])
        if new_cap < booked_count:
            return {"success": False, "message": f"Cannot reduce capacity below current bookings ({booked_count})."}
        route["Capacity"] = new_cap - booked_count
        route["Total_Capacity"] = new_cap

    save_data()
    return {"success": True, "message": f"Route {rid} updated.", "data": route}


def get_available_routes():
    """Return all routes with at least 1 available seat."""
    return [r for r in transportation_data if r["Capacity"] > 0]


def book_ticket(route_id, passenger_name):
    """Book a seat. Returns result dict."""
    ok, err = validate_route_id(route_id)
    if not ok:
        return {"success": False, "message": err}
    ok, err = validate_passenger_name(passenger_name)
    if not ok:
        return {"success": False, "message": err}

    rid = str(route_id).strip().upper()
    pname = str(passenger_name).strip()
    route = find_route(rid)

    if not route:
        return {"success": False, "message": f"Route {rid} not found."}
    if pname in route["Booked"]:
        return {"success": False, "message": f"{pname} already has a booking on route {rid}."}
    if route["Capacity"] <= 0:
        return {"success": False, "message": f"No seats available on route {rid}."}

    with _lock:
        route["Booked"].append(pname)
        route["Capacity"] -= 1
    save_data()
    return {
        "success": True,
        "message": f"Booking confirmed for {pname} on route {rid} to {route['Destination']}.",
        "data": {"route_id": rid, "destination": route["Destination"], "passenger": pname}
    }


def cancel_booking(route_id, passenger_name):
    """Cancel a booking. Returns result dict."""
    ok, err = validate_route_id(route_id)
    if not ok:
        return {"success": False, "message": err}
    ok, err = validate_passenger_name(passenger_name)
    if not ok:
        return {"success": False, "message": err}

    rid = str(route_id).strip().upper()
    pname = str(passenger_name).strip()
    route = find_route(rid)

    if not route:
        return {"success": False, "message": f"Route {rid} not found."}
    if pname not in route["Booked"]:
        return {"success": False, "message": f"{pname} has no booking on route {rid}."}

    with _lock:
        route["Booked"].remove(pname)
        route["Capacity"] += 1
    save_data()
    return {"success": True, "message": f"Booking cancelled for {pname} on route {rid}."}


def check_seat_availability(route_id):
    """Return available seats count or error dict."""
    ok, err = validate_route_id(route_id)
    if not ok:
        return {"success": False, "message": err}

    rid = str(route_id).strip().upper()
    route = find_route(rid)
    if not route:
        return {"success": False, "message": f"Route {rid} not found."}

    return {
        "success": True,
        "available_seats": route["Capacity"],
        "total_seats": route["Total_Capacity"],
        "booked_seats": len(route["Booked"]),
        "route_id": rid,
        "destination": route["Destination"]
    }


def get_passenger_list(route_id):
    """Return passenger list for a route."""
    ok, err = validate_route_id(route_id)
    if not ok:
        return {"success": False, "message": err}

    rid = str(route_id).strip().upper()
    route = find_route(rid)
    if not route:
        return {"success": False, "message": f"Route {rid} not found."}

    return {"success": True, "passengers": route["Booked"], "route_id": rid, "destination": route["Destination"]}


def get_passenger_list_by_destination(destination):
    """Return passengers for all routes serving a destination."""
    ok, err = validate_destination(destination)
    if not ok:
        return {"success": False, "message": err}

    dest = str(destination).strip().lower()
    results = []
    for route in transportation_data:
        if route["Destination"].lower() == dest:
            results.append({
                "route_id": route["Route_Id"],
                "destination": route["Destination"],
                "passengers": route["Booked"]
            })

    if not results:
        return {"success": False, "message": f"No routes found for destination '{destination}'."}
    return {"success": True, "data": results}


def get_passenger_list_by_route(route_id):
    """Alias of get_passenger_list — returns passengers for a route ID."""
    return get_passenger_list(route_id)


def calculate_route_revenue(route_id, ticket_price=TICKET_PRICE):
    """Calculate revenue for a route based on booked passengers."""
    ok, err = validate_route_id(route_id)
    if not ok:
        return {"success": False, "message": err}

    rid = str(route_id).strip().upper()
    route = find_route(rid)
    if not route:
        return {"success": False, "message": f"Route {rid} not found."}

    booked = len(route["Booked"])
    revenue = booked * float(ticket_price)
    return {
        "success": True,
        "route_id": rid,
        "destination": route["Destination"],
        "booked_seats": booked,
        "ticket_price": ticket_price,
        "total_revenue": revenue
    }


def search_route_by_destination(destination):
    """Search for routes whose destination matches (case-insensitive partial match)."""
    if not destination or not str(destination).strip():
        return {"success": False, "message": "Destination cannot be empty."}

    dest = str(destination).strip().lower()
    results = [r for r in transportation_data if dest in r["Destination"].lower()]
    return {"success": True, "routes": results, "count": len(results)}


def view_all_destinations():
    """Return a list of all destination names."""
    return list({r["Destination"] for r in transportation_data})


def view_all_routes():
    """Return a list of all route IDs."""
    return [r["Route_Id"] for r in transportation_data]


def get_route_summary(route_id):
    """Return a full summary dict for a single route."""
    ok, err = validate_route_id(route_id)
    if not ok:
        return {"success": False, "message": err}

    rid = str(route_id).strip().upper()
    route = find_route(rid)
    if not route:
        return {"success": False, "message": f"Route {rid} not found."}

    booked = len(route["Booked"])
    utilization = round((booked / route["Total_Capacity"]) * 100, 1) if route["Total_Capacity"] > 0 else 0
    return {
        "success": True,
        "data": {
            "route_id": route["Route_Id"],
            "destination": route["Destination"],
            "total_capacity": route["Total_Capacity"],
            "available_seats": route["Capacity"],
            "booked_seats": booked,
            "utilization_pct": utilization,
            "passengers": route["Booked"],
            "estimated_revenue": booked * TICKET_PRICE
        }
    }


def get_total_routes():
    return len(transportation_data)


def get_total_destinations():
    return len({r["Destination"] for r in transportation_data})


def get_total_bookings():
    return sum(len(r["Booked"]) for r in transportation_data)


def get_system_statistics():
    """Return aggregated system-wide statistics."""
    total_routes = get_total_routes()
    total_destinations = get_total_destinations()
    total_bookings = get_total_bookings()
    total_capacity = sum(r["Total_Capacity"] for r in transportation_data)
    available_seats = sum(r["Capacity"] for r in transportation_data)
    total_revenue = total_bookings * TICKET_PRICE
    utilization = round((total_bookings / total_capacity) * 100, 1) if total_capacity > 0 else 0

    return {
        "total_routes": total_routes,
        "total_destinations": total_destinations,
        "total_bookings": total_bookings,
        "total_capacity": total_capacity,
        "available_seats": available_seats,
        "total_revenue": total_revenue,
        "utilization_pct": utilization,
        "ticket_price": TICKET_PRICE,
        "routes": [get_route_summary(r["Route_Id"])["data"] for r in transportation_data]
    }


def reset_transportation_data():
    """Reset to seed data (for testing). Clears persisted file."""
    global transportation_data
    with _lock:
        transportation_data = [dict(r) for r in _DEFAULT_DATA]
    save_data()
    return {"success": True, "message": "Transportation data has been reset to defaults."}

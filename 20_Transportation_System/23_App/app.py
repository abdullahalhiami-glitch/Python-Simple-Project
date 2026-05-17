"""
app.py
======
Al-Hiami Transportation System — Flask Application
Fixed, extended, and production-hardened version.
"""

from flask import Flask, render_template, request, jsonify
import Module_Transportation as mt

# ─────────────────────────────────────────────
#  APP SETUP
# ─────────────────────────────────────────────

transportation = Flask(__name__)
transportation.config["JSON_SORT_KEYS"] = False

# System operational flag
_system_running = True


def _ok(data=None, message="Success", status=200):
    """Standard success JSON response."""
    payload = {"success": True, "message": message}
    if data is not None:
        payload["data"] = data
    return jsonify(payload), status


def _err(message="An error occurred.", status=400):
    """Standard error JSON response."""
    return jsonify({"success": False, "message": message}), status


# ─────────────────────────────────────────────
#  PAGE ROUTES
# ─────────────────────────────────────────────

@transportation.route("/")
def home():
    stats = mt.get_system_statistics()
    return render_template(
        "index.html",
        Transportation_System="Al-Hiami Transportation",
        name="Al-Hiami Transportation App",
        Transport=mt.transportation_data,
        exitpro=_system_running,
        stats=stats,
    )


@transportation.route("/about")
def about():
    return render_template(
        "about.html",
        Transportation_System="About — Al-Hiami Transportation",
        name="About Al-Hiami Transportation",
    )


@transportation.route("/contactus")
def contactus():
    return render_template(
        "contactus.html",
        Transportation_System="Contact Us — Al-Hiami Transportation",
        name="Contact Al-Hiami Transportation",
    )


@transportation.route("/information")
def information():
    stats = mt.get_system_statistics()
    return render_template(
        "information.html",
        Transportation_System="Information — Al-Hiami Transportation",
        name="System Information",
        stats=stats,
        routes=mt.transportation_data,
    )


# ─────────────────────────────────────────────
#  API ENDPOINTS
# ─────────────────────────────────────────────

@transportation.route("/status", methods=["GET"])
def check_status():
    global _system_running
    status_str = "Running" if _system_running else "Stopped"
    stats = mt.get_system_statistics()
    return jsonify({
        "success": True,
        "status": status_str,
        "running": _system_running,
        "stats": stats
    })


@transportation.route("/exit", methods=["POST"])
def exit_app():
    global _system_running
    _system_running = False
    return _ok(message="System has been stopped.")


@transportation.route("/restart", methods=["POST"])
def restart_app():
    global _system_running
    _system_running = True
    return _ok(message="System has been restarted and is now running.")


# ── Route Search ─────────────────────────────

@transportation.route("/searchroute", methods=["POST"])
def find_route():
    route_id = request.form.get("route_id", "").strip()
    if not route_id:
        return _err("Route ID is required.", 400)
    route = mt.find_route(route_id)
    if route:
        return _ok(data=route, message="Route found.")
    return _err(f"Route '{route_id}' not found.", 404)


@transportation.route("/searchdestination", methods=["POST"])
def find_destination():
    destination = request.form.get("destination", "").strip()
    if not destination:
        return _err("Destination is required.", 400)
    route = mt.find_destination(destination)
    if route:
        return _ok(data=route, message="Destination found.")
    return _err(f"Destination '{destination}' not found.", 404)


# ── Route Management ─────────────────────────

@transportation.route("/addroute", methods=["POST"])
def add_route():
    route_id = request.form.get("route_id", "").strip()
    destination = request.form.get("destination", "").strip()
    capacity_raw = request.form.get("capacity", "").strip()

    if not route_id or not destination or not capacity_raw:
        return _err("route_id, destination, and capacity are all required.", 400)

    try:
        capacity = int(capacity_raw)
    except ValueError:
        return _err("Capacity must be a valid integer.", 400)

    result = mt.add_route(route_id, destination, capacity)
    if result.get("success"):
        return _ok(data=result.get("data"), message=result["message"], status=201)
    return _err(result["message"], 400)


@transportation.route("/deleteroute", methods=["POST"])
def delete_route():
    route_id = request.form.get("route_id", "").strip()
    if not route_id:
        return _err("Route ID is required.", 400)
    result = mt.delete_route(route_id)
    if result.get("success"):
        return _ok(message=result["message"])
    return _err(result["message"], 404)


@transportation.route("/availableroutes", methods=["GET"])
def get_available_routes():
    routes = mt.get_available_routes()
    return _ok(data=routes, message=f"{len(routes)} available routes found.")


@transportation.route("/viewallroutes", methods=["GET"])
def view_all_routes():
    result = mt.view_all_routes()
    return _ok(data=result, message=f"{len(result)} routes found.")


@transportation.route("/viewalldestinations", methods=["GET"])
def view_all_destinations():
    result = mt.view_all_destinations()
    return _ok(data=result, message=f"{len(result)} destinations found.")


@transportation.route("/searchroutebydestination", methods=["POST"])
def search_route_by_destination():
    destination = request.form.get("destination", "").strip()
    if not destination:
        return _err("Destination is required.", 400)
    result = mt.search_route_by_destination(destination)
    return jsonify(result)


# ── Booking ───────────────────────────────────

@transportation.route("/bookticket", methods=["POST"])
def book_ticket():
    route_id = request.form.get("route_id", "").strip()
    passenger_name = request.form.get("passenger_name", "").strip()
    if not route_id or not passenger_name:
        return _err("route_id and passenger_name are required.", 400)
    result = mt.book_ticket(route_id, passenger_name)
    if result.get("success"):
        return _ok(data=result.get("data"), message=result["message"])
    return _err(result["message"], 400)


@transportation.route("/cancelbooking", methods=["POST"])
def cancel_booking():
    route_id = request.form.get("route_id", "").strip()
    passenger_name = request.form.get("passenger_name", "").strip()
    if not route_id or not passenger_name:
        return _err("route_id and passenger_name are required.", 400)
    result = mt.cancel_booking(route_id, passenger_name)
    if result.get("success"):
        return _ok(message=result["message"])
    return _err(result["message"], 400)


# ── Seat Availability ─────────────────────────

@transportation.route("/checkseatavailability", methods=["POST"])
def check_seat_availability():
    route_id = request.form.get("route_id", "").strip()
    if not route_id:
        return _err("Route ID is required.", 400)
    result = mt.check_seat_availability(route_id)
    if result.get("success"):
        return _ok(data=result, message="Seat availability retrieved.")
    return _err(result["message"], 404)


# ── Passenger Lists ───────────────────────────

@transportation.route("/getpassengerlist", methods=["POST"])
def get_passenger_list():
    route_id = request.form.get("route_id", "").strip()
    if not route_id:
        return _err("Route ID is required.", 400)
    result = mt.get_passenger_list(route_id)
    if result.get("success"):
        return _ok(data=result, message="Passenger list retrieved.")
    return _err(result["message"], 404)


@transportation.route("/getpassengerlistbydestination", methods=["POST"])
def get_passenger_list_by_destination():
    destination = request.form.get("destination", "").strip()
    if not destination:
        return _err("Destination is required.", 400)
    result = mt.get_passenger_list_by_destination(destination)
    if result.get("success"):
        return _ok(data=result.get("data"), message="Passenger list retrieved.")
    return _err(result["message"], 404)


@transportation.route("/getpassengerlistbyroute", methods=["POST"])
def get_passenger_list_by_route():
    route_id = request.form.get("route_id", "").strip()
    if not route_id:
        return _err("Route ID is required.", 400)
    result = mt.get_passenger_list_by_route(route_id)
    if result.get("success"):
        return _ok(data=result, message="Passenger list retrieved.")
    return _err(result["message"], 404)


# ── Revenue ───────────────────────────────────

@transportation.route("/calculaterouterevenue", methods=["POST"])
def calculate_route_revenue():
    route_id = request.form.get("route_id", "").strip()
    ticket_price_raw = request.form.get("ticket_price", str(mt.TICKET_PRICE)).strip()
    if not route_id:
        return _err("Route ID is required.", 400)
    try:
        ticket_price = float(ticket_price_raw)
    except ValueError:
        return _err("Ticket price must be a valid number.", 400)
    result = mt.calculate_route_revenue(route_id, ticket_price)
    if result.get("success"):
        return _ok(data=result, message="Revenue calculated.")
    return _err(result["message"], 404)


# ── Statistics ────────────────────────────────

@transportation.route("/api/statistics", methods=["GET"])
def api_statistics():
    stats = mt.get_system_statistics()
    return jsonify({"success": True, "data": stats})


@transportation.route("/api/routesummary/<route_id>", methods=["GET"])
def api_route_summary(route_id):
    result = mt.get_route_summary(route_id)
    if result.get("success"):
        return _ok(data=result["data"])
    return _err(result["message"], 404)


@transportation.route("/api/allroutes", methods=["GET"])
def api_all_routes():
    return _ok(data=mt.transportation_data, message="All routes retrieved.")


# ─────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    transportation.run(debug=True, host="0.0.0.0", port=5000)
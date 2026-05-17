from __future__ import annotations

from functools import wraps

from flask import Flask, jsonify, render_template, request

import Module_Transportation as mt
from config import Config


transportation = Flask(__name__, template_folder="templates")
transportation.config.from_object(Config)

system_running = True


def api_response(success: bool, message: str, data=None, status_code: int = 200):
    return jsonify({"success": success, "message": message, "data": data}), status_code


def success(message: str, data=None, status_code: int = 200):
    return api_response(True, message, data, status_code)


def error(message: str, status_code: int = 400, data=None):
    return api_response(False, message, data, status_code)


def form_value(name: str) -> str:
    value = request.form.get(name, "")
    if isinstance(value, str):
        value = value.strip()
    if value in (None, ""):
        raise ValueError(f"{name.replace('_', ' ').title()} is required.")
    return value


def optional_form_value(name: str):
    value = request.form.get(name)
    return value.strip() if isinstance(value, str) else value


def guarded_api(handler):
    @wraps(handler)
    def wrapper(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except ValueError as exc:
            return error(str(exc), 400)
        except Exception:
            return error("Unexpected server error. Please try again.", 500)

    return wrapper


def message_status(message: str) -> int:
    normalized = message.lower()
    if "not found" in normalized or "no booking" in normalized:
        return 404
    if "already" in normalized or "no seats" in normalized or "cannot" in normalized:
        return 409
    return 200


def page_context(title: str, active_page: str) -> dict:
    return {
        "Transportation_System": title,
        "name": "Al-Hiami Transportation",
        "stats": mt.get_system_statistics(),
        "system_running": system_running,
        "active_page": active_page,
    }


@transportation.route("/")
def home():
    return render_template("index.html", **page_context("Al-Hiami Transportation", "home"))


@transportation.route("/about")
def about():
    return render_template("about.html", **page_context("About Al-Hiami Transportation", "about"))


@transportation.route("/contactus")
def contactus():
    return render_template("contactus.html", **page_context("Contact Al-Hiami Transportation", "contact"))


@transportation.route("/information")
def information():
    return render_template("information.html", **page_context("Al-Hiami Operations Dashboard", "information"))


@transportation.route("/searchroute", methods=["POST"])
@guarded_api
def find_route():
    route_id = mt.validate_route_id(form_value("route_id"))
    route = mt.find_route(route_id)
    if not route:
        return error("Route not found.", 404)
    return success("Route found.", route)


@transportation.route("/searchdestination", methods=["POST"])
@guarded_api
def find_destination():
    destination = mt.validate_destination(form_value("destination_id"))
    route = mt.find_destination(destination)
    if not route:
        return error("Destination not found.", 404)
    return success("Destination found.", route)


@transportation.route("/addroute", methods=["POST"])
@guarded_api
def add_route():
    route_id = form_value("route_id")
    destination = form_value("destination")
    capacity = form_value("capacity")
    message = mt.add_route(route_id, destination, capacity)
    route = mt.find_route(route_id)
    return api_response(message_status(message) == 200, message, route, message_status(message))


@transportation.route("/updateroute", methods=["POST"])
@guarded_api
def update_route():
    route_id = form_value("route_id")
    destination = optional_form_value("destination")
    capacity = optional_form_value("capacity")
    message = mt.update_route(route_id, destination=destination, capacity=capacity)
    route = mt.find_route(route_id)
    return api_response(message_status(message) == 200, message, route, message_status(message))


@transportation.route("/deleteroute", methods=["POST"])
@guarded_api
def delete_route():
    route_id = form_value("route_id")
    message = mt.delete_route(route_id)
    return api_response(message_status(message) == 200, message, {"route_id": route_id}, message_status(message))


@transportation.route("/availableroutes", methods=["GET"])
@guarded_api
def get_available_routes():
    routes = mt.get_available_routes()
    return success("Available routes loaded.", routes)


@transportation.route("/bookticket", methods=["POST"])
@guarded_api
def book_ticket():
    route_id = form_value("route_id")
    passenger_name = form_value("passenger_name")
    message = mt.book_ticket(route_id, passenger_name)
    route = mt.find_route(route_id)
    return api_response(message_status(message) == 200, message, route, message_status(message))


@transportation.route("/cancelbooking", methods=["POST"])
@guarded_api
def cancel_booking():
    route_id = form_value("route_id")
    passenger_name = form_value("passenger_name")
    message = mt.cancel_booking(route_id, passenger_name)
    route = mt.find_route(route_id)
    return api_response(message_status(message) == 200, message, route, message_status(message))


@transportation.route("/exit", methods=["POST"])
@guarded_api
def exit_app():
    global system_running
    system_running = False
    return success("System marked as offline.", {"status": "Exited"})


@transportation.route("/restart", methods=["POST"])
@guarded_api
def restart_app():
    global system_running
    system_running = True
    return success("System restarted.", {"status": "Running"})


@transportation.route("/status", methods=["GET"])
@guarded_api
def check_status():
    status = "Running" if system_running else "Exited"
    return success("System status loaded.", {"status": status, "running": system_running})


@transportation.route("/checkseatavailability", methods=["POST"])
@guarded_api
def check_seat_availability():
    route_id = form_value("route_id")
    result = mt.check_seat_availability(route_id)
    if isinstance(result, str):
        return error(result, 404)
    return success("Seat availability loaded.", {"route_id": mt.validate_route_id(route_id), "available_seats": result})


@transportation.route("/getpassengerlist", methods=["POST"])
@guarded_api
def get_passenger_list():
    route_id = form_value("route_id")
    result = mt.get_passenger_list(route_id)
    if isinstance(result, str):
        return error(result, 404)
    return success("Passenger list loaded.", {"route_id": mt.validate_route_id(route_id), "passenger_list": result})


@transportation.route("/getpassengerlistbydestination", methods=["POST"])
@guarded_api
def get_passenger_list_by_destination():
    destination = form_value("destination")
    result = mt.get_passenger_list_by_destination(destination)
    if isinstance(result, str):
        return error(result, 404)
    return success("Destination passenger list loaded.", {"destination": destination, "passenger_list": result})


@transportation.route("/getpassengerlistbyroute", methods=["POST"])
@guarded_api
def get_passenger_list_by_route():
    route_id = form_value("route_id")
    result = mt.get_passenger_list_by_route(route_id)
    if isinstance(result, str):
        return error(result, 404)
    return success("Route passenger list loaded.", {"route_id": mt.validate_route_id(route_id), "passenger_list": result})


@transportation.route("/calculaterouterevenue", methods=["POST"])
@guarded_api
def calculate_route_revenue():
    route_id = form_value("route_id")
    ticket_price = optional_form_value("ticket_price")
    result = mt.calculate_route_revenue(route_id, ticket_price=ticket_price)
    if isinstance(result, str):
        return error(result, 404)
    return success("Route revenue calculated.", result)


@transportation.route("/searchroutebydestination", methods=["POST"])
@guarded_api
def search_route_by_destination():
    destination = form_value("destination")
    result = mt.search_route_by_destination(destination)
    if not result:
        return error("No routes found for this destination.", 404, [])
    return success("Routes found for destination.", result)


@transportation.route("/viewalldestinations", methods=["GET"])
@guarded_api
def view_all_destinations():
    return success("Destinations loaded.", mt.view_all_destinations())


@transportation.route("/viewallroutes", methods=["GET"])
@guarded_api
def view_all_routes():
    return success("Routes loaded.", mt.view_all_routes())


@transportation.route("/routesummary", methods=["POST"])
@guarded_api
def route_summary():
    route_id = form_value("route_id")
    result = mt.get_route_summary(route_id)
    if isinstance(result, str):
        return error(result, 404)
    return success("Route summary loaded.", result)


@transportation.route("/systemstatistics", methods=["GET"])
@guarded_api
def system_statistics():
    return success("System statistics loaded.", mt.get_system_statistics())


@transportation.route("/resetdata", methods=["POST"])
@guarded_api
def reset_data():
    message = mt.reset_transportation_data()
    return success(message, mt.get_system_statistics())


if __name__ == "__main__":
    transportation.run(debug=True)

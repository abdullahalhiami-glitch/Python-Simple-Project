'''
Docstring for Python_Projects.My_Project_Transportation_Tickets.Module_Transportation
This Module is For Some Information For The Transportation Program Used In The Main
Program
'''


# Declaring transportation data using a list of dictionaries
transportation_data = [
    {
        "Route_Id": "R1",
        "Destination": "Sana'a",
        "Capacity": 30,
        "Booked": []
    },
    {
        "Route_Id": "R2",
        "Destination": "Aden",
        "Capacity": 25,
        "Booked": []
    },
    {
        "Route_Id": "R3",
        "Destination": "Taiz",
        "Capacity": 20,
        "Booked": []
    },
    {
        "Route_Id": "R4",
        "Destination": "Ibb",
        "Capacity": 15,
        "Booked": []
    },
    {
        "Route_Id": "R5",
        "Destination": "Mukalla",
        "Capacity": 18,
        "Booked": []
    }
]

# Default ticket price
DEFAULT_TICKET_PRICE = 50

# 1. Helper Functions Find Route
def find_route(route_id):
    for route in transportation_data:
        if route["Route_Id"] == route_id:
            return route
    return None

# 2. Helper Functions Find Destination
def find_destination(destination):
    for route in transportation_data:
        if route["Destination"].lower() == destination.lower():
            return route
    return None

# 3. Add Route
def add_route(route_id, destination, capacity):
    if find_route(route_id):
        return f"Route {route_id} already exists."

    if find_destination(destination):
        return f"Destination {destination} already exists."

    if capacity < 1 or capacity > 30:
        return f"Capacity should be between 1 and 30, not {capacity}."

    route_data = {
        "Route_Id": route_id,
        "Destination": destination,
        "Capacity": capacity,
        "Booked": []
    }
    transportation_data.append(route_data)
    return f"Route {route_id} added successfully."

# 4. Get Available Routes
def get_available_routes():
    available_routes = []
    for route in transportation_data:
        if route["Capacity"] > 0:
            available_routes.append(route)
    return available_routes

# 5. Book Ticket
def book_ticket(route_id, passenger_name):
    route = find_route(route_id)
    if not route:
        return "Route not found."

    if passenger_name in route["Booked"]:
        return f"{passenger_name} already booked."

    if route["Capacity"] <= 0:
        return "No seats available."

    route["Booked"].append(passenger_name)
    route["Capacity"] -= 1
    return f"Booking confirmed for {passenger_name} on route {route_id}."

# 6. Cancel Booking
def cancel_booking(route_id, passenger_name):
    route = find_route(route_id)
    if not route:
        return "Route not found."

    if passenger_name not in route["Booked"]:
        return f"{passenger_name} has no booking."

    route["Booked"].remove(passenger_name)
    route["Capacity"] += 1
    return f"Booking cancelled for {passenger_name}."

# 7. Check Seat Availability
def check_seat_availability(route_id):
    route = find_route(route_id)
    if not route:
        return "Route not found."

    return route["Capacity"]

# 8. Get Passenger List
def get_passenger_list(route_id):
    route = find_route(route_id)
    if not route:
        return "Route not found."

    return route["Booked"]

# 9. Get Passenger List By Destination
def get_passenger_list_by_destination(destination):
    route = find_destination(destination)
    if not route:
        return "Destination not found."
    return route["Booked"]

# 10. Get Passenger List By Route
def get_passenger_list_by_route(route_id):
    route = find_route(route_id)
    if not route:
        return "Route not found."
    return route["Booked"]

# 11. Calculate Route Revenue
def calculate_route_revenue(route_id, ticket_price=None):
    if ticket_price is None:
        ticket_price = DEFAULT_TICKET_PRICE
    route = find_route(route_id)
    if not route:
        return "Route not found."

    return len(route["Booked"]) * ticket_price

# 12. Search by Destination
def search_route_by_destination(destination):
    results = []
    for route in transportation_data:
        if route["Destination"].lower() == destination.lower():
            results.append(route)
    return results

# 13. Print all Transportation Data
def print_all_routes():
    print(transportation_data)

# 14. View all destinations
def view_all_destinations():
    destinations = []
    for route in transportation_data:
        destinations.append(route["Destination"])
    return destinations

# 15. View all routes
def view_all_routes():  
    routes = []
    for route in transportation_data:
        routes.append(route["Route_Id"])
    return routes

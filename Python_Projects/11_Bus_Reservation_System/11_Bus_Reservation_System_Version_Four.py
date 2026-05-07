"""Docstring for Python_Projects.11_Bus_Reservation_System.11_Bus_Reservation_System"""

# Declaring transportation data using a list of dictionaries
transportation_data = [
    {
        "Route_Id": "R1",
        "Destination": "Sana'a",
        "Capacity": 30,
        "Booked": []
    }
]

# 1. Helper Functions

def find_route(route_id):
    for route in transportation_data:
        if route["Route_Id"] == route_id:
            return route
    return None


def find_destination(destination):
    for route in transportation_data:
        if route["Destination"] == destination:
            return route
    return None

# 2. Add Route

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

# 3. Get Available Routes

def get_available_routes():
    available_routes = []
    for route in transportation_data:
        if route["Capacity"] > 0:
            available_routes.append(route)
    return available_routes

# 4. Book Ticket

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

# 5. Cancel Booking

def cancel_booking(route_id, passenger_name):
    route = find_route(route_id)
    if not route:
        return "Route not found."

    if passenger_name not in route["Booked"]:
        return f"{passenger_name} has no booking."

    route["Booked"].remove(passenger_name)
    route["Capacity"] += 1
    return f"Booking cancelled for {passenger_name}."

# 6. Check Seat Availability

def check_seat_availability(route_id):
    route = find_route(route_id)
    if not route:
        return "Route not found."

    return route["Capacity"]

# 7. Get Passenger List

def get_passenger_list(route_id):
    route = find_route(route_id)
    if not route:
        return "Route not found."

    return route["Booked"]

# 8. Calculate Route Revenue

def calculate_route_revenue(route_id, ticket_price):
    route = find_route(route_id)
    if not route:
        return "Route not found."

    return len(route["Booked"]) * ticket_price

# 9. Search by Destination

def search_route_by_destination(destination):
    results = []
    for route in transportation_data:
        if route["Destination"].lower() == destination.lower():
            results.append(route)
    return results


if __name__ == "__main__":
    print(add_route("R2", "Ibb", 5))
    print(transportation_data)
    print(book_ticket("R2", "Abdullah"))
    print(book_ticket("R1", "Abdullah"))
    print(book_ticket("R2", "Abdu"))
    print(book_ticket("R2", "Abdah"))
    print(book_ticket("R1", "Abdull"))
    print(book_ticket("R1", "Abdull"))
    print(book_ticket("R1", "Abdull"))
    print(book_ticket("R2", "Abdull45"))
    print(book_ticket("R2", "Abdull12"))
    print(book_ticket("R3", "Abdull12"))
    print(cancel_booking("R1", "Abdull"))
    print(check_seat_availability("R1"))
    print(get_passenger_list("R2"))
    print(calculate_route_revenue("R2", 100))
    print(search_route_by_destination("Sana'a"))

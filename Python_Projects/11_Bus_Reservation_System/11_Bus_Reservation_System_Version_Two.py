'''
Docstring for Python_Projects.11_Bus_Reservation_System.11_Bus_Reservation_System
'''
#Declaring our Transoritation data using list and inside that list dictionaries
transportation_data = [
    {
        "Route_Id":'R1',
        "Destination": "Sana'a",
        "Capacity" : 30,
        "Booked": []
    }
]

# 1. Helper Functions
def find_route(route_id): # Checks the Route
    for Data in transportation_data:
        if Data["Route_Id"] == route_id:
            return route_id
    return None

def find_destination(destination): # Checks the Destination
    for Data in transportation_data:
        if Data["Destination"] == destination:
            return destination
    return None
# def add_capacity(capacity): # Checks the Destination
#     for Data in transportation_data:
#         Data["Capacity"] == capacity
#         return destination
 

#checking our Find_Route
# print(find_route("R1"))
# print(find_route("R2"))
# print(find_route("R3"))
#checking our Find_Destination
# print(find_destination("Sana'a"))
# print(find_destination("Ibb"))

#  2. Add Route
def add_route(route_id, destination, capacity):
    if find_route(route_id):# Checks if the route exists if it exists it return a message of existing Route_Id
        return f"Route {route_id} already exists."
    else:
        if find_destination(destination):# Checks if the destination exists if it exists it return a message of existing destination
            return f"Destination {destination} already exists."
        else:
            if capacity >= transportation_data[0]["Capacity"]:# Checks if the capacity greater than 30 if it greater than 30 it return a message of Capacity error than it accepts it if the capacity lower than 30
                return f"The Capacity should be lower than 30 not {capacity}."
            else:# Add all information if all conditions are true
                Data = {
                    "Route_Id": route_id,
                    "Destination": destination,
                    "Capacity": capacity,
                    "Booked": []
                }
                transportation_data.append(Data)
                return f"Transportion data was added successfully."
#checking the Add_Route Function
# print(add_route("R1","Ibb",15))
# print(add_route("R2","Sana'a",17))
# print(add_route("R2","Ibb",35))
print(add_route("R2","Ibb",5))
print(transportation_data)
# print(find_route("R2"))

# 3. Get Available Routes
def get_available_routes():
    available_routes = []
    for Data in transportation_data:
        if len(Data["Booked"]) < Data["Capacity"]:
            available_routes.append(Data)
    return available_routes
# print(get_available_routes())

    # 4. Book Ticket
def book_ticket(route_id, passenger_name):
    for Data in range(0,len(transportation_data)):
        # print(transportation_data[Data]["Route_Id"])
        # print(len(transportation_data))
        if transportation_data[Data]["Route_Id"] ==find_route(route_id):
            if passenger_name in transportation_data[Data]["Booked"]:
                return f"{passenger_name} already booked."
            else:
                available_seats = transportation_data[Data]["Capacity"] - len(transportation_data[Data]["Booked"])
                transportation_data[Data]["Booked"].append(passenger_name)
                # print(available_seats)
                # print(Data)
                if available_seats ==0:
                    return "No seats available."
                else:
                    return f"Booking confirmed for {passenger_name} on route {route_id}."
        else:
            continue
            return "Route not found."

#Checking the Book Ticket Function
print(book_ticket("R2", "Abdullah"))
print(book_ticket("R1", "Abdullah"))
print(book_ticket("R2", "Abdu"))
print(book_ticket("R2", "Abdah"))
print(book_ticket("R2", "Abdull"))
print(book_ticket("R2", "Abdull45"))
print(book_ticket("R2", "Abdull12"))

# 5. 








# class BusReservationSystem:
#     def __init__(self):
#         # Store all routes here
#         self.routes = []

#     # 🔍 Helper function (internal use)
#     def _find_route(self, route_id):
#         for route in self.routes:
#             if route["route_id"] == route_id:
#                 return route
#         return None

#     # ✅ 1. Add Route
#     def add_route(self, route_id, destination, capacity):
#         if self._find_route(route_id):
#             return f"Route {route_id} already exists."

#         route = {
#             "route_id": route_id,
#             "destination": destination,
#             "capacity": capacity,
#             "booked": []
#         }

#         self.routes.append(route)
#         return f"Route {route_id} added successfully."

#     # ✅ 2. Get Available Routes
#     def get_available_routes(self):
#         available = []

#         for route in self.routes:
#             if len(route["booked"]) < route["capacity"]:
#                 available.append(route)

#         return available

#     # ✅ 3. Book Ticket
#     def book_ticket(self, route_id, passenger_name):
#         route = self._find_route(route_id)

#         if not route:
#             return "Route not found."

#         if passenger_name in route["booked"]:
#             return f"{passenger_name} already booked."

#         if len(route["booked"]) >= route["capacity"]:
#             return "No seats available."

#         route["booked"].append(passenger_name)

#         return f"Booking confirmed for {passenger_name} on route {route_id}."

#     # ✅ 4. Cancel Booking
#     def cancel_booking(self, route_id, passenger_name):
#         route = self._find_route(route_id)

#         if not route:
#             return "Route not found."

#         if passenger_name not in route["booked"]:
#             return f"{passenger_name} has no booking."

#         route["booked"].remove(passenger_name)

#         return f"Booking cancelled for {passenger_name}."

#     # ✅ 5. Check Seat Availability
#     def check_seat_availability(self, route_id):
#         route = self._find_route(route_id)

#         if not route:
#             return "Route not found."

#         available_seats = route["capacity"] - len(route["booked"])
#         return available_seats

#     # ✅ 6. Get Passenger List
#     def get_passenger_list(self, route_id):
#         route = self._find_route(route_id)

#         if not route:
#             return "Route not found."

#         return route["booked"]

#     # ✅ 7. Calculate Revenue
#     def calculate_route_revenue(self, route_id, ticket_price):
#         route = self._find_route(route_id)

#         if not route:
#             return "Route not found."

#         revenue = len(route["booked"]) * ticket_price
#         return revenue

#     # ✅ 8. Search by Destination
#     def search_route_by_destination(self, destination):
#         results = []

#         for route in self.routes:
#             if route["destination"].lower() == destination.lower():
#                 results.append(route)

#         return results

# system = BusReservationSystem()

# system.add_route("R1", "Sanaa", 2)

# print(system.book_ticket("R1", "Ali"))
# print(system.book_ticket("R1", "Ahmed"))
# print(system.book_ticket("R1", "John"))  # Should fail (full)

# print(system.check_seat_availability("R1"))

# print(system.get_passenger_list("R1"))

# print(system.calculate_route_revenue("R1", 100))

# system.cancel_booking("R1", "Ali")

# print(system.get_available_routes())
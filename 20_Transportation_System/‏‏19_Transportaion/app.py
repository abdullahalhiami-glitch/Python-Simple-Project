from flask import Flask,render_template,request,jsonify
import Module_Transportation as mt

#calling our Dictionary list from our Module
mt.transportation_data
exit = True
#declare our varaibles by referencing the Flask(__name__)
transportation = Flask(__name__)

@transportation.route('/')
def home():
    return render_template('index.html', Transportation_System="Transportation-System", name="Al-Hiami Transportation App", Transport = mt.transportation_data, exitpro = exit )

@transportation.route('/about')
def about():
    return render_template('about.html', Transportation_System="Transportation-System-about", name="About Al-Hiami Transportation App" )

@transportation.route('/contactus')
def contactus():
    return render_template('contactus.html', Transportation_System="Transportation-System-contactus", name="Contact Al-Hiami Transportation App" )

@transportation.route('/information')
def information():
    return render_template('information.html', Transportation_System="Transportation-System-information", name="Summary Al-Hiami Transportation App" )

# API Endpoints for Transportation System for searching a route
@transportation.route('/searchroute', methods=['POST'])
def find_route():
    # Find a route by its ID
    route_id = request.form.get('route_id')
    route = mt.find_route(route_id)
    if route:
        return jsonify(route)
    else:
        return jsonify({"message": "Route not found."}), 404
    
# API Endpoints for Transportation System for searching a destination
@transportation.route('/searchdestination', methods=['POST'])
def find_destination():
    # Find a destination by its ID for searching
    try:
        destination_id = request.form.get('destination_id')
        destination = mt.find_destination(destination_id)
        if destination:
            return jsonify(destination)
        else:
            return jsonify({"message": "Destination not found."}), 404
    except Exception as e:
        return jsonify({"message": "Error searching destination."}), 500
    
# API Endpoints for Transportation System for adding a new route
@transportation.route('/addroute', methods=['POST'])
def add_route():
    # Add a new route
    try:
        route_id = request.form.get('route_id')
        destination = request.form.get('destination')
        capacity = int(request.form.get('capacity'))
        result = mt.add_route(route_id, destination, capacity)
        return jsonify({"message": result})
    except Exception as e:
        return jsonify({"message": "Error adding route."}), 500

# API Endpoints for Transportation System for getting available routes
@transportation.route('/availableroutes', methods=['GET'])
def get_available_routes():
    # Get all available routes
    routes = mt.get_available_routes()
    return jsonify(routes)

# API Endpoints for Transportation System for booking a ticket
@transportation.route('/bookticket', methods=['POST'])
def book_ticket():
    # Book a ticket for a route
    try:
        route_id = request.form.get('route_id')
        passenger_name = request.form.get('passenger_name')
        result = mt.book_ticket(route_id, passenger_name)
        return jsonify({"message": result})
    except Exception as e:
        return jsonify({"message": "Error booking ticket."}), 500
    

@transportation.route('/cancelbooking', methods=['POST'])
def cancel_booking():
    # Cancel a booking for a route
    try:
        route_id = request.form.get('route_id')
        passenger_name = request.form.get('passenger_name')
        result = mt.cancel_booking(route_id, passenger_name)
        return jsonify({"message": result})
    except Exception as e:
        return jsonify({"message": "Error canceling booking."}), 500

@transportation.route('/exit', methods=['POST'])
def exit_app():
    global exit
    exit = False
    return jsonify({"message": "Exiting the application."})

@transportation.route('/restart', methods=['POST'])
def restart_app():
    global exit
    exit = True
    return jsonify({"message": "Restarting the application."})

@transportation.route('/status', methods=['GET'])
def check_status():
    global exit
    status = "Running" if exit else "Exited"
    return jsonify({"status": status})

@transportation.route('/checkseatavailability', methods=['POST'])
def check_seat_availability():
    # Check seat availability for a route
    try:
        route_id = request.form.get('route_id')
        result = mt.check_seat_availability(route_id)
        return jsonify({"available_seats": result})
    except Exception as e:
        return jsonify({"message": "Error checking seat availability."}), 500
    
@transportation.route('/getpassengerlist', methods=['POST'])
def get_passenger_list():
    # Get the passenger list for a route
    try:
        route_id = request.form.get('route_id')
        result = mt.get_passenger_list(route_id)
        return jsonify({"passenger_list": result})
    except Exception as e:
        return jsonify({"message": "Error getting passenger list."}), 500
    
@transportation.route('/getpassengerlistbydestination', methods=['POST'])
def get_passenger_list_by_destination():
    # Get the passenger list for a destination
    try:
        destination = request.form.get('destination')
        result = mt.get_passenger_list_by_destination(destination)
        return jsonify({"passenger_list": result})
    except Exception as e:
        return jsonify({"message": "Error getting passenger list by destination."}), 500

@transportation.route('/getpassengerlistbyroute', methods=['POST'])
def get_passenger_list_by_route():
    # Get the passenger list for a route
    try:
        route_id = request.form.get('route_id')
        result = mt.get_passenger_list_by_route(route_id)
        return jsonify({"passenger_list": result})
    except Exception as e:
        return jsonify({"message": "Error getting passenger list by route."}), 500
    
@transportation.route('/calculaterouterevenue', methods=['POST'])
def calculate_route_revenue():
    # Calculate revenue for a route
    try:
        route_id = request.form.get('route_id')
        result = mt.calculate_route_revenue(route_id)
        return jsonify({"revenue": result})
    except Exception as e:
        return jsonify({"message": "Error calculating route revenue."}), 500

@transportation.route('/searchroutebydestination', methods=['POST'])
def search_route_by_destination():
    # Search for routes by destination
    try:
        destination = request.form.get('destination')
        result = mt.search_route_by_destination(destination)
        return jsonify({"routes": result})
    except Exception as e:
        return jsonify({"message": "Error searching routes by destination."}), 500
    
@transportation.route('/viewalldestinations', methods=['GET'])
def view_all_destinations():
    # View all destinations
    try:
        result = mt.view_all_destinations()
        return jsonify({"destinations": result})
    except Exception as e:
        return jsonify({"message": "Error viewing all destinations."}), 500

@transportation.route('/viewallroutes', methods=['GET'])
def view_all_routes():
    # View all routes
    try:
        result = mt.view_all_routes()
        return jsonify({"routes": result})
    except Exception as e:
        return jsonify({"message": "Error viewing all routes."}), 500


if __name__ == '__main__':
    transportation.run(debug=True)
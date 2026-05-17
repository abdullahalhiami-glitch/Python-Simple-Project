from flask import Flask, request, jsonify, render_template
import restaurants as re

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/restaurants', methods=['GET'])
def get_all():
    """9. View all restaurants"""
    result = re.get_all_restaurants()
    return jsonify({"result": result})

@app.route('/restaurants', methods=['POST'])
def add_restaurant():
    """1. Add a new restaurant"""
    data = request.get_json()
    if not data or 'name' not in data or 'cuisine' not in data:
        return jsonify({"error": "Please provide 'name' and 'cuisine' in JSON format"}), 400
    
    name = data['name']
    cuisine = data['cuisine']
    result = re.add_restaurant(name, cuisine)
    return jsonify({"result": result})

@app.route('/restaurants/<name>', methods=['GET'])
def get_info(name):
    """3. View restaurant info"""
    result = re.get_restaurant_info(name)
    return jsonify({"result": result})

@app.route('/restaurants/<name>/rating', methods=['POST'])
def add_rating(name):
    """2. Add a rating"""
    data = request.get_json()
    if not data or 'rating' not in data:
        return jsonify({"error": "Please provide 'rating' in JSON format"}), 400
    
    rating = data['rating']
    result = re.add_rating(name, rating)
    return jsonify({"result": result})

@app.route('/restaurants/<name>/average', methods=['GET'])
def get_average(name):
    """4. Calculate average rating"""
    result = re.calculate_average_rating(name)
    return jsonify({"result": result})

@app.route('/restaurants/search', methods=['GET'])
def search_by_cuisine():
    """5. Search restaurants by cuisine"""
    cuisine = request.args.get('cuisine')
    if not cuisine:
        return jsonify({"error": "Please provide 'cuisine' query parameter"}), 400
    
    result = re.search_by_cuisine(cuisine)
    return jsonify({"result": result})

@app.route('/restaurants/top', methods=['GET'])
def top_rated():
    """6. View top rated restaurants (by min rating)"""
    min_rating = request.args.get('min_rating')
    if not min_rating:
        return jsonify({"error": "Please provide 'min_rating' query parameter"}), 400
    
    result = re.get_top_rated_restaurants(min_rating)
    return jsonify({"result": result})

@app.route('/restaurants/<name>', methods=['PUT'])
def update_cuisine(name):
    """7. Update restaurant cuisine"""
    data = request.get_json()
    if not data or 'cuisine' not in data:
        return jsonify({"error": "Please provide 'cuisine' in JSON format"}), 400
    
    new_cuisine = data['cuisine']
    result = re.update_restaurant_cuisine(name, new_cuisine)
    return jsonify({"result": result})

@app.route('/restaurants/<name>', methods=['DELETE'])
def delete_restaurant(name):
    """8. Delete a restaurant"""
    result = re.delete_restaurant(name)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)

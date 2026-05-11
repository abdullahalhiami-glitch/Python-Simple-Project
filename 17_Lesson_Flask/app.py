from flask import Flask 
pharmacy = Flask(__name__)

@pharmacy.route('/')
def home():
    return '<h1><center>Welcome to the Pharmacy!</center></h1>'

@pharmacy.route('/contact')
def contact():
    return '<h1><center>Contact us at: +967 776 709 263</center></h1>'

@pharmacy.route('/about')
def about():
    return '<h1><center>We are a local pharmacy dedicated to providing quality healthcare products and services to our community.</center></h1>'

if __name__ == '__main__':
    pharmacy.run(debug=True)

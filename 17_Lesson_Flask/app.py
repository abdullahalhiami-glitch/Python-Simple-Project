# from flask import Flask 
# pharmacy = Flask(__name__)

# @pharmacy.route('/')
# def home():
#     return '<h1><center>Welcome to the Pharmacy!</center></h1>'

# @pharmacy.route('/contact')
# def contact():
#     return '<h1><a href="https://wa.me/967776709263>My Phone number</a></h1>'

# @pharmacy.route('/about')
# def about():
#     return '<h1><center>We are a local pharmacy dedicated to providing quality healthcare products and services to our community.</center></h1>'

# if __name__ == '__main__':
#     pharmacy.run(debug=True)

myDegree = ['Mak','kli','PhD']

from flask import Flask, render_template, request
pharmacy = Flask(__name__)

@pharmacy.route('/')
def home():
    return render_template('index.html', GasStation='Gas-Station', name='Abd-Gas Station', degree=myDegree)

@pharmacy.route('/about')
def contact():
    return render_template('about.html', GasStation='Gas-Station-about', num1=5, num2=8)

@pharmacy.route('/contactus')
def about():
    return render_template('contactus.html', GasStation='Gas-Station-contactus')

@pharmacy.route('/information')
def information():
    return render_template('information.html', GasStation='Gas-Station-information')

@pharmacy.route('/submit')
def submit():
    ## this is by using the get method not encrypted data everyone can see it
    username = request.args.get('name')
    age=request.args.get('age')
    if username and age:
        if int(age) < 18:
            return f'<h1>You Are Chiled</h1> <h2>Hello, {username}!</h2>'
        else:
            return f'<h1>You Are Adult</h1> <h2>your age is, {age}!</h2>'
    else:
        return f'<h1>Form not submitted</h1>'
    # return f'<h1>form submitted successfuly</h1><p>Hello {username}!</p>'

    #using Post Method
    # username=request.form.get('name')
    # age=request.form.get('age')
    # if username and age:
    #     if int(age) < 18:
    #         return f'<h1>You Are Chiled</h1> <h2>Hello, {username}!</h2>'
    #     else:
    #         return f'<h1>You Are Adult</h1> <h2>Hello, {username}!</h2>'
    # else:
    #     return f'<h1>Form not submitted</h1>'

if __name__ == '__main__':
    pharmacy.run(debug=True)

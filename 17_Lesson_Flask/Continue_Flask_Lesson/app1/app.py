from flask import Flask, render_template,request

#Here is like we make a reference for the pharmecy
pharmecy=Flask(__name__)

#dealing with data types using python and html
my_dgree=['BSc','MSc','PhD']

#function using the flask method for declaring a function for the home page
#and this symbol '/' tells us we are in the home page 
@pharmecy.route('/')
def home():
    return render_template('index.html', pagetitle='Pharmacy',name='Ms')

#function using the flask method for declaring a function for the about page
#and this symbol '/about' tells us we are in the about page 
@pharmecy.route('/about')
def about():
    return render_template('about.html', pagetitle='Pharmacy-about', degrees=my_dgree)

#function using the flask method for declaring a function for the contact page
#and this symbol '/contact' tells us we are in the contact page
@pharmecy.route('/contact')
def contact():
    return render_template('contactus.html', pagetitle='Pharmacy-contact' )


@pharmecy.route('/submit', methods=['POST'] )
def submit():
    #using Get Methos
    # username=request.args.get('name')
    # age=request.args.get('age')
    
    #using Post Method
    username=request.form.get('name')
    age=request.form.get('age')
    if username and age:
        if int(age) < 18:
            return f'<h1>You Are Chiled</h1> <h2>Hello, {username}!</h2>'
        else:
            return f'<h1>You Are Adult</h1> <h2>Hello, {username}!</h2>'
    else:
        return f'<h1>Form not submitted</h1>'



if __name__ == '__main__':
    pharmecy.run(debug=True)
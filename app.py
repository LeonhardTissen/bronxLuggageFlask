# Importing all of the dependencies
from flask import Flask, render_template
import os
from products import products

# This is the port number the app runs on
port = 5065

# Creating the app, it will be referenced in all of the routes and when starting the server
app = Flask(__name__)

# The homepage
@app.route('/')
def homepage():
    return render_template('index.html.j2')

# The catalogue
@app.route('/catalogue')
def catalogue():
    return render_template('catalogue.html.j2')

# The contact page
@app.route('/contact')
def contact():
    return render_template('contact.html.j2')

# The about page
@app.route('/about')
def about():
    return render_template('about.html.j2')

# The login page
@app.route('/login')
def login():
    return render_template('login.html.j2')

# The product listings
@app.route('/products/<category>')
def productlistings(category):
    if category.lower() not in products:
        return render_template('404.html.j2')
    
    selected_category = products[category.lower()]
    return render_template('products.html.j2', products = selected_category, section = category.capitalize())

# A single product
@app.route('/products/<category>/<product>')
def singleproduct(category, product):
    if category.lower() not in products:
        return render_template('404.html.j2')
    
    selected_product = None

    selected_category = products[category.lower()]
    for item in selected_category:
        if item[0] == product:
            selected_product = item
    
    if selected_product == None:
        return render_template('404.html.j2')

    return render_template('singleproduct.html.j2', category = category, product = selected_product, section = category.capitalize())

# The 404 page
@app.errorhandler(404)
def errorhandler(e):
    print(e)
    return render_template('404.html.j2')

# Start hosting the server
app.run(host='0.0.0.0', port=port, debug=True)
# Importing all of the dependencies
from flask import Flask, render_template
import os
import numpy as np

# This is the port number, defaults to 5000 if no environment variable is found
port = int(os.getenv('PORT', 5000))

products = {
    'rimowa': [
        ['Rimowa Essential', 'bagblack', '2,000'],
        ['Strong Travels', 'black', '1,800'],
        ['Blueness', 'bluebag', '2,400'],
        ['Sage Serrano', 'green', '1,200'],
        ['Pastel Yellow', 'suitcase', '1,700'],
        ['Pretty Pink', 'pink', '3,000'],
        ['Round Wrap', 'round', '1,000'],
        ['Bright Days', 'yellow', '4,110'],
        ['Simple Side', 'medium', '1,700']
    ],
    'globetrotter': [
        ['Boss Black', 'blackcase', '2,000'],
        ['Bold peach', 'fantastic', '5,800'],
        ['Classic English', 'browncase', '2,400'],
        ['Woven Women', 'brownpurse', '1,200'],
        ['Hard-cover Hold', 'handback', '8,100'],
        ['Sheepish', 'sheep', '3,400'],
        ['I Have Some Baggage', 'suitcase', '5,000'],
        ['Turtle Takes', 'turtle', '3,700']
    ]
}

# Creating the app, it will be referenced in all of the routes and when starting the server
app = Flask(__name__)

# The homepage
@app.route('/')
def homepage():
    return render_template('index.html')

# The catalogue
@app.route('/catalogue')
def catalogue():
    return render_template('catalogue.html')

# The product listings
@app.route('/products/<category>')
def productlistings(category):
    selected_category = products[category.lower()]
    return render_template('products.html', products = selected_category, section = category.capitalize())

# A single product
@app.route('/products/<category>/<product>')
def singleproduct(category, product):
    selected_category = products[category.lower()]
    for item in selected_category:
        if item[0] == product:
            selected_product = item

    return render_template('singleproduct.html', category = category, product = selected_product, section = category.capitalize())

# The 404 page
@app.errorhandler(404)
def errorhandler(e):
    print(e)
    return render_template('404.html')

# Start hosting the server
app.run(host='0.0.0.0', port=port, debug=True)
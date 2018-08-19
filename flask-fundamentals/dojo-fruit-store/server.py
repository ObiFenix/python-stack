'''               [ Assignment: Dojo Fruit Store  ]
Objectives:
===================================================
<>  Shall building a server with Flask from scratch
<>  Shall pass paas information to the routes
<>  Shall generate different http responses url requests
========================================================'''

import datetime
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

quanities = [1,2,3,4]
stack = [{'Apple':1}, {'Raspberry':0}, {'Strawberry':0}, {'Blackberry':0}]

@app.route('/')
def index():
    return render_template("index.html", quanities=quanities, fruits=stack)

@app.route('/checkout', methods=['POST'])
def checkout():
    print("\n\n")
    new_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    _stack = [
        { 'Apple'     : int(request.form['apple']) },
        { 'Blackberry': int(request.form['blackberry']) },
        { 'Raspberry' : int(request.form['raspberry']) },
        { 'Strasberry': int(request.form['strawberry']) }
    ]
    _buyer = { 
        'firstname' : request.form['first_name'],
        'lastname'  : request.form['last_name'], 
        'id'        : request.form['student_id']
    }
    return render_template("checkout.html", student=_buyer, student_stack=_stack, date=new_date)

@app.route('/fruits')
def fruits():
    fruits_in_stack = []
    for item in stack:
        for key in item:
            fruits_in_stack.append(key.lower())
    print ("\n\n\n\n",fruits_in_stack)
    return render_template("fruits.html", fruits=fruits_in_stack)

if __name__=="__main__":
    app.run(debug=True)
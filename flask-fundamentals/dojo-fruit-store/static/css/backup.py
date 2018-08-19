'''               [ Assignment: Dojo Fruit Store  ]
Objectives:
===================================================
<>  Shall building a server with Flask from scratch
<>  Shall pass paas information to the routes
<>  Shall generate different http responses url requests
========================================================'''

from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

quanities = [1,2,3,4]
fruits = {'apple':1, 'raspberry':0, 'strawberry':0, 'blackberry':0 }

@app.route('/')
def index():
    return render_template("index.html", quanities=quanities, fruits=fruits)

@app.route('/checkout', methods=['POST'])
def checkout():
   
    apple      = int(request.form['apple'])
    first_name = request.form['first_name']
    last_name  = request.form['last_name']
    student_id = request.form['student_id']
    total      = apple+strawberry+blackberry+raspberry
    return render_template(
        "checkout.html",
        apple     = int(request.form['apple']),
        blackberry= int(request.form['blackberry']),
        raspberry = int(request.form['raspberry']),
        strasberry= int(request.form['strawberry']),
        first_name= first_name,
        last_name = last_name, 
        student_id=student_id)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)
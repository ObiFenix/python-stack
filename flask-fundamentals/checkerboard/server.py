#                      [ Assignment: Checkerboard  ]
'''
Objectives:
===================================================
<>  Shall building a server with Flask from scratch
<>  Shall pass paas information to the routes
<>  Shall generate different http responses url requests:
========================================================='''

# import the Flask libray
from flask import Flask, render_template

# Backend server setup
app = Flask (__name__)
print (__name__)

@app.route('/')
def home ():
    return render_template('index.html', rows=10, cols=10)

@app.route('/<x>/<y>')
def chooseGrid (x, y):
    return render_template('index.html', rows=int(x), cols=int(y))

if __name__ == '__main__':
    app.run( debug = True )

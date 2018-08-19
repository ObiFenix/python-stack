#                      [ Assignment: Understanding Routing  ]

'''
Objectives:
===================================================
<>  Shall building a server with Flask from scratch
<>  Shall pass paas information to the routes
<>  Shall generate different http responses url requests:
========================================================='''

from flask import Flask, render_template   # import the Flask libray
app = Flask (__name__)

print (__name__)                            # Not required though, just for fun

@app.route ( '/play' )
def index ():
    return render_template('index.html', times=3, color='lightblue')

@app.route ( '/play/<times>' )
def level (times):
    return render_template('index.html', times=int(times), color='lightblue')

@app.route ('/play/<times>/<color>')
def assigncolor (times, color):
    return render_template('index.html', times=int(times), color=color)


if __name__ == '__main__':
    app.run( debug = True )

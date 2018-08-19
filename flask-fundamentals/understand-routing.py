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

@app.route ( '/' )
def hello_worlds ():
    return 'Hellow World'

@app.route ( '/dojo' )
def success ():
    return 'Dojo'

@app.route ( '/say/<name>' )
def say (name):
    return "Hi " + name

@app.route ('/repeat/<id>/<name>')
def repeat (name, id):
    return f"Hello {name}  {id}\n\n" * int(id)
    

if __name__ == '__main__':
    app.run( debug = True )
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
    dictList = [
        { 'firstname': 'Riya',    'lastname': 'Wasnik'},
        { 'firstname': 'Juliana', 'lastname': 'Stakland'},
        { 'firstname': 'Felecia', 'lastname': 'Pittman'},
        { 'firstname': 'Authman', 'lastname': 'Apatira'},
        { 'firstname': 'Shiraz',  'lastname': 'Sultan'},
        { 'firstname': 'Josh',    'lastname': 'Reese'},
        { 'firstname': 'Matt',    'lastname': 'Tucker'}
    ]
    return render_template ('index.html', students=dictList, rows=len(dictList), cols=len(dictList[0].keys())+1)

@app.route('/<first>/<last>')
def add_person (first, last):
    dictList.push({first, last})
    return render_template('index.html', students=dictList, rows=len(dictList), cols=len(dictList[0].keys())+1)


if __name__ == '__main__':
    app.run( debug = True )

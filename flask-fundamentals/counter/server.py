#                      [ Assignment: Dojo Survey  ]
'''
Objectives:
===================================================
<>  Shall building a server with Flask from scratch
<>  Shall pass paas information to the routes
<>  Shall generate different http responses url requests:
========================================================='''

''' import the Flask libray '''
#    module       Class     Method         Method    object
from flask import Flask, render_template, redirect,  request, session

''' Backend server setup '''
# Object
app = Flask (__name__)
app.secret_key = 'counter'

@app.route ('/')
def index ():
    if ('count' in session):    session['count'] += 1
    else:                       session['count'] = 1
    # Debugging in terminal
    # ====================
    print (session)
    print(request.cookies)
    #=====================
    return render_template("index.html", counter=session['count'])

@app.route ('/newsession')
def session_counter ():
    # Debugging in terminal
    # =====================
    underline = "\n"
    underline = "-" * 20
    session['count'] += 1
    print ('Session Counter Info:\n%s\n' % underline)
    print ('Session terminated was session ', session['count'],'\n\n')
    # ================================================================
    return redirect ('/')

@app.route ('/sessionreset')
def session_reset ():
    end_session = session.pop('count')
    # Debugging in terminal
    # =====================
    underline = "-" * 20
    print ('Session Counter Info:\n%s\n' % underline)
    print (f'Session terminated was session #{end_session}\n\n')
    # =========================================================
    return redirect ('/')     # Redirects back to index '/'

if __name__ == '__main__':    # Run the server applicatin
    app.run (debug = True)

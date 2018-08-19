# ========================
# Import Required Packages
# ========================
# shall mport the function connectToMySQL from mysqlconnection.py
from flask import Flask, render_template, redirect, request
from mysqlconnection import connectToMySQL

app = Flask(__name__)

# ======================
# Stableshing Connection 
# ======================
# <> shall invoke the connectToMySQL function and 
#    pass it the name of the database we're using
# <> shall store an instance of MySQLConnection return 
#    from connectToMySQL
mysql = connectToMySQL('mydb')


# ===============
# Required Routes
# ===============

# <> Allow users to fetch records
@app.route('/')
def friends():
  
    all_friends = mysql.query_db("SELECT * FROM friends")
    print("\n\nFetched all friends\n-------------------\n")
    print(all_friends)
    return render_template('friends.html', friends=all_friends)


# Allow users to insert records
@app.route('/create_friend', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation) VALUES (%(first_name)s, %(last_name)s, %(occupation)s);"
    data = {
        'first_name': request.form['first_name'],
        'last_name':  request.form['last_name'],
        'occupation': request.form['occupation']
    }
    mysql.query_db(query, data)
    return redirect('/')


# shall invoke the query_db method for debugging purposes
# print("all the users", mysql.query_db("SELECT * FROM friends;"))
if __name__ == "__main__":
    app.run(debug=True)

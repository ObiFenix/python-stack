from flask import Flask

# <> shall mport the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL

app = Flask(__name__)

# <> shall invoke the connectToMySQL function and pass it the name of the database we're using
# <> shall store an instance of MySQLConnection return from connectToMySQL
mysql = connectToMySQL('mydb')

# shall invoke the query_db method
print("all the users", mysql.query_db("SELECT * FROM users;"))
if __name__ == "__main__":
    app.run(debug=True)
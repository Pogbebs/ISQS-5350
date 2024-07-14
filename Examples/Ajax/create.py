#!/Users/billkaduru/anaconda3/bin/python3
import cgi
import cgitb
import mysql.connector
import bcrypt
import json

cgitb.enable()  # Enable for debugging

form = cgi.FieldStorage()

# Retrieve data from fields
username = form.getvalue('username')
password = form.getvalue('password')

# Prepare the Content-type header
print("Content-type: application/json\r\n")

response = {}

if username and password:  # Check if username and password are provided
    # Hash the password
    password_bytes = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    # Connect to the database
    mydb = mysql.connector.connect(
    host="localhost",
    user="isqs5350",
    password="isqs5350Password!",
    database="isqs5350"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO user (UserName, Password) VALUES (%s, %s)"
    val = (username, hashed_password)
    try:
        mycursor.execute(sql, val)
        mydb.commit()
        response["success"] = True
        response["message"] = "User added successfully!"
    except mysql.connector.Error as err:
        response["success"] = False
        response["message"] = f"Error on insert: {str(err)}"

    mycursor.close()
    mydb.close()
else:
    response["success"] = False
    response["message"] = "Missing username or password."

print(json.dumps(response))

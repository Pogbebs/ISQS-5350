#!/Users/billkaduru/anaconda3/bin/python3
import cgi
import mysql.connector
import bcrypt
import json

print("Content-Type: application/json\n")  # Remember to add newline

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
username = form.getvalue('username')
password = form.getvalue('password')

# Initialize the response dictionary
response = {}

# Connect to your MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="isqs5350",
  password="isqs5350Password!",
  database="isqs5350"
)

mycursor = mydb.cursor()

# SQL query to get the hashed password of the user
sql = "SELECT Password FROM user WHERE UserName = %s"
val = (username,)

try:
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        # Fetch the stored hash
        stored_hash = result[0]
        
        # Comparing submitted password after hashing with stored hash
        if bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
            response["success"] = True
            response["message"] = "Login successful"
        else:
            response["success"] = False
            response["message"] = "Password incorrect"
    else:
        # Username not found
        response["success"] = False
        response["message"] = "No user found with that username"
except mysql.connector.Error as err:
    response["success"] = False
    response["message"] = f"Database error: {err}"

# Make sure to close the cursor and connection
mycursor.close()
mydb.close()

# Send the JSON response
print(json.dumps(response))

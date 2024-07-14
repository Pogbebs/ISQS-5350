#! C:\Python312\python.exe
import cgi
import mysql.connector
import bcrypt

form = cgi.FieldStorage() 

# Retrieve data from "Get" fields
username = form.getvalue('username')
password  = form.getvalue('password')
email = form.getvalue('email')

# Hash the password
password_bytes = password.encode('utf-8')
hashedpassword = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello Somebody</title>")
print ("</head>")
print ("<body>")

mydb = mysql.connector.connect(
  host="localhost",
  user="isqs5350",
  password="isqs5350Password!",
  database="isqs5350"
)

mycursor = mydb.cursor()

sql = "INSERT INTO user (UserName, Email, Password) VALUES ( %s, %s, %s)"
val = (username, email, hashedpassword)
try:
  mycursor.execute(sql, val)
  mydb.commit()
  print("User added successfully!")
  print("<br><br><a href='read.py'>View List</a>")
  print("<br><br><a href='index.html'>Crud Home</a>")
except mysql.connector.Error as err:
  print("Error on insert: {}".format(err))
print ("</body>")
print ("</html>")



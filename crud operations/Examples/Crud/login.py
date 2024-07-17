#! C:\Users\prais\AppData\Local\Programs\Python\Python312\python.exe
import cgi
import mysql.connector
import bcrypt

form = cgi.FieldStorage() 

# Retrieve data from "Get" fields
username = form.getvalue('username')
password  = form.getvalue('password')

print("Content-type:text/html\r\nSet-Cookie: SayHello=" +username +"; Path=/; Expires=Wed, 21 Oct 2024 07:28:00 GMT; SameSite=Lax\r\n")
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

sql = "Select username, password from user where UserName = %s"
val = (username, )
try:
  mycursor.execute(sql, val)
  myresult = mycursor.fetchall()
  if myresult:
    retrieved_password = myresult[0][1]
    if bcrypt.checkpw(password.encode('utf-8'), retrieved_password.encode('utf-8')):
      print("User found with that username and password")
      print("<br>User logged in successfully!")
    else:
      print("Password incorrect")
  else:
    print("No user found with that username")
  print("<br><br><a href='read.py'>View List</a>")
  print("<br><br><a href='index.html'>Crud Home</a>")
except mysql.connector.Error as err:
  print("Error on insert: {}".format(err))
print ("</body>")
print ("</html>")



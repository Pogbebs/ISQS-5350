#! C:\Users\prais\AppData\Local\Programs\Python\Python312\python.exe
import cgi
import mysql.connector
import bcrypt

form = cgi.FieldStorage() 

# Retrieve data from "Get" fields
id = form.getvalue('id2delete')

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

sql = "Delete from user where id = %s"
val = (id,)
try:
  mycursor.execute(sql, val)
  mydb.commit()
  print("User deleted successfully!")
  print("<br><br><a href='read.py'>View List</a>")
except mysql.connector.Error as err:
  print("Error on delete: {}".format(err))
print ("</body>")
print ("</html>")
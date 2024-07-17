#! C:\Users\prais\AppData\Local\Programs\Python\Python312\python.exe
import cgi, cgitb 
import mysql.connector


print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>PHP Crud</title>")
print ("</head>")
print ("<body>")

mydb = mysql.connector.connect(
  host="localhost",
  user="isqs5350",
  password="isqs5350Password!",
  database="isqs5350"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM user")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  print("<br>")
 
print("<br><br><a href='index.html'>Crud Home</a>")  
print("</body>")
print("</html>")
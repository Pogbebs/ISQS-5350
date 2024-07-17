#!/Users/billkaduru/anaconda3/bin/python3
import cgi
import cgitb 
import mysql.connector
import html  # Import the html module for escaping HTML entities

# Enable detailed error messages
cgitb.enable()

# Set the content type to HTML
print("Content-type:text/html\r\n")

# Begin the HTML response
print("""
<html>
<head>
    <title>User Table</title>
    <style>
        table, th, td {
            border: 1px solid black;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
        }
    </style>
</head>
<body>
    <h2>User Table</h2>
    <table>
        <tr>
            <th>ID</th>
            <th>UserName</th>
            <th>Email</th>
        </tr>
""")

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="isqs5350",
  password="isqs5350Password!",
  database="isqs5350"
)

# Create a cursor to execute the SQL query
mycursor = mydb.cursor()

# Execute the SQL query to select all users
mycursor.execute("SELECT * FROM user")

# Fetch all the rows returned by the database query
myresult = mycursor.fetchall()

# Iterate over the rows to print each one in an HTML table row
for row in myresult:
    print("<tr>")
    print(f"<td>{html.escape(str(row[0]))}</td>")  # Username, safely escaped
    print(f"<td>{html.escape(str(row[1]))}</td>")  # Email, safely escaped
    # Don't escape password if you're showing the hashed version, but generally avoid showing passwords in HTML.
    print(f"<td>{html.escape(str(row[2]))}</td>")  # Password (hashed), safely escaped
    print("</tr>")

# End the HTML response
print("""
    </table>
    <br><br><a href='index.html'>Home</a>

</body>
</html>
""")

# Close the cursor and database connection
mycursor.close()
mydb.close()

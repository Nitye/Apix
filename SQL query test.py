import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', passwd='Darknite07', database='hotel')
mycursor = mydb.cursor()
room_occupant = 'Rahul Jain'
sql = "SELECT room_number FROM bookings WHERE name = 'Rahul Jain'"
mycursor.execute(sql)
myresult = mycursor.fetchone()

print(myresult)
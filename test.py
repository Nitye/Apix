import mysql.connector
import datetime

mydb = mysql.connector.connect(host='localhost', user='root', passwd='Darknite07', database='hotel')
mycursor = mydb.cursor()

def add_booking():
    sqlform = "Insert into bookings(name,phone,checkin,checkout,amount,room_number,pretotal) values(%s,%s,%s,%s,%s,%s,%s)"
    new_name = str(input("Enter name of new guest:"))
    new_phone = str(input("Enter Phone number of guest:"))
    chin = str(input("Enter Check-in Date(yyyy-mm-dd):"))
    new_chin = datetime.datetime.strptime(chin, "%Y-%m-%d")
    chout = str(input("Enter Check-out Date(yyyy-mm-dd):"))
    new_chout = datetime.datetime.strptime(chout, "%Y-%m-%d")
    price_per_day = 5000
    tax = 20/100
    date_1 = new_chin
    date_2 = new_chout
    delta_diff = date_2-date_1
    number_of_days = int(f'{delta_diff.days}')
    pretotal = (number_of_days*price_per_day)
    amount_payable = pretotal + (tax*pretotal)
    room_no = int(input("Enter available room number:"))
    entries = [(new_name, new_phone, new_chin, new_chout, amount_payable, room_no, pretotal)]
    mycursor.executemany(sqlform, entries)
    print("Booking added")
    mydb.commit()

def find_room():
    l = ["Rahul Jain", "Nitye Gupta", "Shubham Garg", "Amir Khan"]
    room_occupant = str(input("Enter name of room occupant:"))
    if room_occupant == l[0]:
        query = "Select room_number from bookings where name = 'Rahul Jain'"
    elif room_occupant == l[1]:
        query = "Select room_number from bookings where name = 'Nitye Gupta'"
    elif room_occupant == l[2]:
        query = "Select room_number from bookings where name = 'Shubham Garg'"
    elif room_occupant == l[3]:
        query = "Select room_number from bookings where name = 'Amir Khan'"
    mycursor.execute(query)
    for room_number in mycursor:
        test_tuple = room_number
        res = int(''.join(map(str, test_tuple)))
        print("{} is staying in the room {}".format(room_occupant, res))
    mydb.commit()

def find_dates():
    l = ["Rahul Jain", "Nitye Gupta", "Shubham Garg", "Amir Khan"]
    room_occupant = str(input("Enter name of room occupant:"))
    if room_occupant == l[0]:
        query = "Select checkin,checkout from bookings where name = 'Rahul Jain'"
    elif room_occupant == l[1]:
        query = "Select checkin,checkout from bookings where name = 'Nitye Gupta'"
    elif room_occupant == l[2]:
        query = "Select checkin,checkout from bookings where name = 'Shubham Garg'"
    elif room_occupant == l[3]:
        query = "Select checkin,checkout from bookings where name = 'Amir Khan'"
    mycursor.execute(query)
    for checkin,checkout in mycursor:
        test_tuple = checkin
        print("{} checked in on {}".format(room_occupant, test_tuple))
        test_tuple2 = checkout
        print("{} checked out on {}".format(room_occupant, test_tuple2))
    mydb.commit()

def bill():
    l = ["Rahul Jain", "Nitye Gupta", "Shubham Garg", "Amir Khan"]
    room_occupant = str(input("Enter name of room occupant:"))
    if room_occupant == l[0]:
        query = "Select amount,phone,pretotal from bookings where name = 'Rahul Jain'"
    elif room_occupant == l[1]:
        query = "Select amount,phone,pretotal from bookings where name = 'Nitye Gupta'"
    elif room_occupant == l[2]:
        query = "Select amount,phone,pretotal from bookings where name = 'Shubham Garg'"
    elif room_occupant == l[3]:
        query = "Select amount,phone,pretotal from bookings where name = 'Amir Khan'"
    mycursor.execute(query)
    for amount,phone,pretotal in mycursor:
        print("================================")
        print("     Heavens Delight, Delhi     ")
        print("================================")
        print("                                ")
        print("Guest Name: {}".format(room_occupant))
        print("Phone Number: {}".format(phone))
        print("                                ")
        print("Price per Day: Rs. 5000")
        tax = 20/100
        print("Number of Days: {}".format(pretotal/5000))
        print("Pretotal: {}".format(pretotal))
        print("Tax: 20%")
        print("Final Amount: {}".format(amount))
        print("================================")
        print("                                ")

    mydb.commit()


print("If you want to add a booking, press 1")
print("If you want to check the room number of a guest, press 2")
print("If you want to see check-in and check-out dates of guests, press 3")
print("If you want to get the bill of a guest, press 4")
operation = int(input(""))
if operation == 1:
    add_booking()
elif operation == 2:
    find_room()
elif operation == 3:
    find_dates()
elif operation == 4:
    bill()
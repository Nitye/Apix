import datefinder
import datetime
import os

date = str(datetime.date.today())
hour = datetime.datetime.now().hour
min = datetime.datetime.now().minute

text = str("alarm for 1:15")

if "alarm" and "tomorrow" in text:
    date_timeB = datefinder.find_dates(text)
    for mat in date_timeB:
        stringB = str(mat)
        dateB = str(datetime.date.today() + datetime.timedelta(days=1))
        timeB = stringB[11:]
        hourB= int(timeB[:-6])
        minB = int(timeB[3:-3])
        print(mat)
        print(dateB)
        print(hourB)
        print(minB)
        while True:
            if dateB == date:
                if hourB == hour:
                    if minB == min:
                        print("Alarm is off")
                        os.startfile("C:\\Apix Media\\alarm music.mp3")
                        break

elif "alarm" in text:
    date_timeA = datefinder.find_dates(text)
    for mat in date_timeA:
        stringA = str(mat)
        dateA = str(stringA[:-9])
        timeA = stringA[11:]
        hourA = int(timeA[:-6])
        minA = int(timeA[3:-3])
        print(mat)
        print(dateA)
        print(hourA)
        print(minA)
        while True:
            if dateA == date:
                if hourA == hour:
                    if minA == min:
                        print("Alarm is off")
                        os.startfile("C:\\Apix Media\\alarm music.mp3")
                        break
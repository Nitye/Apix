import datetime
import time
import os

n = 1
c, b, a = input("Enter the date = ").split('/')
hr, min, sec = input("Enter the time = ").split(':')
schedule_date = datetime.date(int(a), int(b), int(c))
while n>0:
    if time.localtime().tm_hour == int(hr) and int(min) and int(sec) and datetime.date.today() == schedule_date:
        os.startfile('C:\\songs\\Wolves(Lyrics).mp3')
        break
    else:
        n+=1
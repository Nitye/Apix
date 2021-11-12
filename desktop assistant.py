import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random
import smtplib
import operator
import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui
import requests
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import datefinder
from functools import reduce

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

hour = int(datetime.datetime.now().hour)
min = int(datetime.datetime.now().minute)
date = str(datetime.date.today())

def wishMe():
    if hour>=4 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")

    else:
        speak("Good Evening!")
        print("Good Evening!")
    print("I am apix. How may I help you.")
    speak("I am apix. How may I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please.")
        return "None"
    return query

def stopMusic():
    try:
        os.system('TASKKILL /F /IM GrooveMusic.exe')
    except Exception as e:
        print(str(e))

def sendEmail(to, content):
    e  = open("C:\\Apix Media\\Apix email.txt", "r")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    email = e.readline()
    password = e.readline()
    server.login(email, password)
    server.sendmail(email, to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        numbers = [int(word) for word in query.split() if word.isdigit()]

        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("According to Wikipedia " + results)
            speak("According to Wikipedia")
            speak (results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'music' in query:
            music_dir = 'C:\\songs'
            songs = os.listdir(music_dir)
            number = random.randint(0, 200)
            os.startfile(os.path.join(music_dir, songs[number]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is " + strTime)
            print("The time is " + strTime)

        elif 'email' in query:
            try:
                speak("What should I say?")
                print("What should I say?")
                content = takeCommand()
                to = "sayeshagupta26@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
                print("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry I am unable to send this email")
                print("Sorry I am unable to send this email")

        elif 'camera' in query:
            os.chdir("C://Apix Media")
            cap = cv2.VideoCapture(0)
            cv2.namedWindow("Apix Camera")
            img_counter = 0
            x = 1
            print("Say cheese to click picture and thanks to close camera")
            speak("Say cheese to click picture and thanks to close camera")
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Failed to open camera")
                    speak("Failed to open camera")
                    break
                cv2.imshow("Apix Camera", frame)
                k = cv2.waitKey(1)
                order = takeCommand()
                if order == 'cheese':
                    img_name = "Apix image" + str(x) + ".png".format(img_counter)
                    x += 1
                    cv2.imwrite(img_name, frame)
                    print('Picture taken and saved in Apix Media')
                    speak('Picture taken and saved in Apix Media')
                    img_counter+=1
                elif order == 'thanks':
                    print('Closing camera')
                    speak('Closing camera')
                    break
            cap.release()

        elif 'record' and 'video' in query:
            os.chdir("C://Apix Media")
            y = 1
            cap = cv2.VideoCapture(0)
            fourcc = cv2.VideoWriter_fourcc(*'MJPG')
            rec = cv2.VideoWriter('Apix Video' + str(y) + '.avi', fourcc, 24.0, (640, 480))
            y += 1
            print("Recording Video, Press Q to stop recording")
            speak("Recording Video, Press Q to stop recording")
            while True:
                ret, frame = cap.read()
                cv2.imshow("God's beautiful creation", frame)
                key = cv2.waitKey(1) & 0xff
                rec.write(frame)
                if key == ord('q'):
                    print("Recording stopped. Recording saved in Apix Media")
                    speak("Recording stopped. Recording saved in Apix Media")
                    break
            cap.release()
            rec.release()

        elif 'record my screen' in query:
            os.chdir("C://Apix Media")
            z = 1
            print("Screen recording started, Say done to stop recording")
            speak("Screen recording started, say done to stop recording")
            fourcc = cv2.VideoWriter_fourcc(*'MJPG')
            out = cv2.VideoWriter("Apix video" + str(z) + ".avi", fourcc, 10.0, (1366, 768))
            z += 1
            while True:
                img = ImageGrab.grab()
                img_np = np.array(img)
                frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
                out.write(frame)
                wait = cv2.waitKey(1)
                screen_record_order = takeCommand()
                if screen_record_order == "done":
                    print("Stopped screen recording. Recording saved in Apix Media")
                    speak("Stopped screen recording. Recording saved in Apix Media")
                    break
            out.release()

        elif 'take' and 'screenshot' in query:
            os.chdir("C://Apix Media")
            print("Say take screenshot or press Esc to take screenshot")
            speak("Say take screenshot or press Escape to take screenshot")
            w = 1
            screenshot = pyautogui.screenshot()
            ss_command = takeCommand()
            if ss_command == 'take screenshot':
                screenshot.save('Apix Screenshots' + str(w) + '.png')
                w += 1
                print("Screenshot taken and saved in Apix Media")
                speak("Screenshot taken and saved in Apix Media")

            elif cv2.waitKey(1) == 27:
                screenshot.save('Apix Screenshots' + str(w) + '.png')
                w += 1
                print("Screenshot taken and saved in Apix Media")
                speak("Screenshot taken and saved in Apix Media")

        elif 'roll' and 'dice' in query:
            dice = random.randint(1, 6)
            print("Your number is " + str(dice))
            speak("Your number is " + str(dice))

        elif 'sum' or 'add' in query:
            print(numbers)
            sum1 = reduce((lambda x, y: x+y), [numbers])
            print("The sum is " + str(sum1))
            speak("The sum is " + str(sum1))

        elif 'difference' or 'subtract' in query:
            numbers1 = [int(word) for word in query.split() if word.isdigit()]
            diff = reduce((lambda x, y: x-y), numbers1)
            abs_diff = abs(reduce((lambda x, y: x-y), numbers1))
            print("The difference is " + str(diff) + " and the absolute difference is " + str(abs_diff))
            speak("The difference is " + str(diff) + " and the absolute difference is " + str(abs_diff))

        elif 'product' or 'multiply' or 'into' in query:
            numbers2 = [int(word) for word in query.split() if word.isdigit()]
            product = reduce((lambda x, y: x*y), numbers2)
            print("The product is " + str(product))
            speak("The product is " + str(product))

        elif 'divide' or 'quotient' in query:
            numbers3 = [int(word) for word in query.split() if word.isdigit()]
            quotient = reduce((lambda x, y: x/y), numbers3)
            print("The result is " + str(quotient))
            speak("The result is " + str(quotient))

        elif 'weather' in query:
            f = open("C:\\Apix Media\\Apix Secrecies.txt", "r")
            user_api = f.readline()
            print("Which city's weather would you like to know about?")
            speak("Which city's weather would you like to know about?")
            location = takeCommand()
            complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api
            api_link = requests.get(complete_api_link)
            api_data = api_link.json()
            # print(api_data)
            if api_data['cod'] == '484':
                print("Invalid city: {}, Please check your city name".format(location))
            else:
                temp_city = ((api_data['main']['temp']) - 273.15)
                weather_desc = api_data['weather'][0]['description']
                hmdt = api_data['main']['humidity']
                wind_spd = api_data['wind']['speed']
                date_time = datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
                print(("Weather Stats for: "+location).format(location.upper(), date_time))
                print("Current temperature is: {:.2f} deg C".format(temp_city))
                print("Current weather desc  :", weather_desc)
                print("Current Humidity      :", hmdt, '%')
                print("Current wind speed    :", wind_spd, 'kmph')
                speak("Weather Stats for - {} || {}".format(location.upper(), date_time))
                speak("Current temperature is: {:.2f} degree Celsius".format(temp_city))
                speak("Current weather description is  :" + weather_desc)
                speak("Current Humidity is     :" + str(hmdt) + '%')
                speak("Current wind speed is   :" + str(wind_spd) + 'kilometres per hour')

        elif "alarm" and "tomorrow" in query:
            date_timeB = datefinder.find_dates(query)
            print("Setting alarm.....")
            speak("Setting alarm")
            for mat in date_timeB:
                stringB = str(mat)
                dateB = str(datetime.date.today() + datetime.timedelta(days=1))
                timeB = stringB[11:]
                hourB = int(timeB[:-6])
                minB = int(timeB[3:-3])
                while True:
                    if dateB == date:
                        if hourB == hour:
                            if minB == min:
                                print("Your alarm has gone off")
                                speak("Your alarm has gone off")
                                os.startfile("C:\\Apix Media\\alarm music.mp3")
                                break

                    else:
                        break

        elif "alarm" in query:
            date_timeA = datefinder.find_dates(query)
            print("Setting alarm.....")
            speak("Setting alarm")
            for mat in date_timeA:
                stringA = str(mat)
                dateA = str(stringA[:-9])
                timeA = stringA[11:]
                hourA = int(timeA[:-6])
                minA = int(timeA[3:-3])
                while True:
                    if dateA == date:
                        if hourA == hour:
                            if minA == min:
                                print("Your alarm has gone off")
                                speak("Your alarm has gone off")
                                os.startfile("C:\\Apix Media\\alarm music.mp3")
                                break

                    else:
                        break

        elif 'chat' in query:
            bot = ChatBot('Apix')
            bot.set_trainer(ListTrainer)
            langFile = os.listdir('C:/Users/dell/Desktop/Chat-Bot-main/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/')
            for file in langFile:
                data = open('C:/Users/dell/Desktop/Chat-Bot-main/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/' + file,'r', encoding='utf-8').readlines()
                bot.train(data)
            while True:
                ip = takeCommand()
                if ip != 'bye':
                    reply = str(bot.get_response(ip))
                    print("Apix: ", reply)
                    speak(reply)

                elif ip == 'bye':
                    print("I will miss you")
                    speak("I will miss you")
                    break

        elif 'stop' or 'abort' in query:
            stopMusic()

        elif 'bye' or 'quit' or 'see you later' in query:
            print("Hope I was of service to you. Bye")
            speak("Hope I was of service to you. Bye")
            exit()

        # Error: aage ka kuch ho nahi raha hai
        elif 'toss' or 'flip' in query:
            toss = ['Heads', 'Tails']
            toss_result = random.choice(toss)
            print("The result is " + toss_result)
            speak("The result is " + toss_result)

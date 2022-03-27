import pyttsx3
import speech_recognition as sr
import numpy as np
import cv2
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        audio = r.listen(source)

    try:
        print("Recognizing..")
        speak("Recognizing")
        query = r.recognize_google(audio, language='en-in')

    except Exception as e:
        print(e)
        print("Could you say that again please")
        speak("Could you say that again please")
        return "None"
    return query

if __name__ == '__main__':
    print("Hello, I am Edith, I can memorize people")
    speak("Hello, I am Edith, I can memorize people")

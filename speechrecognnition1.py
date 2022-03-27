import speech_recognition as sr
import webbrowser as wb
from win32com.client import Dispatch

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()
speak = Dispatch("Sapi.SpVoice")

with sr.Microphone() as source:
    print('Hey I am apix')
    speak.Speak('Hey I am apix')
    print('Speak now')
    speak.Speak('Speak now')
    audio = r3.listen(source)

if 'video' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print('Search your video')
        speak.Speak('Search your video')
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            print('Searching '+get)
            speak.Speak('Searching Youtube for '+get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('I am sorry there was an error. Try again later.')
            speak.Speak('I am sorry there was an error. Try again later.')
        except sr.RequestError as e:
            print('Sorry I can not do that'.format(e))


if 'search' in r1.recognize_google(audio):
    r1 = sr.Recognizer()
    url = 'https://en.wikipedia.org/wiki/'
    with sr.Microphone() as source:
        print('What do you want me to search?')
        speak.Speak('What do you want me to search?')
        audio = r1.listen(source)

        try:
            get = r1.recognize_google(audio)
            print('Searching '+get)
            speak.Speak('Searching '+get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('I am sorry I am unable to do that right now. Please try again later.')
            speak.Speak('I am sorry I am unable to do that right now. Please try again later.')
        except sr.RequestError as e:
            print('Sorry I can not do that'.format(e))

else:
    print('I am sorry I can not help you with that.')
    speak.Speak('I am sorry I can not help you with that.')
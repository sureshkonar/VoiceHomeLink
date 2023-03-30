import pyttsx3
import datetime
import speech_recognition as sr
import pyfirmata
import time
import datetime
from pymata4 import pymata4
import os
import serial
import webbrowser as wb
import wikipedia
import subprocess
import pyjokes


board=pyfirmata.Arduino('COM5')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
voicespeed = 170
engine.setProperty('rate', voicespeed)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)


def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day

    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def open_chrome():
    speak('opening chrome')
    url = "https://www.google.co.in/"
    chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
    wb.get(chrome_path).open(url)

def open_portfolio():
    speak('opening portfolio')
    url = "https://sureshkonar.github.io/suresh-portfolio-heroku/"
    chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
    wb.get(chrome_path).open(url)

def wishme():
    speak("welcome back sir")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good morning")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon")
    elif hour >= 18 and hour <= 21:
        speak("Good evening")
    else:
        speak("Good night")

    speak("Jarvis at your service . Please tell me how can i help u?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        # r.pause_threshold = 1
        audio=r.listen(source,timeout=2)
        # audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio)
    except Exception as e:
        print(e)
        print("---Say that Again---")

        return "None"
    return query




if __name__ == "__main__":
    board.digital[3].write(0)
    board.digital[8].write(0)
    board.digital[6].write(0)
    board.digital[5].write(0) 
    board.digital[4].write(0)
    board.digital[9].write(0)
    board.digital[13].write(1)
    wishme()

    while True:
        query = takeCommand().lower()  
        print(query)

        if "time" in query:  
            time()           
        elif "date" in query:  
            date()  

        elif'portfolio' in query:
            open_portfolio()

        elif 'chrome' in query:
            open_chrome()

        elif "search" in query:
            speak("what should i search?")
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"  
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")  
        
        elif "open notepad" in query:
            speak("opening notepad")
            location = "C:/WINDOWS/system32/notepad.exe"
            notepad = subprocess.Popen(location)

        elif "close notepad" in query:
                speak("closing notepad")
                notepad.terminate()

        elif "joke" in query:
                speak(pyjokes.get_jokes())

        elif 'turn on blue light' in query:
            speak('Turning on the Light....')
            #time.sleep(0.1)
            board.digital[3].write(1)

        elif 'turn off blue light' in query:
            speak('Truning of the light....')
            # time.sleep(0.1)
            board.digital[3].write(0)

        elif 'turn on red light' in query:
            speak('Turning on the Light....')
            #time.sleep(0.1)
            board.digital[4].write(1)

        elif 'turn off red light' in query:
            speak('Truning of the light....')
            # time.sleep(0.1)
            board.digital[4].write(0)

        elif 'turn on green light' in query:
            speak('Turning on the Light....')
            #time.sleep(1)
            board.digital[5].write(1)

        elif 'turn off green light' in query:
            speak('Turning of the light....')
            # time.sleep(0.1)
            board.digital[5].write(0) 

        elif 'turn on fan' in query:
            speak('Turning on the fan....')
            #time.sleep(0.1)
            board.digital[6].write(1)

        elif 'turn off fan' in query:
            speak('Turning of the fan....')
            # time.sleep(0.1)
            board.digital[6].write(0)

        # elif 'security' in query:
        #     speak('Entering Security Mode')
        #     suresh=board.analog[1].read()
        #     # pratish=float(suresh)
        #     # print(pratish)
        #     print(suresh)
        #     # speak(pratish)
        #     if suresh==1:
        #         speak('threat Detected')
        #         break
        #     else:
        #         speak('all good outside no threat detected')
        #         break

        elif 'turn on alarm' in  query:
            board.digital[13].write(0)
            speak('alarm is turned on....')

        elif 'turn off alarm' in  query:
            board.digital[13].write(1)
            speak('alarm is turned off....')

        elif 'on arcade' in query:
            speak('entering arcade mode')
            board.digital[8].write(1)
            speak('laser turned on')  

        elif 'exit arcade' in query:
            speak('exiting arcade mode')
            board.digital[8].write(0)
            speak('laser turned off') 
        
        elif 'ir' in query:
            speak('turneing on ir')
            ir=board.digital[9].read()
            print(ir)
        
        elif 'offline' in query:
            speak('Going Offline....')
            board.digital[3].write(0)
            board.digital[8].write(0)
            board.digital[6].write(0)
            board.digital[5].write(0) 
            board.digital[4].write(0)
            board.digital[9].write(0)
            board.digital[13].write(1)
            quit()
            


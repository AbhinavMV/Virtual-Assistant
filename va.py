import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
import random
import wolframalpha
from googlesearch import search

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
gcPath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
vsPath = "\"C:\\Users\\Administrator\\Desktop\\Microsoft VS Code\\Code.exe\""
musicPath = "E:\\SONGS\\"
fp = open("C:\\Users\\Administrator\\Desktop\\Codes\\test.txt","r")
clientId = fp.read()
client = wolframalpha.Client(clientId)

webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(gcPath))

def wishMe():
    time = datetime.datetime.now().hour
    if time>=0 and time<12:
        speak("Good Morning")
    elif time>=12 and time<18:
        speak("Good Afternoon")
    else:
        speak("Good Night")
    speak("Sir, How can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    except:
        print("Say that again..")
    return query

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    wishMe()
    while True:  
        try:
            query = takeCommand().lower()
            if "wikipedia" in query:
                query = query.replace("wikipedia","")
                speak(f"The first two lines of {query}are ")
                print(wikipedia.summary(query , sentences=2))

            elif "hello" in query:
                speak("Hello sir")
                
            elif "bye" in query:
                speak("Goodbye Sir")
                exit(1)
            elif "play music" in query:
                songPath = random.choice(os.listdir(musicPath))
                filePath = "\""+musicPath+songPath+"\""
                os.system(filePath)
            elif "open youtube" in query:
                webbrowser.get("chrome").open("youtube.com")
            elif "open google" in query:
                webbrowser.get("chrome").open("google.com")
            elif "open code" in query:
                os.system(vsPath)
            elif "open chegg" in query:
                webbrowser.get("chrome").open("expert.chegg.com")
            else:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    print(results)
                except:
                    speak("Sorry nothing available.\nRecommended sites by google")
                    for i in search(query,tld="co.in",lang="en",num=5,stop=5,pause=2):
                        print(i)
        except:
            speak("Could not understand.")
            query = input("Type your query")      


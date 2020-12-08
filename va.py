import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

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
        print("None")
    return query

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    wishMe()  
    query = "Shahrukh khan wikipedia"
    if "wikipedia" in query:
        query = query.replace("wikipedia","")
        speak(f"The first two lines of {query}are ")
        print(wikipedia.summary(query , sentences=2))

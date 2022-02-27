import pyttsx3
import speech_recognition as sr
import datetime
import os
import subprocess, time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# speech to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"You said : {query}")

    except Exception as e:
        speak("Say that again please.")
        return "none"
    return query


# greet
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=4:
        speak("It's getting late sir")
    elif hour > 4 and hour < 6:
        speak("Early Morning sir Good for your health")
    elif hour >= 6 and hour <= 12:
        speak("Good Morning Sir.")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon Sir")
    elif hour >= 18 and hour <24:
        speak("Good Evening Sir")
    speak("How can I help you?")


if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()

        # logic building for task
        if "thanks" in query or "thank you" in query:
            speak("It's my duty sir")
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
        if "open cmd" in query or "open command prompt" in query:
            os.system("start cmd")
        if "open calculator" in query:
            npath = "C:\\Windows\\System32\\calc.exe"
            os.startfile(npath)
        if "open camera" in query:
            subprocess.run('start microsoft.windows.camera:',shell=True)
            time.sleep(10)
            subprocess.run('Taskkill /IM WindowsCamera.exe /F',shell=True)
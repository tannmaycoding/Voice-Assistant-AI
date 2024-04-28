"""
This Is An AI at a fundamental level.
An AI is a software which Helps in making work EASY.
You Can import all the functions for other Work.

Modules Used:
    smtplib,
    ssl,
    EmailMessage from email.message,
    sys,
    random,
    os,
    pyttsx3,
    datetime,
    speech_recognition as sr,
    webbrowser,
    wikipedia,

Functions Made:
    speak: For AI to speak,
    takeCommand: For taking Speech Input,
    wishMe: For Wishing User In Start Of Program,
    sendEmail: To send Email
"""

# Importing Modules
import smtplib
import ssl
from email.message import EmailMessage

import sys
import random

import webbrowser
import wikipedia

import os

import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    """Speaks Audio Argument"""
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """Wishes User By Speaking In Start"""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am AI. Please tell me how may I help you")


def takeCommand():
    """Takes Speech Input"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}\n")

        except Exception as e:
            print(e)
            print('Say That Again Please')
            speak("Say That Again Please")
            return 'None'
        return query


def sendEmail(fr, password, to, sub, cont):
    """
    Sends Email from(fr) with password(password) -> to(to) with subject(sub) and with content(cont)
    :param fr: sender's address
    :param password: sender's password
    :param to: receiver's address
    :param sub: email's subject
    :param cont:  email's content
    """
    em = EmailMessage()
    em['From'] = fr
    em['To'] = to
    em['Subject'] = sub
    em.set_content(cont)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(fr, password)
        smtp.sendmail(fr, to, em.as_string())


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower().casefold()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'your-music-folder'
            songs = random.choice(os.listdir(music_dir))
            print(songs)
            os.startfile(os.path.join(music_dir, songs))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open python' in query:
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1.3\\bin\\pycharm64.exe"
            os.startfile(path)

        elif 'email' in query:
            try:
                email_sender = 'senders-email-address'
                sender_password = 'senders-password'
                email_receiver = 'recievers-email-addreaa'
                speak("Please tell the subject")
                subject = takeCommand()
                speak("What is the content?")
                content = takeCommand()
                sendEmail(email_sender, sender_password, email_receiver, subject, content)

            except Exception as e:
                print(e)

        elif 'quit' in query:
            sys.exit()

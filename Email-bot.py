import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
import time


listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        pass





def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('nitinjunior3@gmail.com','yqodzyybkicjhrny')
    email = EmailMessage()
    email['From'] = 'nitinjunior3@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
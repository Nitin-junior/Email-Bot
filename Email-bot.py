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




email_list = {
    'dude': 'COOL_DUDE_EMAIL',
    'nitin': 'nitinpriyadarshi70@gmail.com',
    'pink': 'jennie@blackpink.com',
    'lisa': 'lisa@blackpink.com',
    'irene': 'irene@redvelvet.com'
}


def get_email_info():
    name = time.sleep(2)
    talk('Tell me name of person you want to send email')
    name = get_info()

    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk(' Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()



get_email_info()

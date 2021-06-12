import speech_recognition as sr
import pyttsx3
import pywhatkit
from datetime import datetime
import wikipedia
import pyjokes



listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'tom' in command:
                command = command.replace('tom', '')
    except Exception as e:
        print("ERROR : " + str(e))
    return command

def run_app():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date today' in command:
        thedate = datetime.today().strftime('%Y-%m-%d')
        print(thedate)
        talk('Today is ' + str(thedate))
    elif 'what is' in command:
        item = command.replace('what is', '')
        talk(item)
        pywhatkit.search(item)
    elif 'search' in command:
        item = command.replace('search', '')
        talk(item)
        pywhatkit.search(item)
    elif 'how to' in command:
        talk(command)
        pywhatkit.search(command)
    elif 'tell me a joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif command == 'who are you':
        print("Virtual Assistant")
        talk("I am your Virtual assistant")
    else:
        talk("Please say it again")


while True:
    run_app()



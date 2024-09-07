import speech_recognition as sr
import datetime
import webbrowser
import pyttsx3

# Initialize the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None

def tell_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is " + time)

def tell_date():
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    speak("Today's date is " + date)

def search_web(query):
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)

while True:
    command = take_command()
    if command is not None:
        if "hello" in command:
            speak("Hello! How can I assist you today?")
        elif "time" in command:
            tell_time()
        elif "date" in command:
            tell_date()
        elif "search" in command:
            query = command.replace("search", "")
            search_web(query)
        else:
            speak("I didn't understand that. Please try again!")
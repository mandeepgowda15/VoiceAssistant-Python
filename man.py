import pyttsx3
import webbrowser
import speech_recognition as sr


send=pyttsx3.init()
voices = send.getProperty('voices')
send.setProperty('rate', 150)
send.setProperty('voice', voices[1].id)

def openChrome():
    speak("Opening chrome")
    chromepath="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    command = takeCommand("What should i do in chrome?")
    if 'open chrome' in command:
        speak("opening chrome")
        webbrowser.get(chromepath).open_new_tab('https://www.google.com')
    else:
        speak("What should I search?")
        command = takeCommand("What should I search?")
        speak(command)
        webbrowser.get(chromepath).open_new_tab(command)

def speak(audio):
    send.say(audio)
    send.runAndWait()

def call():
    speak("hey Universe")


def takeCommand(cmd="Listening....."):
    r=sr.Recognizer()
    with sr.Microphone() as mic:
        print(cmd)
        r.pause_threshold = 1
        audio = r.listen(mic)

    try:
        print("Recognizing..........")
        text = r.recognize_google(audio)
        text = text.lower()
        return text

    except Exception as e:
        speak(e)
        print(e)

    return None

if __name__=="__main__":
    call()
    while True:
        text = takeCommand("I'm hearing..........")
        if 'open chrome' in text:
            openChrome()

        elif 'end the service' in text:
            speak("Good bye...............")
            quit()

    

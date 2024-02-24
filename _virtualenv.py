import speech_recognition as sr
from gtts import gTTS
import os
import webbrowser

def listen_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("mpg123 -q output.mp3")

def open_website(url):
    webbrowser.open(url)
    speak(f"Opening {url}.")

def process_command(command):
    if command is not None:
        if "hello" in command:
            speak("Hello USER! How can I help you?")
        elif "tell me your name" in command:
            speak("I am Jarvis and im ayaan's assistent.")
        elif "tell me a joke" in command:
            speak("meri ex ka pati chutia hai!")
        elif "tell me jarvis aaj kya hai" in command:
            speak("ajj faizul bhai ka birthday hai ")
        elif "to aaj kya karna chahie" in command:
            speak("party karo nanga nacho sub ki gand maar doo")
        elif "tell me the truth" in command:
            speak(" bhaiyaji Your ex is rand.")
        elif "are you sure" in command:
            speak("haa haa bhai, im definately sure.")
        elif "open youtube" in command:
            open_website("https://www.youtube.com")
        elif "open instagram" in command:
            open_website("https://www.instagram.com")
        elif "open google" in command:
            open_website("https://www.google.com")
        elif "open facebook" in command:
            open_website("https://www.facebook.com")
        elif "open spotify" in command:
            open_website("https://www.spotify.com")
        elif "open netflix" in command:
            open_website("https://www.netflix.com")
        elif "open amazon" in command:
            open_website("https://www.amazon.com")
        elif "open flipkart" in command:
            open_website("https://www.flipkart.com")
        elif "open amazon prime" in command:
            open_website("https://www.amazon.com/prime")
        elif "thank you" in command:
            speak("you're welcome")
        elif "exit" in command:
            speak("Exiting program.")
            exit()
        else:
            speak("Command not recognized. Try again.")

if __name__ == "__main__":
    while True:
        command = listen_command()
        process_command(command)

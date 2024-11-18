import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    '''convert text to speech'''
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Listen for a voice command."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

def respond_to_command(command):
    """Respond to the user's command."""
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}.")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}.")
    elif "search" in command:
        search_term = command.split("search")[-1].strip()
        url = f"https://www.google.com/search?q={search_term}"
        webbrowser.open(url)
        speak(f"Here are the search results for {search_term}.")
    else:
        speak("I can respond to commands like hello, time, date, and search.")

def main():
    """Main function to run the assistant."""
    speak("Hi, I am your voice assistant.")
    while True:
        command = listen()
        respond_to_command(command)

if __name__ == "__main__":
    main()


# to runnig this programme use following command in your terminal :- python assistant.py

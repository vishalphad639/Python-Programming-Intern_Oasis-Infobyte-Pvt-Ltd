import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests
import smtplib
from email.mime.text import MIMEText
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, WEATHER_API_KEY

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
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

def send_email(to, subject, body):
    """Send an email."""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to, msg.as_string())
        speak("Email sent successfully.")
    except Exception as e:
        speak("Failed to send email.")
        print(e)

def get_weather(city):
    """Fetch the weather information."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather_description = data['weather'][0]['description']
        temp = main['temp']
        speak(f"The weather in {city} is {weather_description} with a temperature of {temp} degrees Celsius.")
    else:
        speak("I couldn't fetch the weather data.")

def respond_to_command(command):
    """Respond to the user's command."""
    if "hello" in command:
        speak("Hello! How can I assist you today?")
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
    elif "send email" in command:
        # Example command: "send email to example@example.com with subject Test and body This is a test"
        try:
            _, to, *rest = command.split()
            subject_index = rest.index("subject") + 1
            body_index = rest.index("body") + 1
            subject = rest[subject_index]
            body = ' '.join(rest[body_index:])
            send_email(to, subject, body)
        except Exception as e:
            speak("There was an error sending the email.")
            print(e)
    elif "weather" in command:
        city = command.split("in")[-1].strip()
        get_weather(city)
    else:
        speak("I can help you with commands like hello, time, date, search, send email, and weather.")

def main():
    """Main function to run the assistant."""
    speak("Hi, I am your advanced voice assistant.")
    while True:
        command = listen()
        respond_to_command(command)

if __name__ == "__main__":
    main()


# to runnig this programme use following command in your terminal;- python assistant.py
import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import io
import geocoder

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        
        # Set up API key
        self.api_key = "106fe02eb7b0476a8b766e817fb11fc5"  # Replace with your OpenWeatherMap API key
        
        # Create input field for location
        self.location_entry = tk.Entry(root, width=30)
        self.location_entry.pack(pady=10)
        
        # Create button to get weather
        self.get_weather_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack(pady=10)
        
        # Unit selection
        self.unit_var = tk.StringVar(value="metric")
        tk.Radiobutton(root, text="Celsius", variable=self.unit_var, value="metric").pack()
        tk.Radiobutton(root, text="Fahrenheit", variable=self.unit_var, value="imperial").pack()
        
        # Create labels to display weather info
        self.weather_info = tk.Label(root, text="", font=("Arial", 16))
        self.weather_info.pack(pady=10)

        self.weather_icon = tk.Label(root)
        self.weather_icon.pack(pady=10)
        
    def get_weather(self):
        location = self.location_entry.get()
        if not location:
            messagebox.showwarning("Input Error", "Please enter a city name or ZIP code.")
            return
        
        weather_data = self.fetch_weather_data(location)
        if weather_data:
            self.display_weather(weather_data)
        else:
            messagebox.showerror("Data Error", "Could not retrieve weather data.")

    def fetch_weather_data(self, location):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.api_key}&units={self.unit_var.get()}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None

    def display_weather(self, data):
        city = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        
        self.weather_info.config(text=f"{city}: {temp}°{self.unit_var.get()[0].upper()}, Humidity: {humidity}%, Conditions: {weather_description.capitalize()}")
        
        # Load and display the weather icon
        icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"
        self.display_icon(icon_url)

        # Fetch and display forecast data
        lat, lon = self.get_location()
        forecast_data = self.fetch_forecast_data(lat, lon)
        if forecast_data:
            self.display_forecast(forecast_data)

    def display_forecast(self, data):
        daily_forecast = data['daily']
        forecast_text = "7-Day Forecast:\n"
        for day in daily_forecast[:7]:
            temp_day = day['temp']['day']
            weather_desc = day['weather'][0]['description']
            forecast_text += f"{temp_day}°{self.unit_var.get()[0].upper()} - {weather_desc.capitalize()}\n"
        messagebox.showinfo("Forecast", forecast_text)

    def get_location(self):
        g = geocoder.ip('me')
        return g.latlng  # Returns [latitude, longitude]

    def fetch_forecast_data(self, latitude, longitude):
        url = f"http://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&appid={self.api_key}&units={self.unit_var.get()}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None

    def display_icon(self, icon_url):
        try:
            response = requests.get(icon_url)
            image = Image.open(io.BytesIO(response.content))
            image = image.resize((100, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.weather_icon.config(image=photo)
            self.weather_icon.image = photo  # Keep a reference
        except Exception as e:
            print(f"Error loading icon: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
    
    # to running this program use this command in your terminal;- python weather_app_gui.py
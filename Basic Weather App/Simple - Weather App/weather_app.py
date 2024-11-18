import requests

def get_weather_data(location, api_key):
    # URL to fetch the weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4XX or 5XX)
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_weather(data):
    if data:
        city = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']

        print(f"Current weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {weather_description.capitalize()}")
    else:
        print("Could not retrieve weather data.")
def main():
    api_key = "106fe02eb7b0476a8b766e817fb11fc5"  # Replace with your OpenWeatherMap API key
    location = input("Enter a city name or ZIP code: ")

    weather_data = get_weather_data(location, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()

# to run this programme use this command in terminal;- python weather_app.py

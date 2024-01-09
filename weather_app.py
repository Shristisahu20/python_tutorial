# weather_app.py

import requests  # Import the 'requests' library for handling HTTP requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # You can change units to 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Oops, something went wrong:", err)

def display_weather(weather_data):
    if weather_data:
        print(f"Location: {weather_data['name']}, {weather_data['sys']['country']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    else:
        print("Weather data not available.")

if __name__ == "__main__":
    api_key = "95b7e6013fa287d06d5fdbf484fb1389"  # Replace with your actual API key
    location = input("Enter the city name or ZIP code: ")

    weather_data = get_weather(api_key, location)

    display_weather(weather_data)

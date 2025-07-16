import requests

# 🔑 Get your free API key from https://openweathermap.org/api
API_KEY = "YOUR_API_KEY_HERE"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Ask the user for a city
city = input("Enter city name: ")

# Build the request URL
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"  # Celsius
}

# Send the GET request
response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']
    weather = data['weather'][0]['description']
    print(f"✅ The temperature in {city} is {temperature}°C with {weather}.")
else:
    print("❌ City not found or API error.")

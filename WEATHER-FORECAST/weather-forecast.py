import requests

def get_weather(city):
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = 'edabce9ed80a29675aecf90d4df89f4d'
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    # Make the API request
    response = requests.get(base_url)
    data = response.json()
    
    # Extract relevant weather information from the API response
    if data['cod'] == 200:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        description = data['weather'][0]['description']
        
        # Display weather information
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description}")
    else:
        print("City not found. Please check the input.")

# Prompt the user for input
city_input = input("Enter the name of a city: ")
get_weather(city_input)

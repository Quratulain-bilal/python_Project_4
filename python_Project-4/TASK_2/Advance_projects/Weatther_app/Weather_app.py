import requests

# 1. Enter your city
city = input("Enter city name: ")

# 2. Get weather data
url = f"http://wttr.in/{city}?format=%t+%C"
weather = requests.get(url).text

# 3. Show result
print(f"Weather in {city}: {weather}")
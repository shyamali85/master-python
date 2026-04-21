import requests

city = input("Enter city name: ")

api_key = "YOUR_API_KEY_HERE" # ← replace with your key

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
   data = response.json()

   weather = data["weather"][0]["description"]
   temp_kelvin = data["main"]["temp"]
   temp_celsius = temp_kelvin - 273.15

   print(f"Weather: {weather}")
   print(f"Temperature: {temp_celsius:.2f} °C")
else:
   print("Error: City not found or API issue")
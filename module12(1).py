import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

if response.status_code == 200:
   data = response.json()
   print(data["value"]) # only print the joke text
else:
   print("Error fetching joke")
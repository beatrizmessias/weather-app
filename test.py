import requests
import datetime
import json

key = '7a41c9a9fa31295e2ab9dbacbd031a2d'
city = 'Brasília'
api_link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'

# Request
r = requests.get(api_link)

# Convert data
data = r.json()

print(data)









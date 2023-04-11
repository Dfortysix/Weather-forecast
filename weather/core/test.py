import requests

api_key = '10fbf22a02e8255aa2148a7853568814'
city = 'Hanoi'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print('City:', data['name'])
    print('Temperature:', data['main']['temp'])
    print('Humidity:', data['main']['humidity'])
    print('Wind speed:', data['wind']['speed'])
else:
    print('An error occurred:', response.text)
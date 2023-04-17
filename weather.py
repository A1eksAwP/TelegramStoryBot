from tokens import weather_token
import requests
from datetime import datetime


def get_weather(city='Saint Petersburg, RU', token=weather_token):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={token}&units=metric'
    try:
        r = requests.get(url)
    except Exception as e:
        print(e)
        return 'Такого города не найдено'
    if r.status_code != 200:
        return 'Такого города не найдено'
    data = r.json()
    time = datetime.fromtimestamp(data.get('dt')).strftime('%H:%M')
    city = data.get('name')
    wind = data.get('wind').get('speed')
    temp = data.get('main').get('temp')
    feel_like = data.get('main').get('feels_like')
    humidity = data.get('main').get('humidity')
    condition = data.get('weather')[0].get('description')
    coord_lon = data.get('coord').get('lon')
    coord_lat = data.get('coord').get('lat')
    sunrise = datetime.fromtimestamp(data.get('sys').get('sunrise')).strftime('%H:%M')
    sunset = datetime.fromtimestamp(data.get('sys').get('sunset')).strftime('%H:%M')
    return f"""
На момент {time} погода в {city}:
Состояние: "{condition}";
Температура: {temp}с;
Влажность: {humidity}%;
Ощущается как: {feel_like}с;
Ветер: {wind}м/с;
Восход: {sunrise};
Закат: {sunset};
Координаты: {coord_lon}/{coord_lat}.
В целом {'прохладно' if int(temp) < 10 else 'тепло'}.
"""

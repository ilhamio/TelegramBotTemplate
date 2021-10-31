from aiogram import types
from data.config import OPEN_WEATHER_TOKEN
import datetime, requests

from loader import dp


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={OPEN_WEATHER_TOKEN}&units=metric&lang=ru')
        data = r.json()

        time = message.date
        city = data['name']
        cur_weather = data['main']['temp']
        type_of_weather = str(data['weather'][0]['description']).capitalize()
        feel_like = round(data['main']['feels_like'])
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])

        await message.reply(f"***{time.strftime('%Y-%m-%d %H:%M')}***\n"
                            f'Погода в городе {city} на данный момент:\n'
                            f'Температура: {cur_weather} C° - {type_of_weather}\n'
                            f'Ощущается: {feel_like} C°\n'
                            f'Влажность: {humidity}%\n'
                            f'Давление: {pressure} мм.рт.ст\n'
                            f'Скорость ветра: {wind} м/c\n'
                            f'Время рассвета: {sunrise}\n'
                            f'Время заката: {sunset}')
    except:
        await message.reply('Проверьте название города')

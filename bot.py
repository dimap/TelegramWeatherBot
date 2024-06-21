import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Получаем API ключи из переменных окружения Docker. 
# API ключ https://www.visualcrossing.com
VISUAL_CROSSING_API_KEY = os.getenv('VISUAL_CROSSING_API_KEY')
# API ключ Telegram бота. Можно получить через https://t.me/Botfather
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Функция получения погоды по API
def get_weather(city: str) -> str:
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=metric&key={VISUAL_CROSSING_API_KEY}&contentType=json"
    response = requests.get(url)
    # Сохраняем ответ в виде JSON
    data = response.json()

    # При получении ошибки в ответе
    if 'errorCode' in data:
        return "Не удалось получить данные о погоде. Проверьте правильность названия города."

    # Выдёргиваем текущее состояние из всего ответа в отдельную переменную
    current_conditions = data['currentConditions']
    # Парсим JSON в читаемый текст 
    weather_report = (
        f"Погода в городе {city}:\n"
        f"Температура: {current_conditions['temp']}°C\n"
        f"Ощущается как: {current_conditions['feelslike']}°C\n"
        f"Описание: {current_conditions['conditions']}\n"
        f"Влажность: {current_conditions['humidity']}%\n"
        f"Скорость ветра: {current_conditions['windspeed']} км/ч"
    )
    return weather_report

# Обработчик команды /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Привет! Я бот для получения погоды. Напиши /weather <название города>, чтобы узнать погоду.')

# Обработчик команды /weather
async def weather(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 0:
        await update.message.reply_text('Пожалуйста, укажите название города.')
        return

    city = ' '.join(context.args)
    weather_report = get_weather(city)
    await update.message.reply_text(weather_report)

def main() -> None:
    # Создание объекта Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Добавление обработчиков команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("weather", weather))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
# Telegram-Weather-Bot
Простой Telegram бот написанный на Python, запускаемый из Docker контейнера, предназначенный для получения текущей погоды любого города. Для получения погоды используется API [Visual Crossing](https://www.visualcrossing.com) <br>
Данная программа написана для обучения и не предназначена для постоянного использования. Часть кода написана с помощью ИИ. <br>
Используются библиотеки python-telegram-bot и requests

# Установка и запуск контейнера
Для использования необходим установленный Docker
1) Переходим в папку, куда хотим копировать проект <br>
   ```
   cd /путь/к/проекту
   ```
3) Если есть установленный git, то можно скопировать репозиторий используя команду <br>
   ```
   git clone https://github.com/dimap/TelegramWeatherBot.git
   cd TelegramWeatherBot
   ```
   Либо сделать это вручную
4) **Если установлен docker-compose**, то в файле *docker-compose.yml* необходимо прописать собственные API ключи вместо *your_telegram_bot_token* и *your_visual_crossing_api_key*. <br>
   После этого для установки и запуска контейнера можно использовать <br>
   ```
   sudo docker-compose up --build -d
   ```
   **Если docker-compose не установлен**, то для сборки образа сначала надо использовать команду <br>
   ```
   sudo docker build -t telegram-bot .
   ```
   После этого для запуска контейнера используется команда
   ```
   sudo docker run -d --name telegram-weather-bot \
       -e TELEGRAM_BOT_TOKEN=your_telegram_bot_token \
       -e VISUAL_CROSSING_API_KEY=your_visual_crossing_api_key \
       telegram-weather-bot
   ```
   Где *your_telegram_bot_token* и *your_visual_crossing_api_key* это собственные API ключи сервисов

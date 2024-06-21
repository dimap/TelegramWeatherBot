# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install python-telegram-bot requests

# Копируем файл скрипта в контейнер
COPY bot.py /app/bot.py

# Устанавливаем рабочую директорию
WORKDIR /app

# Запускаем скрипт при запуске контейнера
CMD ["python", "bot.py"]
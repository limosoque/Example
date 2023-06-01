FROM ubuntu:latest
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код вашего приложения внутрь контейнера
COPY app.py
COPY binary_search.py

RUN python test_binary_search.py

pyinstaller --name=binary_search_app --onefile App.py -p binary_search.py

# Определяем команду, которая будет выполняться при запуске контейнера
CMD [ "python", "/dist/binary_search_app" ]

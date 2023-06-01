FROM ubuntu:latest
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код вашего приложения внутрь контейнера
COPY app.py .
COPY binary_search.py .

RUN pyinstaller --name=binary_search_app --onefile app.py


# Определяем команду, которая будет выполняться при запуске контейнера
CMD [ "./binary_search_app" ]

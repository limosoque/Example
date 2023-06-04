FROM ubuntu:latest AS build
FROM python:latest

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt && rm -rf /root/.cache/pip

# Копируем исходный код вашего приложения внутрь контейнера
COPY app.py .
COPY binary_search.py .

RUN pyinstaller --name=binary_search_app --onefile app.py -p binary_search.py
RUN ls /app/dist
# RUN pip uninstall -y -r requirements.txt



# Определяем команду, которая будет выполняться при запуске контейнера
CMD [ "/app/binary_search_app" ]

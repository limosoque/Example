FROM python:latest
WORKDIR app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
#&& rm -rf /root/.cache/pip

COPY app.py app.py
COPY binary_search.py binary_search.py

RUN pyinstaller --name=binary_search_app --onefile app.py -p binary_search.py
# RUN pip uninstall -y -r requirements.txt

FROM ubuntu:latest
WORKDIR app
COPY --from=build /app/dist/binary_search_app /app

# Определяем команду, которая будет выполняться при запуске контейнера
CMD [ "/app/binary_search_app" ]

FROM python:latest as build
WORKDIR app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py app.py
COPY binary_search.py binary_search.py

RUN pyinstaller --name=binary_search_app --onefile app.py -p binary_search.py


FROM ubuntu:latest
WORKDIR app
COPY --from=build /app/dist/binary_search_app /app

CMD [ "/app/binary_search_app" ]

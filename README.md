# Создание пайплайна сборки и выгрузки артефактов с использованием GitHub Actions и Docker

В ходе выполнения лабораторной работы реализованы:
* Приложение на языке python, выполняющее бинарный поиск числа в заданном массиве;
* Тестирование кода;
* Система сборки приложения под linux и windows;
* Отправка собранного под разные системы приложения в telegram;
* Выгрузка готового Docker-контейнера после успешной сборки в пайплайн и загрузка контейнера в Docker Hub;
* Cтатический анализ и автоматическое форматирование кода;
* Сборка на собственном подключенном агенте (собственный ПК).

## Бинарный поиск

В файле **binary_search.py** находится реализация бинарного поиска нерекурсивным методом, а в **app.py** - программа взаимодействия с пользователем.

## Тестирование

Работа функции **binary_search** тестируется при помощи pytest.

## Сборка приложения под linux и windows, отправка в telegram

В job **linux_build** выполняется сборка приложения при помощи pyinstaller, выгрузка артефакта собранного приложения на github и отправка приложения в telegram.
Под windows тот же самый процесс разбит на 2 job, потому что pyinstaller собирает приложение только под систему, на которой его запускают, а **appleboy/telegram-action** работает только на linux. **windows_build** собирает приложение и загружает его на github, после чего **send_windows_build** загружает артефакт и отправляет его в telegram. 

~~~YAML
- name: Send Telegram message
          uses: appleboy/telegram-action@master
          with:
            to: ${{ secrets.TELEGRAM_TO }}
            token: ${{ secrets.TELEGRAM_TOKEN }}
            message: Workflow triggered by ${{ github.event_name }} event
            document: windows_build.exe
~~~

## Создание docker image

В job **docker_build** из dockerfile собирается image и доставляется ко мне на docker hub. В dockerfile pyinstaller собирает исполняемый файл на одной системе, который затем выполняется на другой системе, что в 10 раз уменьшает размера image.

## Запуск docker image на локальном ПК

В job self-hosted созданный ранее image скачивается и запускается на локальной машине.

~~~YAML
- name: Run docker image
        run: |
          docker pull ${{ secrets.DOCKERHUB_USERNAME }}/binary_search_app:latest
          docker run ${{ secrets.DOCKERHUB_USERNAME }}/binary_search_app:latest
~~~

## Cтатический анализ и автоматическое форматирование кода
Job codacy_check запускает **codacy/codacy-analysis-cli-action**, который анализирует код и выводит рекомендации. 
Job auto_formatter устанавливает **black**, который форматирует код и, если workflow вызван push, создает commit в репозиторий с исправленным кодом.

~~~YAML
 - name: Commit and push changes
        if: github.event_name == 'push'
        run: |
          git config --global user.email "actions@github.com"
          git config --global user.name "GitHub Actions"
          status=$(git status)
          if [[ $status != "nothing to commit" ]]; then
            git commit -am "Auto-format Python code"
            git push
          fi
~~~

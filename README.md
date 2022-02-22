# Бот, который пингует сервера в ДНР и ЛНР

Для отправки icmp запросов в linux библиотеке aioping требуются root права.

## Установка:

1. Склонировать репозиторий, установить окружение и требуемые библиотеки
    ```shell
    git clone https://github.com/Egorrko/dlnr_status.git
    cd dlnr_status
    python -m venv env
    source env/bin/activate  # linux
    env/Scripts/activate.bat  # windows
    pip install -r requirements.txt
    ```
2. Заполнить `settings.json`
    ```json
    "BOT_TOKEN": "get_me_from_@BotFather", 
    "CHANNEL_USERNAME": "@example",
    ```
3. Запустить.
    ```shell
    python app/main.py
    ```

# Бот, который пингует сервера в ДНР и ЛНР

Для отправки icmp запросов в linux библиотеке aioping требуются root права.

## Установка:

1. Установить окружение и требуемые библиотеки
    ```shell
    python -m venv env
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
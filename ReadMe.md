# Telegram Bot for Remote PC Monitoring

This project is a Telegram bot for remote monitoring and basic management of a personal PC. It was created as a learning and showcase project to practice Python, the Telegram Bot API, aiogram, and system monitoring.

The bot is intended only for the owner and ignores commands from all other users. It can check whether it is running correctly, show system status, display CPU and RAM usage, and check network availability. Access is restricted through `OWNER_ID`, so only the owner can interact with it.

## Technologies Used

* Python 3
* aiogram 3
* psutil
* python-dotenv

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
TOKEN=your_telegram_bot_token
OWNER_ID=your_telegram_id
```

Run the bot:

```bash
python bot.py
```

## Project Structure

```text
project/
│
├── bot.py
├── requirements.txt
├── .env
└── README.md
```

## Security

* The bot token is stored in `.env`
* `.env` should never be uploaded to GitHub
* The bot only accepts commands from the owner

## Disclaimer

This software is provided for educational and personal use only. I am not responsible for any misuse, damage, data loss, or unauthorized access caused by the use of this bot.

---

# Telegram Bot для удалённого мониторинга ПК

Этот проект представляет собой Telegram-бота для удалённого мониторинга и базового управления личным ПК. Он был создан как учебный и демонстрационный проект для практики Python, Telegram Bot API, aiogram и системного мониторинга.

Бот предназначен только для владельца и игнорирует команды от других пользователей. Он умеет проверять, что запущен и работает, показывать статус системы, отображать загрузку CPU и RAM, а также проверять доступность сети. Доступ ограничен через `OWNER_ID`, поэтому управлять ботом может только владелец.

## Используемые технологии

* Python 3
* aiogram 3
* psutil
* python-dotenv

## Установка

Клонируйте репозиторий:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

Создайте файл `.env` в корне проекта:

```env
TOKEN=your_telegram_bot_token
OWNER_ID=your_telegram_id
```

Запуск бота:

```bash
python bot.py
```

## Структура проекта

```text
project/
│
├── bot.py
├── requirements.txt
├── .env
└── README.md
```

## Безопасность

* Токен бота хранится в `.env`
* `.env` нельзя загружать на GitHub
* Бот принимает команды только от владельца

## Отказ от ответственности

Данное программное обеспечение предоставляется только в образовательных и личных целях. Я не несу ответственности за любое неправомерное использование, ущерб, потерю данных или несанкционированный доступ, возникшие в результате использования этого бота.

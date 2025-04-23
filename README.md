# Bia_Notifier Telegram Bot

![aiogram](https://img.shields.io/badge/python-v3.10-blue.svg?logo=python&logoColor=yellow) ![aiogram](https://img.shields.io/badge/aiogram-v3-blue.svg?logo=telegram) ![License](https://img.shields.io/badge/license-MIT-blue.svg)

A service for notifying employees about changes in the calendar. Every time any changes happens on the Exchange's calendar, all the invited employers will be notified with an `.ics` files containing new event parameters

## Features

The bot provides the following features:

- Employers notification about closest events
- Sending an `.ics` file with updated event parameters *(for example: new time, new place)*
- Fully controllable notification settings

## Commands

The bot has several commands that can be used to access its features:

- `/start`: Sends an greeting and adds user to a system
- `/help`: Sends an help message, so user can learn about bot's commands
- `/settings`: Allows user to modify default notification settings
- `/get`: Sends user an `.isc` file with all the future meetings that are up-to-date

## Requirements

- Python v3.13.0
- aiogram v3.20.0
- SQLAlchemy v2.0.40
- ics v0.7.2
*(you can see all the requirements in `requirements.txt` file)*

## Installation

To get started with this bot, follow these steps:

- Clone this repository to your local machine.

    ```
    $ git clone https://github.com/clowixdev/samus_bot.git
    ```

- Create a virtual environment, activate it and install required dependencies.

    ```
    $ pyenv exec python -m venv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt
    ```

- Create a new bot on Telegram by talking to the BotFather, and [obtain the API token](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token).

- Add all the environmental data to the `.env` file

- Run the bot using `python bot.py`.
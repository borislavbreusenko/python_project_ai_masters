# Telegram bot for movie recomendation

Watch the movie of your choice if you have an option. 
Use this bot when in doubt.

## Getting Started

These are instructions to run the bot on your machine.

### Installing

Use python 3.10.6.
To install all libraries run this command:

```pip install -r requirements.txt```

## Deployment

Let's make this alive. 

### Getting API keys
1. You need telegram bot API key to run your bot. You can use this instruction:
2. You need unofficial kinopoisk API key to make requests. You can use this instruction:

### Flask server

First step is to run Flask server:

```waitress-serve --port=5000 film_searcher_server:app```

### Telegram bot

Run telegram bot:
```python src/bot.py```

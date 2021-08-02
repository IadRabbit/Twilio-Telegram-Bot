# Twilio-Telegram-Bot

![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)

A simple telegram bot for sending SMS through TWILIO API

## Installation

Installing dependencies

``` bash
pip3 install -r req.txt
```

## Config bot

First before you start the bot you need to fill proprely the variables inside the [settings.py](https://github.com/IadRabbit/Twilio-Telegram-Bot/blob/main/settings.py)

```python
__bot_token = "" # YOUR TELEGRAM BOT TOKEN TALK TO @BotFather
__twilio_account_sid = "" # YOUR TWILIO ACCOUNT SID CAN BE FOUND HERE https://console.twilio.com/?frameUrl=/console
__twilio_auth_token = "" # YOUR TWILIO AUTH TOKEN CAN BE FOUND HERE https://console.twilio.com/?frameUrl=/console
twilio_messaging_service_sid = "" # YOUR TWILIO MESSAGING SERVICE SID CAN BE FOUND HERE  https://console.twilio.com/us1/develop/sms/services?frameUrl=/console/sms/services
```

## Start bot

And then just use it :)

``` bash
./twilio_bot.py
```

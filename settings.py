#!/usr/bin/python3

from telegram.ext import Updater
from twilio.rest import Client as __twilio_client

__bot_token = "" # YOUR TELEGRAM BOT TOKEN TALK TO @BotFather
__twilio_account_sid = "" # YOUR TWILIO ACCOUNT SID CAN BE FOUND HERE https://console.twilio.com/?frameUrl=/console
__twilio_auth_token = "" # YOUR TWILIO AUTH TOKEN CAN BE FOUND HERE https://console.twilio.com/?frameUrl=/console
twilio_messaging_service_sid = "" # YOUR TWILIO MESSAGING SERVICE SID CAN BE FOUND HERE  https://console.twilio.com/us1/develop/sms/services?frameUrl=/console/sms/services

twilio_client = __twilio_client(__twilio_account_sid, __twilio_auth_token)
tg_bot_api = Updater(token = __bot_token)

root_ids = {} # CHAT ID SET FOR FORBID UNAUTHORIZED USERS TO SEND SMS
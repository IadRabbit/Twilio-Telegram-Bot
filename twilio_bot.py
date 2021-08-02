#!/usr/bin/python3

from time import sleep
from telegram import Update

from telegram.ext import (
	Filters, CommandHandler, MessageHandler
)

from settings import (
	twilio_client, tg_bot_api,
	root_ids, twilio_messaging_service_sid
)

bot = tg_bot_api.bot
users_data = {}

def send_msg(chat_id):
	c_user_data = users_data[chat_id]
	number = c_user_data['number']
	msg = c_user_data['msg']

	twilio_client.messages.create(
		number,
		messaging_service_sid = twilio_messaging_service_sid,
		body = msg
	)

	bot.send_message(
		chat_id = chat_id,
		text = f"Message sent to {number} :)"
	)

def check_user(chat_id):
	if chat_id in users_data:
		return

	users_data[chat_id] = {}

def start_command(update: Update, context):
	msg = update.message
	chat_id = msg.from_user.id

	bot.send_message(
		chat_id = chat_id,
		text = "Press /send_message",
	)

def send_message_command(update: Update, context):
	msg = update.message
	chat_id = msg.from_user.id
	check_user(chat_id)
	c_user_data = users_data[chat_id]

	bot.send_message(
		chat_id = chat_id,
		text = "Okay send me the number",
	)

	c_user_data['stage'] = "send_number"

def msgs_handler(update: Update, context):
	msg = update.message
	chat_id = msg.from_user.id
	check_user(chat_id)
	c_user_data = users_data[chat_id]

	if not c_user_data:
		bot.send_message(
			chat_id = chat_id,
			text = "Press /send_message first"
		)

		return

	c_stage = c_user_data['stage']
	msg = msg.text

	if c_stage == "send_number":
		c_user_data['number'] = msg
		c_user_data['stage'] = "send_msg"

		bot.send_message(
			chat_id = chat_id,
			text = "Okay, now send me the message to be sent"
		)
	elif c_stage == "send_msg":
		c_user_data['msg'] = msg
		send_msg(chat_id)

dispatcher = tg_bot_api.dispatcher

to_access = Filters.user(root_ids)

start_handler = CommandHandler(
	"start",
	start_command,
	filters = to_access, run_async = True
)

dispatcher.add_handler(start_handler)

send_message_handler = CommandHandler(
	"send_message",
	send_message_command,
	filters = to_access, run_async = True
)

dispatcher.add_handler(send_message_handler)

msgs = MessageHandler(
	(
		Filters.text &
		to_access
	), msgs_handler, run_async = True
)

dispatcher.add_handler(msgs)

tg_bot_api.start_polling()
print("BOT STARTED :)")

try:
	while True:
		sleep(4)
except KeyboardInterrupt:
	print("\nEXITTING :)")
	tg_bot_api.stop()
	exit()
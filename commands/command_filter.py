from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ParseMode
import os

source="https://github.com/Artis7eeR/forward-Tag-Remover-Bot"
START_TEXT="Hi [{}](tg://user?id={})\nI am A Forward Tag remover Bot.Send /help To Know What I Can Do"
HELP_TEXT="Forward A File,Video,Image,Post,etc I will Remove The File Source And Send Back You File if Any Bugs Found Report

@missioncrackjeeneet"

#Inline Keyboard Button
keyboard = [
[
 InlineKeyboardButton("My Father 🎅", url=https://t.me/tausifur_123)
]
]
reply_markup = InlineKeyboardMarkup(keyboard)

#Start Message
def start_text(u,c):
 u.message.reply_text(START_TEXT.format(u.message.from_user.full_name,u.message.chat.id),reply_markup=reply_markup,
parse_mode=ParseMode.MARKDOWN)

#Help Message
def help_text(u,c):
  u.message.reply_text(HELP_TEXT,reply_markup=reply_markup,parse_mode=ParseMode.MARKDOWN)

from telethon import custom, events, Button
import os,re
from YuiGBot import telethn as bot
from YuiGBot import telethn as tgbot
from YuiGBot.events import register 
@register(pattern="/myinfo")
async def YuiGBot(event):
  button = [[custom.Button.inline("CHECK",data="information")]]
  await bot.send_message(event.chat, "YOUR INFORMATION",buttons=button)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
  try:
    boy = event.sender_id
    PRO = await bot.get_entity(boy)
    YuiGBot = "YOUR DETAILS \n"
    YuiGBot += f"FIRST NAME : {first_name} \n"
    YuiGBot += f"LAST NAME : {user.last_name}\n"
    YuiGBot += f"YOU BOT : {bot} \n"
    YuiGBot += f"RESTRICTED : {restricted} \n"
    YuiGBot += f"USER ID : {user.id}\n"
    YuiGBot += f"USERNAME : {user.username}\n"
    await event.answer(YuiGBot, alert=True)
  except Exception as e:
    await event.reply(f"{e}")

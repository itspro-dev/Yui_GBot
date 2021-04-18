import asyncio
import aiohttp
import re
from config2 import token, owner_id, bot_id
from pyrogram import Client, filters

eliana = Client(
    ":memory:",
    token="1414346382:AAF9oz4SNi1LaNF0Cph9mtdZfD8OhnkipPc",
    api_id=1979859,
    api_hash="2d8efd791d4ae887c2411aee30f3542e",
)


async def chatbot(text):
    url = f"https://elianaapi.herokuapp.com/eliana/chatbot?text={text}&name=eliana"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            res = await res.json()
            text = res["message"]
            return text

@eliana.on_message(filters.command("about") & ~filters.edited)
async def about(_, message):
    await message.reply_text(
        "[Eliana Api](https://elianaapi.herokuapp.com/)"
        + " | [Owner](https://github.com/Red-Aura/Eliana-Api)", disable_web_page_preview=True)


@eliana.on_message(filters.command("eliana") & ~filters.edited)
async def start(_, message):
    await eliana.send_chat_action(message.chat.id, "typing")
    await message.reply_text(
        "**I Am Eliana Chatbot**"
    )



@eliana.on_message(
    ~filters.private 
    & ~filters.command("help")
    & ~filters.edited
)
async def chat(_, message):
    if message.reply_to_message:
        if not message.reply_to_message.from_user.id == bot_id:
            return
        await eliana.send_chat_action(message.chat.id, "typing")
        if not message.text:
            query = "Hello"
        else:
            query = message.text
        if len(query) > 50:
            return
        try:
            res = await chatbot(query)
            await asyncio.sleep(1)
        except Exception as e:
            res = str(e)
        await message.reply_text(res)
        await eliana.send_chat_action(message.chat.id, "cancel")
    else:
        if message.text:
            query = message.text
            if len(query) > 50:
                return
            if re.search("[.|\n]{0,}[l|L][u|U][n|N][a|A][.|\n]{0,}", query):
                await eliana.send_chat_action(message.chat.id, "typing")
                try:
                    res = await chatbot(query)
                    await asyncio.sleep(1)
                except Exception as e:
                    res = str(e)
                await message.reply_text(res)
                await eliana.send_chat_action(message.chat.id, "cancel")


@eliana.on_message(
    filters.private
    & ~filters.command("help")
    & ~filters.edited
)
async def chatpm(_, message):
    if not message.text:
        return
    await eliana.send_chat_action(message.chat.id, "typing")
    query = message.text
    if len(query) > 50:
        return
    try:
        res = await chatbot(query)
        await asyncio.sleep(1)
    except Exception as e:
        res = str(e)
    await message.reply_text(res)
    await eliana.send_chat_action(message.chat.id, "cancel")


print(
    """
  Eliana Started
"""
)


eliana.run()

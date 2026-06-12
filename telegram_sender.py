from telegram import Bot
from config import BOT_TOKEN, CHANNEL_ID
import asyncio

async def send_signal(message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(
        chat_id=CHANNEL_ID,
        text=message
    )

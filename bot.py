import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram import types
from config import TELEGRAM_BOT_TOKEN


bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


async def send_message_to_user(user_id: int, text: str):
    await bot.send_message(chat_id=user_id, text=text, parse_mode="HTML")


@dp.message(Command("start"))
async def start(message: types.Message, bot: Bot):
    user_id = message.chat.id
    await bot.send_message(chat_id=user_id, text=f"Ваш id : {user_id}")

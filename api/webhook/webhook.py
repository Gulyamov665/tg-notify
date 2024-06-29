from fastapi import APIRouter
from config import WEBHOOK_PATH
from aiogram import types
from settings import logger
from bot import bot, dp


router = APIRouter()


@router.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    logger.info(f"Webhook received update: {update}")
    update = types.Update(**update)
    await dp.feed_update(bot, update)

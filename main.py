from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic_types import MessageRequest, ShopOrder
from aiogram import types
from bot import send_message_to_user, bot, dp
from utils.create_text import create_text, create_shop_order
from config import TELEGRAM_BOT_TOKEN, WEBHOOK_URL, WEBHOOK_PATH
from api.views import router as aurora_router
from api.webhook.webhook import router as webhook_router
import logging
from settings import logger


# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


origins = ["*"]

# WEBHOOK_PATH = f"/bot/{TELEGRAM_BOT_TOKEN}"
# WEBHOOK_URL = "https://tg-notify-devteam-a9d6d4f8.koyeb.app" + WEBHOOK_PATH
# WEBHOOK_URL = "https://5f91-84-54-82-236.ngrok-free.app" + WEBHOOK_PATH


async def lifespan(app: FastAPI):
    logger.info("Запуск: Установка вебхука.")
    await bot.set_webhook(WEBHOOK_URL)
    print("Опять работа...")

    yield

    logger.info("Завершение работы: Удаление вебхука и закрытие сессии бота.")
    print("Нужно больше золото...")
    await bot.delete_webhook()
    await bot.session.close()


app = FastAPI(lifespan=lifespan)
app.include_router(aurora_router, tags=["aurora-notification"])
app.include_router(webhook_router, tags=["webhook"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.post(WEBHOOK_PATH)
# async def bot_webhook(update: dict):
#     logger.info(f"Webhook received update: {update}")
#     update = types.Update(**update)
#     await dp.feed_update(bot, update)


@app.post("/send_message/")
async def send_message_users(message: MessageRequest):
    text = create_text(message.dict())
    users_id = [user.chat_id for user in message.observers_profile]
    ex_id = (
        message.executor_profile.chat_id if message.executor_profile.chat_id else None
    )
    await send_message_to_user(ex_id, text)
    for user_id in users_id:
        await send_message_to_user(user_id, text)

    return {"status": "messages sent"}


# @app.post("/dispatcher/")
# async def send_message_to_group(messages: Order):
#     availability = messages.dict()["availability"]
#     text = create_order(messages.dict())
#     group_id = messages.dict()["chat_id"]
#     if availability:
#         await send_message_to_user(group_id, text)
#         return {"status": "Order created and message sended"}
#     return {"status": "Orders is not available in this vendor"}


# @app.post("/waiterCall/")
# async def send_message_to_group(messages: WaiterCall):
#     message = messages.dict()["table"]
#     text = f"📲 вызов официанта за стол  №{message}"
#     group_id = messages.dict()["chat_id"]
#     await send_message_to_user(group_id, text)
#     return {"status": "message sended"}


@app.post("/shop/")
async def send_message_to_group(messages: ShopOrder):
    text = create_shop_order(messages.dict())
    group_id = messages.dict()["chat_id"]
    await send_message_to_user(group_id, text)
    return {"status": "message sended"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)

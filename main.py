from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from pydantic_types import MessageRequest, ShopOrder
from bot import send_message_to_user, bot
from utils.create_text import create_text, create_shop_order
from config import WEBHOOK_URL
from api.views import router as aurora_router
from api.webhook.webhook import router as webhook_router
from settings import logger


origins = ["*"]


async def lifespan(app: FastAPI):
    logger.info("Запуск: Установка вебхука.")
    await bot.set_webhook(WEBHOOK_URL)
    print("Опять работа...")

    yield

    logger.info("Завершение работы: Удаление вебхука и закрытие сессии бота.")
    print("Нужно больше золото...")
    await bot.delete_webhook()
    await bot.session.close()


app = FastAPI(default_response_class=ORJSONResponse, lifespan=lifespan)
app.include_router(aurora_router, tags=["aurora-notification"])
app.include_router(webhook_router, tags=["webhook"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


@app.post("/shop/")
async def send_message_to_group(messages: ShopOrder):
    text = create_shop_order(messages.dict())
    group_id = messages.dict()["chat_id"]
    await send_message_to_user(group_id, text)
    return {"status": "message sended"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)

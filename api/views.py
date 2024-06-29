from fastapi import APIRouter
from .schemas import Order, WaiterCall
from bot import send_message_to_user
from utils.create_text import create_order

router = APIRouter()


@router.post("/dispatcher/")
async def send_message_to_group(messages: Order):
    availability = messages.dict()["availability"]
    text = create_order(messages.dict())
    group_id = messages.dict()["chat_id"]
    if availability:
        await send_message_to_user(group_id, text)
        return {"status": "Order created and message sended"}
    return {"status": "Orders is not available in this vendor"}


@router.post("/waiterCall/")
async def send_message_to_group(messages: WaiterCall):
    message = messages.dict()["table"]
    text = f"📲 вызов официанта за стол  №{message}"
    group_id = messages.dict()["chat_id"]
    await send_message_to_user(group_id, text)
    return {"status": "message sended"}

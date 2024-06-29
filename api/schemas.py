from pydantic import BaseModel
from typing import List


class Items(BaseModel):
    name: str
    price: int
    count: int


class Order(BaseModel):
    items: List[Items]
    totalPrice: int
    table: str
    chat_id: int
    availability: bool


class WaiterCall(BaseModel):
    table: str
    chat_id: int

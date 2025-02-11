from pydantic import BaseModel
from typing import List, Dict, Optional


class ExecutorProfile(BaseModel):
    user: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    chat_id: Optional[int] = None
    avatar: Optional[str] = None


class ObserverProfile(BaseModel):
    user: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    chat_id: Optional[int] = None
    avatar: Optional[str] = None


class MessageRequest(BaseModel):
    id: int
    created_at: Optional[str] = None
    name: Optional[str] = None
    start_time: Optional[str] = None
    dead_line: Optional[str] = None
    status: Optional[str] = None
    executor: Optional[int] = None
    observers: Optional[List[int]] = None
    comments: Optional[str] = None
    priority: Optional[str] = None
    classification: Optional[int] = None
    classification_name: Optional[str] = None
    task_images: Optional[List[str]] = None
    executor_profile: ExecutorProfile
    observers_profile: Optional[List[ObserverProfile]] = None
    task_comment: Optional[List[Dict]] = None


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


class ShopItems(BaseModel):
    name: str
    price: float
    quantity: int
    size: str
    color: str


class ShopOrder(BaseModel):
    username: str
    chat_id: int
    orderLoc: str
    totalPrice: int
    items: List[ShopItems]


class MondayPromo(BaseModel):
    firstname: Optional[str]
    lastname: Optional[str]
    phone: Optional[int]
    chat_id : int


class BonBon(BaseModel):
    firstname: Optional[str]
    lastname: Optional[str]
    phone: Optional[str]
    comment: str
    chat_id : int
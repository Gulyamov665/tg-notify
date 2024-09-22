def create_text(message: dict):
    id = message["id"]
    name = message["name"]
    created_at = message["created_at"]
    dead_line = message["dead_line"]
    classification_name = message["classification_name"]
    comments = message["comments"]
    executor_name = message["executor_profile"]["first_name"]
    executor_last_name = message["executor_profile"]["last_name"]
    priority = message["priority"]
    status = message["status"]
    return f"""  
🟢 Новая задача

🆔 Id : {id if id else None}
🎯 Название : {name if name else None}
📅 Создан : {created_at if created_at else None}
📅 Конец : {dead_line if dead_line else None}
✉️ Классификация : {classification_name if classification_name else None}
🗒️ Комментарии : {comments if comments else None}
🤵‍♂️ Исполнитель : {executor_name if executor_name else None} {executor_last_name if executor_last_name else None}
🚨 Приоритет : {priority if priority else None}
★ Статус : {status if status else None}
    """


def create_order(messages: dict):
    table1 = messages["table"]
    totalPrice = messages["totalPrice"]
    items = messages["items"]
    header = "<b>🟢 —Новый заказ—</b> \n\n"
    table_info = f"<b>🍽 Стол: № {table1}</b>\n\n"
    order = "<b>🧾  Состав заказа:</b>\n"
    linear = "<b>————————————————</b>\n"
    info = ""
    for message in items:
        name = message["name"]
        count = message["count"]
        price = message["price"]
        line = f"<b>— {name} х {count} от {price} сум</b>\n\n"
        info += line
    full = (
        header
        + table_info
        + order
        + linear
        + info
        + linear
        + f"<b>💳 Итого: {totalPrice}</b>\n"
    )
    return full


def create_shop_order(messages: dict):
    username = messages["username"]
    location = messages["orderLoc"]
    totalPrice = messages["totalPrice"]
    # color = messages["color"]
    # size = messages["size"]
    items = messages["items"]
    header = "<b>🟢 —New Order—</b> \n\n"
    table_info = f"<b>👤 Customer name: {username}</b>\n\n"
    location = f"<b>📍 Location: {location}</b>\n\n"
    # phone = f"<b>📞 Customer phone number: {phone}</b>\n\n"
    order = "<b>🧾  Order's compound:</b>\n"
    linear = "<b>————————————————</b>\n"
    info = ""
    for message in items:
        name = message["name"]
        count = message["quantity"]
        price = message["price"]
        color = message["color"]
        size = message["size"]
        line = f"🛒 <b>— {name} х {count} от {price} $</b>\n\n"
        color = f"🌈 Color <b>— {color}</b>\n\n"
        size = f"Size <b>— {size}</b>\n\n"
        info += line + color + size
    full = (
        header
        + table_info
        + order
        + linear
        + info
        + location
        + linear
        + f"<b>💸 Итого: {totalPrice}</b>\n"
    )
    return full


def monday_promo(messages: dict):
    name = messages["firstname"]
    lastname = messages["lastname"]
    phone = messages["phone"]

    header = "<b>👤 —New Request—</b> \n\n"
    firstname = f"<b> Фамилия: {name}</b>\n\n"
    lastname = f"<b> Имя: {lastname}</b>\n\n"
    phone = f'<b> Номер: <a href="tel:{phone}">{phone}</a></b>\n\n'
    linear = "<b>————————————————</b>\n"

    full = header + firstname + lastname + phone + linear
    return full

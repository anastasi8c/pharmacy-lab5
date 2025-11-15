def calculate_total(price, quantity, discount=0):
    return price * quantity * (1 - discount / 100)


def calculate_discount_multiplier(discount):
    return 1 - discount / 100


def apply_discount(price, discount):
    return price * (1 - discount / 100)


def display_order_summary(price, quantity, discount):
    total = calculate_total(price, quantity, discount)
    return f"Заказ: {quantity} шт. по {price} руб. со скидкой {discount}% = {total} руб."


def check_stock(quantity):
    """Проверяет уровень запасов"""
    if quantity < 10:  # Оставляем порог 10 из main
        return "НИЗКИЙ ЗАПАС!"  # Оставляем сообщение из main
    return "OK"


if __name__ == "__main__":
    print("Расчет стоимости заказа:")
    total = calculate_total(price=150, quantity=5, discount=10)
    print(f"Итого: {total} руб.")


    stock_status = check_stock(3)
    print(f"Статус запасов: {stock_status}")
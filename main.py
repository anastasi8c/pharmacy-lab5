# Намеренно создаем настоящую ошибку
def calculate_total(price, quantity, discount=0):
    return price * quantity * (1 - discount / 100)  # УБИРАЕМ вызов функции = ЛОГИЧЕСКАЯ ОШИБКА!

def calculate_discount_multiplier(discount):
    return 1 - discount / 100

def apply_discount(price, discount):
    return price * (1 - discount / 100)

def display_order_summary(price, quantity, discount):
    total = calculate_total(price, quantity, discount)
    return f"Заказ: {quantity} шт. по {price} руб. со скидкой {discount}% = {total} руб."


def check_stock(quantity):
    """Проверяет уровень запасов"""
    if quantity < 5:
        return "Низкий запас"
    return "Запас нормальный"



if __name__ == "__main__":
    print("Расчет стоимости заказа:")
    total = calculate_total(price=150, quantity=5, discount=10)
    print(f"Итого: {total} руб.")

    # Новая функциональность - проверка запасов
    stock_status = check_stock(3)
    print(f"Статус запасов: {stock_status}")

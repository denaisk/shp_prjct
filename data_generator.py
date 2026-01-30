import time
import random
from prometheus_client import start_http_server, Counter, Gauge

# 1. Определяем метрики
# Counter — счетчик, который только растет (как общее число заказов)
ORDERS_TOTAL = Counter('shop_orders_total', 'Total number of orders', ['status', 'product_category'])
# Gauge — показатель, который может идти вверх и вниз (как цена последнего заказа)
LAST_ORDER_PRICE = Gauge('shop_last_order_price', 'Price of the last processed order')

def generate_data():
    categories = ['Electronics', 'Books', 'Clothing', 'Home']
    statuses = ['success', 'success', 'success', 'failed'] # 25% ошибок для интереса

    while True:
        # Имитируем случайные данные
        cat = random.choice(categories)
        status = random.choice(statuses)
        price = random.uniform(10.0, 500.0)

        # Записываем данные в метрики
        ORDERS_TOTAL.labels(status=status, product_category=cat).inc()
        LAST_ORDER_PRICE.set(price)

        print(f"Generated: {cat} - {status} - ${price:.2f}")
        
        # Пауза между событиями (имитируем нагрузку)
        time.sleep(random.uniform(1, 5))

if __name__ == '__main__':
    # Запускаем мини-сервер на порту 8000, откуда Prometheus будет брать данные
    start_http_server(8000)
    print("Generator started on port 8000...")
    generate_data()
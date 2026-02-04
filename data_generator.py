import time
import random
from prometheus_client import start_http_server, Counter, Gauge

# Метрики
ORDERS_TOTAL = Counter('shop_orders_total', 'Total number of orders', ['status', 'product_category'])
LAST_ORDER_PRICE = Gauge('shop_last_order_price', 'Price of the last processed order')
REVENUE_TOTAL = Counter('shop_revenue_total', 'Total revenue', ['product_category'])

def generate_data():
    categories = ['Electronics', 'Books', 'Clothing', 'Home']
    statuses = ['success', 'success', 'success', 'failed'] # 25% ошибок для интереса

    while True:
        cat = random.choice(categories)
        status = random.choice(statuses)
        price = random.uniform(10.0, 500.0)

        # Записываем данные в метрики
        ORDERS_TOTAL.labels(status=status, product_category=cat).inc()
        REVENUE_TOTAL.labels(product_category=cat).inc(price)
        LAST_ORDER_PRICE.set(price)

        print(f"Generated: {cat} - {status} - ${price:.2f}")
        
        # Пауза между событиями (имитируем нагрузку)
        time.sleep(random.uniform(1, 5))

if __name__ == '__main__':
    # Запускаем мини-сервер на порту 8000, откуда Prometheus будет брать данные
    start_http_server(8000)
    print("Generator started on port 8000...")
    generate_data()
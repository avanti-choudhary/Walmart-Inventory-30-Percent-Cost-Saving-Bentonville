# kafka_producer.py - Simulates Walmart POS real-time sales stream
# Senior Concept: Producer = Walmart Store POS sending data every second

import json
import time
import random
from datetime import datetime

# Simulating Kafka - writes to a file that consumer will read live
# For real Walmart cluster, this would be: KafkaProducer(bootstrap_servers='walmart-kafka:9092')

PRODUCTS = [
    {"product_id": 101, "product_name": "Milk", "price": 3.5},
    {"product_id": 102, "product_name": "Bread", "price": 2.5},
    {"product_id": 103, "product_name": "Eggs", "price": 4.0},
]

print("🟢 Walmart POS Producer Started - Sending live sales...")

while True:
    sale = random.choice(PRODUCTS)
    event = {
        "store_id": "WMT-Bentonville-001",
        "product_id": sale["product_id"],
        "product_name": sale["product_name"],
        "quantity": random.randint(1, 5),
        "price": sale["price"],
        "timestamp": datetime.now().isoformat()
    }
    # In real Kafka: producer.send('walmart_sales', event)
    # For your project (works without Kafka server): append to stream file
    with open("live_sales_stream.jsonl", "a") as f:
        f.write(json.dumps(event) + "\n")
    
    print(f"📤 Sent: {event}")
    time.sleep(2) # new sale every 2 seconds
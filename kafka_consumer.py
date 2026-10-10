# kafka_consumer.py - Consumes real-time stream for inventory calculation
# Senior Concept: Consumer = Data Pipeline that updates inventory in real-time

import json
import time
import os

print("🔵 Walmart Inventory Consumer Started - Listening...")

# Clear old stream
if os.path.exists("live_sales_stream.jsonl"):
    os.remove("live_sales_stream.jsonl")

# Simulate consuming live
seen_lines = 0
while True:
    if os.path.exists("live_sales_stream.jsonl"):
        with open("live_sales_stream.jsonl", "r") as f:
            lines = f.readlines()
            # Only read new lines
            for line in lines[seen_lines:]:
                event = json.loads(line)
                print(f"📥 Consumed: Store {event['store_id']} sold {event['quantity']}x {event['product_name']} | Need to update inventory")
            seen_lines = len(lines)
    time.sleep(1)
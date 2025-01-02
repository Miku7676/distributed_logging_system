import json
import os
from kafka import KafkaConsumer


KAFKA_BROKER = os.getenv('KAFKA_BROKER', 'broker:9092')
print(f"Connecting to Kafka broker at {KAFKA_BROKER}")
consumer = KafkaConsumer('info_log',\
                         bootstrap_servers=[KAFKA_BROKER],\
                         auto_offset_reset = 'earliest',\
                         group_id = 'log_group',\
                         value_deserializer = lambda x: json.loads(x.decode('utf-8')))


print("waiting")
for message in consumer:
    print(message.value)
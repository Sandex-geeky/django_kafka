import json
from kafka import KafkaConsumer
from time import sleep

consumer = KafkaConsumer(
    'topic_traffic_log',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for event in consumer:
    data = event.value
    user_id = data.get('user_id')
    traffic_mb = data.get('traffic_mb')
    total_cost = data.get('total_cost')
    print(f'User: {user_id}, Traffic MBytes: {traffic_mb}, Cost: {total_cost}')
    
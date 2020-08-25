import json
import os
from time import sleep

from celery import shared_task
from kafka import KafkaProducer


@shared_task
def calc_money(user_id, traffic_mb):
    COST_PER_MB = 0.05
    data = {
        'user_id': user_id,
        'traffic_mb': traffic_mb,
        'total_cost': traffic_mb * COST_PER_MB,
    }
    producer = KafkaProducer(
        bootstrap_servers=['{0}:{1}'.format(os.getenv('KAFKA_HOST'),os.getenv('KAFKA_PORT'))],
        value_serializer=lambda x: json.dumps(x).encode('utf-8')
    )
    producer.send('topic_traffic_log', value=data)
import datetime
import json
import random

import pika
import sys

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='task_exchange', exchange_type='direct')
channel.queue_declare(queue='task_queue', durable=True)
channel.queue_bind(exchange='task_exchange', queue='task_queue')

count = 0

while True:
    count += 1
    if count > 10:
        break

    message = {
        "id": count,
        "payload": random.randint(1, 3000),
        "date": datetime.datetime.now().isoformat()
    }

    channel.basic_publish(
        exchange='task_exchange',
        routing_key='task_queue',
        body=json.dumps(message).encode(),
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ))

    print(" [x] Sent %r" % message)

connection.close()

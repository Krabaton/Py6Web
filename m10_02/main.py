import pika
from faker import Faker
import random
from models.models import Contacts

fake = Faker()


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange='mail_service', exchange_type='direct')
    channel.queue_declare(queue='marketing_campaign', durable=True)
    channel.queue_bind(exchange='mail_service', queue='marketing_campaign')

    for count in range(1, 20):
        contact = Contacts(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            cell_phone=fake.phone_number(),
            age=random.randint(21, 75)
        ).save()

        channel.basic_publish(
            exchange='mail_service',
            routing_key='marketing_campaign',
            body=str(contact.id).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))

    connection.close()


if __name__ == '__main__':
    main()

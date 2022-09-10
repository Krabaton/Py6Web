import pika
import time
from models.models import Contacts
from services.mail import send_email


def callback(ch, method, properties, body):
    _id = body.decode()
    contact, = Contacts.objects(id=_id, completed=False)
    if contact:
        email = contact.email
        first_name = contact.first_name
        last_name = contact.last_name
        send_email('noreply@natalia_co.com', email, f"<h1> Hello <span>{first_name} {last_name}</span></h1>")
        Contacts.objects(id=_id).update_one(set__completed=True)
        time.sleep(1)
        print(f" [x] Done: {first_name} {last_name}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='marketing_campaign', durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='marketing_campaign', on_message_callback=callback)

    channel.start_consuming()


if __name__ == '__main__':
    main()

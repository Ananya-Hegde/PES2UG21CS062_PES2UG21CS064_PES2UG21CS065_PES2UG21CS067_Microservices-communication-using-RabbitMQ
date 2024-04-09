# consumer_one.py
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='item_creation')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print("item_creation")

channel.basic_consume(queue='item_creation', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for item_creation requests. To exit press CTRL+C')
channel.start_consuming()

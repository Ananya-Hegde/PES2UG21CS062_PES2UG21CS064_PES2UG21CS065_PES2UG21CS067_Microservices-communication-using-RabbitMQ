# consumer_one.py
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='order_processing')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print("order_processing")

channel.basic_consume(queue='order_processing', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for order_processing requests. To exit press CTRL+C')
channel.start_consuming()

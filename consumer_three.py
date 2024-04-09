# consumer_one.py
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='stock_management')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print("stock_management")

channel.basic_consume(queue='stock_management', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for stock management requests. To exit press CTRL+C')
channel.start_consuming()

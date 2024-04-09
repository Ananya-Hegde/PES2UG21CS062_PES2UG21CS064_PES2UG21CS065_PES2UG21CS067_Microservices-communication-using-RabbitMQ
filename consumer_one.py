# consumer_one.py
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='health_check')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print("Good health")

channel.basic_consume(queue='health_check', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for Health Check requests. To exit press CTRL+C')
channel.start_consuming()

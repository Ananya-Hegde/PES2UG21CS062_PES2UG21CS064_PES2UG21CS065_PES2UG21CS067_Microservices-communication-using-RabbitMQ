# producer.py
from flask import Flask, request
import pika
import json

app = Flask(__name__)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='health_check')
channel.queue_declare(queue='item_creation')
channel.queue_declare(queue='stock_management')
channel.queue_declare(queue='order_processing')

@app.route("/")
def hello_world():
    return "hello world"

@app.route('/health_check')
def health_check():
    # data = request.json
    data = "inside health_check"
    channel.basic_publish(exchange='', routing_key='health_check',body=data)
    return 'Health Check Request Sent to Consumer One'
    

@app.route('/item_creation')
def item_creation():
    # data = request.json
    data = "inside item creation"
    channel.basic_publish(exchange='', routing_key='item_creation', body=data)
    return 'Item Creation Request Sent to Consumer Three'

@app.route('/stock_management')
def stock_management():
    # data = request.json
    data = "inside stock management"
    channel.basic_publish(exchange='', routing_key='stock_management', body=data)
    return 'Stock Management Request Sent to Consumer Three'

@app.route('/order_processing')
def order_processing():
    # data = request.json
    data = "inside order processing"
    channel.basic_publish(exchange='', routing_key='order_processing',body=data ) 
    return 'Order Processing Request Sent to Consumer Four'

if __name__ == '__main__':
    app.run(debug=True, port=5000)

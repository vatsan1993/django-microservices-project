#amqps://cakgpxbg:bnTjHn6fSaH3o7aS1vmenXlJQxHekWTH@seal.lmq.cloudamqp.com/cakgpxbg

import pika, json

params = pika.URLParameters('amqps://cakgpxbg:bnTjHn6fSaH3o7aS1vmenXlJQxHekWTH@seal.lmq.cloudamqp.com/cakgpxbg')



def publish(method, body):
    connection = pika.BlockingConnection(params)

    channel = connection.channel()
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)

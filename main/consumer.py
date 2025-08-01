

import pika, json
from main import app,Product, db

params = pika.URLParameters('amqps://cakgpxbg:bnTjHn6fSaH3o7aS1vmenXlJQxHekWTH@seal.lmq.cloudamqp.com/cakgpxbg')

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='main')
print('Received in main')

def callback(channel, method, properties, body):

    if body:
        data = json.loads(body)
        print(data)
        with app.app_context():
            if properties.content_type == 'product_created':
                product = Product(id =data['id'], title=data['title'], image=data['image'])
                db.session.add(product)
                db.session.commit()
            elif properties.content_type == 'product_updated':
                product = Product.query.get(data['id'])
                if product:
                    product.title = data['title']
                    product.image = data['image']
                    db.session.commit()
            elif properties.content_type == 'product_deleted':
                product = Product.query.get(data['id'])
                if product:
                    db.session.delete(product)
                    db.session.commit()

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')
channel.start_consuming()

connection.close()
#amqps://cakgpxbg:bnTjHn6fSaH3o7aS1vmenXlJQxHekWTH@seal.lmq.cloudamqp.com/cakgpxbg
import pika, json, os, django, sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()
from products.models import Product

params = pika.URLParameters('amqps://cakgpxbg:bnTjHn6fSaH3o7aS1vmenXlJQxHekWTH@seal.lmq.cloudamqp.com/cakgpxbg')


connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
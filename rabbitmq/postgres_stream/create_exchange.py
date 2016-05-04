import pika

# connect to rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters( 'localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='nlp01', type='direct')

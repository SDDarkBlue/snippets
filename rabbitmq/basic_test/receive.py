import pika

# connect to rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters( 'localhost'))
channel = connection.channel()

# Declare the queue (not necessary if sender was run first, but good practice)
channel.queue_declare(queue='hello')


# this callback function will be called by pika when a message comes in
def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

# link the callback function to the 'hello' queue
# This will fail if the queue does not exist
channel.basic_consume(callback, queue='hello', no_ack=True)

# Start consuming
print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()

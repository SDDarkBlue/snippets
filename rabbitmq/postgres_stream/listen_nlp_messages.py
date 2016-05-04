import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='nlp01', type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='nlp01', queue=queue_name, routing_key='all')

print ' [*] Waiting for nlp01 updates. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received message: "
    print "        method: %r" % (method,)
    print "        properties: %r" % (properties,)
    print "        body: %r" % (body,)
    print ""

channel.basic_consume(callback, queue=queue_name, no_ack=True) 
channel.start_consuming()

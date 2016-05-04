import pika
import pickle
import pandas as pd
import sys
import uuid
from mm_models import FishTrackingDetectionSchema


def set_up_mq_channel():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='fish_tracking', type='fanout')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange='fish_tracking', queue=queue_name)
    return {'connection': connection, 'channel': channel, 'queue': queue_name}

def callback(ch, method, properties, body):
    print '[x] data chunk received. Start processing.'
    data_obj = pickle.loads(body)
    schema = FishTrackingDetectionSchema()
    data = schema.dump(data_obj, many=True)
    if data.errors != {}:
        print 'errors during validation:'
        for key, value in data.errors.iteritems():
            print '{0}:'.format(key)
            print value
        sys.exit(-1)
    df = pd.DataFrame.from_records(data.data)
    df.fillna('')
    fileid = uuid.uuid1()
    filename = 'received_data_chunk_{0}.csv'.format(fileid.hex)
    df.to_csv(filename, sep=',', index=False, na_rep='')
    print '[x] data chunk written to file.'

def main():
    conn_data = set_up_mq_channel()
    conn_data['channel'].basic_consume(callback, queue=conn_data['queue'], no_ack=True)
    print ' [*] Waiting for messages. To exit press CTRL+C'
    conn_data['channel'].start_consuming()

main()
import pandas as pd
import pickle
import pika
import sys
from mm_models import FishTrackingDetectionSchema

def set_up_mq_channel():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='fish_tracking', type='fanout')
    return {'connection': connection, 'channel': channel}


def csvrows_to_obj(rows, as_bytes=False):
    if as_bytes:
        return pickle.dumps(FishTrackingDetectionSchema(many=True).load(rows))
    else:
        return FishTrackingDetectionSchema(many=True).load(rows)


def dataframe_to_obj(d):
    data = d.T.to_dict().values()
    return csvrows_to_obj(data)


def byte_data_stream(indata, channel):
    records_per_chunk = 5000
    for i in range(0, len(indata), records_per_chunk):
        msg_body = pickle.dumps(indata[i:i+records_per_chunk])
        msg_properties = create_message_properties()
        publish_message(channel, msg_body, msg_properties)
        print '[*] message published'

def create_message_properties():
    msg_properties = pika.BasicProperties()
    msg_properties.content_type = 'byte'
    return msg_properties

def publish_message(channel, msg_body, msg_properties):
    channel.basic_publish(body=msg_body, exchange='fish_tracking', properties=msg_properties, routing_key='')

def main():

    connection_data = set_up_mq_channel()
    infile = '../test_data/test9l.csv'
    data_cols = ['datetime', 'receiver_id', 'transmitter_id', 'old_station_name', 'station_name', 'latitude',
                  'longitude']
    data = pd.read_csv(infile, sep=',', header=0, names=data_cols)
    serlzd_data = dataframe_to_obj(data)
    if serlzd_data.errors != {}:
        print 'errors during validation:'
        for key, value in serlzd_data.errors.iteritems():
            print '{0}:'.format(key)
            print value
        sys.exit(-1)
    byte_data_stream(serlzd_data.data, connection_data['channel'])
    connection_data['connection'].close()

main()
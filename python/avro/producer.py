from kafka import KafkaProducer
import avro.schema
import io
from avro.io import DatumWriter

data = {'name': 'Tony', 'favorite_number': 8, 'favorite_color': 'green'}

schema = avro.schema.parse(open('./schema.avsc').read())

def serialize(data):
    writer = DatumWriter(schema)
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    writer.write(data, encoder)
    return bytes_writer.getvalue()


producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=serialize)
producer.send('test2', data)
producer.flush()
producer.close() # close will also flush, but I'm leaving it in here for demonstration purposes

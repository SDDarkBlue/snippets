from kafka import KafkaConsumer
from kafka.common import TopicPartition
import avro.schema
import avro.io
import io

consumer = KafkaConsumer(bootstrap_servers=['localhost:9092'])
consumer.assign([TopicPartition('test2', 0)])
consumer.seek(TopicPartition('test2', 0), 0)
print consumer.committed(TopicPartition('test2', 0))

schema = avro.schema.parse(open('./schema.avsc').read())

for msg in consumer:
    bytes_reader = io.BytesIO(msg.value)
    decoder = avro.io.BinaryDecoder(bytes_reader)
    reader = avro.io.DatumReader(schema)
    user = reader.read(decoder)
    consumer.commit()
    print(user)

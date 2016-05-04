import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.parse(open('./schema.avsc', 'rb').read())

# Create an avro file

writer = DataFileWriter(open('user.avro', 'wb'), DatumWriter(), schema)
writer.append({'name': 'Eric', 'favorite_number': 128})
writer.append({'name': 'Tanya', 'favorite_color': 'red', 'favorite_number': 383})
writer.close()

# Now read that file

reader = DataFileReader(open('user.avro', 'rb'), DatumReader())
for user in reader:
    print user
reader.close()

from boto.dynamodb2.layer1 import DynamoDBConnection
from boto.dynamodb2.table import Table

DEFAULTS = {
    'tablename': 'detections',
}

conn = DynamoDBConnection(aws_access_key_id='foo', aws_secret_access_key='bar', host='localhost', port=8000, is_secure=False)
table = Table(DEFAULTS['tablename'], connection=conn)

# query for transmitter
resultset = table.query_2(transmitter__eq='A69-1601-14872')
for r in resultset:
    print r

# query for receiver
resultset = table.scan(receiver__eq='VR2W-115434')

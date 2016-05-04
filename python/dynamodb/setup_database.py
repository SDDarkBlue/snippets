import pandas as pd
import sys
from boto.dynamodb2 import connect_to_region
from boto.dynamodb2.layer1 import DynamoDBConnection
from boto.dynamodb2.fields import HashKey, RangeKey
from boto.dynamodb2.table import Table

def check_arguments():
    if len(sys.argv) != 2:
        print 'usage: ./setup_database.py <l or s> (for local or service)'
        sys.exit(-1)
    return sys.argv[1]

def connectToDynamoLocal():
    """
    connect to DynamoDB Local. This will fail if it is not running on localhost:8000.
    """
    print 'connecting to local dynamodb...'
    conn = DynamoDBConnection(aws_access_key_id='foo', aws_secret_access_key='bar', host='localhost', port=8000, is_secure=False)
    print 'connected.'
    return conn

def connectToDynamoService():
    """
    This will use your ~/.boto configuration file containing
    access key and access secret
    """
    print 'connecting to service dynamodb...'
    conn = connect_to_region('eu-west-1')
    print 'connected.'
    return conn

def createTable(conn):
    print 'creating table detections...'
    logs = Table.create('detections', schema=[HashKey('transmitter'), RangeKey('timestamp')], connection=conn)
    print 'table created.'
    return logs

def connectToTable(conn):
    print 'connecting to table detections...'
    logs = Table('detections', connection=conn)
    print 'connected.'
    return logs

def readTestData():
    print 'reading test data...'
    TESTFILE = 'testdata.csv'
    d = pd.read_csv(TESTFILE, encoding='utf-8-sig')
    d.columns = ['date', 'time', 'receiver', 'transmitter', 'transmittername', 'transmitterserial', 'sensorvalue', 'sensorunit', 'stationname', 'latitude', 'longitude']
    d['timestamp'] = d['date'] + ' ' + d['time']
    print 'test data read.'
    return d

def writeItem(item, table=None):
    table.put_item(data=dict(item[item.notnull()]))

def main():
    mode = check_arguments()
    if mode == 'l':
        conn = connectToDynamoLocal()
    elif mode == 's':
        conn = connectToDynamoService()
    if 'detections' in conn.list_tables()['TableNames']:
        table = connectToTable(conn)
    else:
        table = createTable(conn)
    data = readTestData()
    encoded_data = data.apply(lambda x: x.apply(lambda y: y.encode('utf-8') if isinstance(y, unicode) else y))
    encoded_data.apply(writeItem, axis=1, table=table)

main()

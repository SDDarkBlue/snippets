from datetime import date
import pickle
import sys
from marshmallow import Schema, fields, pprint

class ArtistSchema(Schema):
    name = fields.Str()
    release_date = fields.Date()
    number_of_times_sold = fields.Number()

if __name__ == '__main__':
    schema = ArtistSchema()
    data = {'name': 'this is an artist', 'release_date': date(1970, 4, 2), 'number_of_times_sold': 4929492}
    data_str = str(data)
    result = schema.dump(data)
    pck_data = pickle.dumps(result.data)
    pprint(result.data, indent=2)
    print 'size of original data as dict: %s' % sys.getsizeof(data)
    print 'size of original data as string: %s' % sys.getsizeof(data_str)
    print 'size of data after marshalling: %s' % sys.getsizeof(result.data)
    print 'size of data after pickling: %s' % sys.getsizeof(pck_data)
    print 'size of entire marshalling result: %s' % sys.getsizeof(result)
    print '[x]: marshalled data:'
    print result.data
    print '[x]: pickled data:'
    print pck_data
    print '[x]: marshalled result:'
    print result

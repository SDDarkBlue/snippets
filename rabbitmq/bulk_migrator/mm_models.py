from marshmallow import Schema, fields
from mm_custom_fields import cDateTime


class FishTrackingDetectionSchema(Schema):
    datetime = cDateTime(required=True, format='%Y-%m-%d %H:%M:%S')
    receiver_id = fields.Str()
    transmitter_id = fields.Str(required=True)
    old_station_name = fields.Str()
    station_name = fields.Str(required=True)
    latitude = fields.Decimal(places=5)
    longitude = fields.Decimal(places=5)

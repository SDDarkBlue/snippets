#!/usr/bin/python

import sys
import requests
import simplejson as json

if len(sys.argv) != 2:
    print "usage: ./get_coordinates.py location_name"
    sys.exit(-1)

location_name = sys.argv[1]
parameters = {"format": "json", "q": location_name}
r = requests.get("http://open.mapquestapi.com/nominatim/v1/search.php", params=parameters)
data = json.loads(r.text)
coordinates = []
for result_point in data:
    name = result_point["display_name"].encode("utf-8")
    lat = result_point["lat"]
    lon = result_point["lon"]
    coordinates.append("{0}:\t{1} {2}".format(name, lon, lat))
for coordinate in coordinates:
    print coordinate

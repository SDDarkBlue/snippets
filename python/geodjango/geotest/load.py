from django.contrib.gis.utils import LayerMapping
from testapp.models import WorldBorder

worldborder_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'geom' : 'MULTIPOLYGON',
}
f = 'testapp/data/TM_WORLD_BORDERS-0.3.shp'

def run(verbose=True):
    lm = LayerMapping(WorldBorder, f, worldborder_mapping, transform=False, encoding='utf-8')
    lm.save(strict=True, verbose=verbose)

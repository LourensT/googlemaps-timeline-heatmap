from typing import List
import json
import sys
sys.path.append('scripts/')

from determine_range import FindRanges
from filter_to_range import FilterDataInRanges
from calculate_values_raster import FieldValue
from colors_to_raster import MapPicture

def LoadLocationData(fp : str) -> List:
    with open(fp, 'r', encoding=None) as input:
        d = json.load(input)
    coordinates = []
    for item in d['locations']:
        point = ((item['latitudeE7']/1e7), (item['longitudeE7']/1e7))
        coordinates.append(point)
    
    return coordinates

def Main():
    points = LoadLocationData('locationdata.json')
    ranges = FindRanges(points)
    data = FilterDataInRanges(points, ranges)
    fieldvalues = FieldValue(data, ranges)
    MapPicture(fieldvalues)


if __name__ == '__main__':
    Main()
#rewrite heatmap.py to work for every locationdata.json
#documentation in standardization.md

from typing import List
import json
from tkinter import Tk, PhotoImage
import numpy as np
import os

def LoadLocationData(fp : str) ->List:
    with open(fp, 'r', encoding=None) as input:
        d = json.load(input)
    coordinates = []
    for item in d['locations']:
        point = ((item['latitudeE7']/1e7), (item['longitudeE7']/1e7))
        coordinates.append(point)
    
    return coordinates

def FindRanges(data, range_start=25, range_end=75):
    latitudes = []
    longitudes = []
    for item in data:
        latitudes.append(item[0])
        longitudes.append(item[1])
    
    #find quartiles 
    quartiles_latitude = np.percentile(latitudes, [range_start, 50, range_end])
    quartiles_longitude = np.percentile(longitudes, [range_start, 50, range_end])

    #square boundaries
    if (quartiles_latitude[2]-quartiles_latitude[0]) > (quartiles_longitude[2]-quartiles_longitude[0]):
        lowerboundary_latitude = quartiles_latitude[0]
        upperboundary_latitude = quartiles_latitude[2]
        lowerboundary_longitude = (quartiles_longitude[1] - ((quartiles_latitude[2]-quartiles_latitude[0])/2))
        upperboundary_longitude = (quartiles_longitude[1] + ((quartiles_latitude[2]-quartiles_latitude[0])/2))
    
    return lowerboundary_latitude, upperboundary_latitude, lowerboundary_longitude, upperboundary_longitude

def FilterDataInRanges(data, ranges):
    filtered_data = []
    for item in data:
        if ((item[0] > ranges[0]) and (item[0] < ranges[1])) and ((item[1] > ranges[2]) and (item[1] < ranges[3])):
            filtered_data.append(item)

    return filtered_data

def FieldValue(data, ranges, raster=(1000,1000)):
    pixel_frequency = {}

    for item in data:
        y = int(((item[0]-ranges[0]) / (ranges[1]-ranges[0])) * raster[1] )
        x = int(((item[1]-ranges[2]) / (ranges[3]-ranges[2])) * raster[0] )
        if (x,y) not in pixel_frequency:
            pixel_frequency[(x,y)] = 1
        else:
            pixel_frequency[(x,y)] += 1
    
    return pixel_frequency

def MapPicture(pixel_frequency, raster=(1000,1000)):
    root = Tk()
    img = PhotoImage(width=raster[0], height=raster[1])

    for i in range(1, raster[0]):
        x = i
        for j in range(1, raster[0]):
            y = j
            img.put('#000000', (x,y))

    pixel_values = []
    for item in pixel_frequency.values():
        pixel_values.append(item)
    freqstats = np.percentile(pixel_values, [25, 50, 75])

    for coordinate in pixel_frequency:
        color = GetColor(pixel_frequency[coordinate], freqstats)
        img.put(color, coordinate)

    filename = 'heat.png'
    img.write(filename, format='png')


def GetColor(value, percentiles):
    if float(value) < percentiles[0]:
        return '#ffffff'
    elif float(value) < percentiles[1]:
        return '#3383FF'
    elif float(value) < percentiles[2]:
        return '#FF3333'
    else:
        return '#F3FF00'

def Main():
    points = LoadLocationData('locationdata.json')
    ranges = FindRanges(points)
    data = FilterDataInRanges(points, ranges)
    fieldvalues = FieldValue(data, ranges)
    MapPicture(fieldvalues)


if __name__ == '__main__':
    Main()
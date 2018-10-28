#rewrite heatmap.py to work for every locationdata.json
#documentation in standardization.md

from typing import List
import json
import matplotlib.pyplot as plt
from tkinter import Tk, Canvas, PhotoImage, mainloop
from scipy import stats
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


def GetColor(value, source):
    percentiles = np.percentile(source, [25, 50, 75])
    if percentiles[0] == percentiles[1]:
        new_source = []
        for item in source:
            if item != int(percentiles[0]):
                new_source.append(item)
        percentiles = np.percentile(new_source, [25, 50, 75])

    if float(value) < percentiles[0]:
        return '#ffffff'
    elif float(value) < percentiles[1]:
        return '#3383FF'
    elif float(value) < percentiles[2]:
        return '#FF3333'
    else:
        return '#F3FF00'

points = LoadLocationData('locationdata.json')
ranges = FindRanges(points)
new_data = FilterDataInRanges(points, ranges)
print(len(points))
print(len(new_data))
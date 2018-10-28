import json
import matplotlib.pyplot as plt
from tkinter import Tk, Canvas, PhotoImage, mainloop
from scipy import stats
import numpy as np
import os

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

with open('locationdata.json', 'r', encoding=None) as input:
    d = json.load(input)

#print(type(d['locations'][0]['latitudeE7']))

latitude = []
longitude = []
timestamps = []
pixel_coordinates = []
pixel_frequency = []
latitude_raw = []
longitude_raw = []

#write functions to automate this!!
latitude_nul = 0
latitude_height = 0.05 
longitude_nul = 0
longitude_width = 0.05

for item in d['locations']:
    if ((item['latitudeE7'] != 0) or (item['longitudeE7'] != 0)):
        if (((item['latitudeE7'] / 1e7) < latitude_nul) and ((item['latitudeE7'] / 1e7) > (latitude_nul - latitude_height))):
            if (((item['longitudeE7'] / 1e7) > longitude_nul) and ((item['longitudeE7'] / 1e7) < (longitude_nul + longitude_width))):
                latitude_raw.append((item['latitudeE7'] / 1e7))
                longitude_raw.append((item['longitudeE7'] / 1e7))
                timestamps.append(item['timestampMs'])

print(len(timestamps))

latitude_0 = min(latitude_raw)
longitude_0 = min(longitude_raw) 
print(latitude_0, longitude_0)

for item in latitude_raw:
    latitude.append(item - latitude_0 )

for item in longitude_raw:
    longitude.append(item - longitude_0 )

WIDTH, HEIGHT = 1000, 1000

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000001")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

for i in range(1, 1000):
    x = i
    for j in range(1, 1000):
        y = j
        img.put('#000000', (x,y))

count = 0

for i in range(len(longitude)):
    y = int((latitude[i] / latitude_height) * HEIGHT )
    x = int((longitude[i] / longitude_width) * WIDTH )
    if (x,y) not in pixel_coordinates:
        img.put("#ffffff", (x, y))
        pixel_coordinates.append((x,y))
        pixel_frequency.append(1)
        #filename = 'files\\' + str(count) + '.png'
        #img.write(filename, format='png')
        #count += 1
    else:
        pixel_frequency[pixel_coordinates.index((x,y))] += 1

filename = '1.png'
img.write(filename, format='png')

#frequency_range = max(pixel_frequency) - min(pixel_frequency)
for i in range(len(pixel_coordinates)):
    color = GetColor(pixel_frequency[i], pixel_frequency)
    img.put(color, pixel_coordinates[i])


filename = 'heat4.png'
img.write(filename, format='png')

mainloop()


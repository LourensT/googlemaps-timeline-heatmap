from getcolor import GetColor
from tkinter import Tk, PhotoImage
import numpy as np

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

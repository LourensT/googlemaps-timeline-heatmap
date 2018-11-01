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
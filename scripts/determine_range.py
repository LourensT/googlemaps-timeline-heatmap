import numpy as np

def FindRanges(data, range_start=10, range_end=90, square=True):
    latitudes = []
    longitudes = []
    for item in data:
        latitudes.append(item[0])
        longitudes.append(item[1])
    
    #find quartiles 
    quartiles_latitude = np.percentile(latitudes, [range_start, 50, range_end])
    quartiles_longitude = np.percentile(longitudes, [range_start, 50, range_end])

    

    #square boundaries
    if square:
        if (quartiles_latitude[2]-quartiles_latitude[0]) > (quartiles_longitude[2]-quartiles_longitude[0]):
            lowerboundary_latitude = quartiles_latitude[0]
            upperboundary_latitude = quartiles_latitude[2]
            lowerboundary_longitude = (quartiles_longitude[1] - ((quartiles_latitude[2]-quartiles_latitude[0])/2))
            upperboundary_longitude = (quartiles_longitude[1] + ((quartiles_latitude[2]-quartiles_latitude[0])/2))
        else:
            lowerboundary_longitude = quartiles_longitude[0]
            upperboundary_longitude = quartiles_longitude[2]
            lowerboundary_latitude = (quartiles_latitude[1] - ((quartiles_longitude[2]-quartiles_longitude[0])/2))
            upperboundary_latitude = (quartiles_latitude[1] + ((quartiles_longitude[2]-quartiles_longitude[0])/2))
    else:
        lowerboundary_longitude = quartiles_longitude[0]
        upperboundary_longitude = quartiles_longitude[2]
        lowerboundary_latitude = quartiles_latitude[0]
        upperboundary_latitude = quartiles_latitude[2]
    
    print('Latitude: lowerboundary=%s, upperboundary=%s' % (lowerboundary_latitude, upperboundary_latitude))
    print('Longitude: lowerboundary=%s, upperboundary=%s' % (lowerboundary_longitude, upperboundary_longitude))

    return lowerboundary_latitude, upperboundary_latitude, lowerboundary_longitude, upperboundary_longitude
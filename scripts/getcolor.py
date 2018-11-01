def GetColor(value, percentiles):
    if float(value) < percentiles[0]:
        return '#ffffff'
    elif float(value) < percentiles[1]:
        return '#3383FF'
    elif float(value) < percentiles[2]:
        return '#FF3333'
    else:
        return '#F3FF00'
def FilterDataInRanges(data, ranges):
    filtered_data = []
    for item in data:
        if ((item[0] > ranges[0]) and (item[0] < ranges[1])) and ((item[1] > ranges[2]) and (item[1] < ranges[3])):
            filtered_data.append(item)

    return filtered_data
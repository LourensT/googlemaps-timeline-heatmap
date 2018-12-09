import csv
import requests
import time

all_addresses= []
with open('bezorg.csv', 'r', encoding='utf-8') as input:
    for row in csv.reader(input):
        geocode = str(row[0]) + ', ' + str(row[2]) + ', ' + str(row[1])
        all_addresses.append(geocode)
''' 
for item in all_addresses:
#parameters = {'key' : '333e3da05885f2' , 'q' : item , 'format': 'json'}
#response = requests.get('https://eu1.locationiq.com/v1/search', params=parameters)
    url = 'https://eu1.locationiq.com/v1/search.php?key=333e3da05885f2&q=' + item + '&format=json'
    response = requests.get(url)
'''


geopoints = []

for item in all_addresses:
    url = 'https://eu1.locationiq.com/v1/search.php?key=333e3da05885f2&q=' + item + '&format=json'
    response = requests.get(url)
    point = {}
    try:
        point["latitudeE7"] = int(float(response.json()[0]['lat']) * (10**7))
        point["longitudeE7"] = int(float(response.json()[0]['lon']) * (10**7))
        print(point)
        geopoints.append(point)
        print(item + 'done')
        time.sleep(1.5)
    except KeyError:
        print(response.text)
        break


final_export = {"locations" : geopoints}

with open('bezorg.json', 'w') as output:
    output.write(str(final_export))
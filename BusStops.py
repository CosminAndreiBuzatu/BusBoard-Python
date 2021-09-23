from key import *
import requests
from Constants import *


class BusStops:

    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    def getBusStations(self):
        r = requests.get(f'https://transportapi.com/v3/uk/places.json?app_id={appId}&app_key={key}&lat={self.latitude}&lon={self.longitude}')
        response = r.json()
        return response


    def getTwoNearestBusStops(self):
        busStations = self.getBusStations()
        busStops = busStations['member']
        count = 0
        count1= 0
        atcocode = []
        for busStop in busStops:
            if count < 2 and busStop['type'] == 'bus_stop':
                count1 += 1
                if count1 == 1:
                    FirstStop.append({'StopName' : busStop['name'], 'Distance' : busStop['distance']})
                    count += 1
                    atcocode.append(busStop['atcocode'])
                if count1 == 2:
                    SecondStop.append({'StopName' : busStop['name'], 'Distance' : busStop['distance']})
                    count += 1
                    atcocode.append(busStop['atcocode'])

        return atcocode


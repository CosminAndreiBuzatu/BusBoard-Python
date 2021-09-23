from key import *
import requests
from Constants import *


class BusesInfo:

    def __init__(self, atcocodes):
        self.atcocodes = atcocodes

    def getInfoBusStation(self):
        actocode = []
        for busStopSerial in self.atcocodes:
            r = requests.get(f'https://transportapi.com/v3/uk/bus/stop/{busStopSerial}/live.json?app_id={appId}&app_key={key}&group=no')
            response = r.json()
            actocode.append(response)
        return actocode

    def getDepartureBusesInfo(self):
        busStops = self.getInfoBusStation()
        count1 = 0
        for buses in busStops:
            departures = buses['departures']['all']
            count = 0
            for busNumber in departures:
                if count1 == 0:
                    if busNumber['aimed_departure_time'] == None and count < 5:
                        FirstUnsortedBusesInfo.append({'Bus' : busNumber['line'] , 'Direction' : busNumber['direction'], 'Time' : 'Unknown'})
                        count += 1
                    if count < 5:
                        FirstUnsortedBusesInfo.append({'Bus' : busNumber['line'] , 'Direction' : busNumber['direction'], 'Time' : busNumber['aimed_departure_time']})
                        count += 1
                if count1 == 1:
                    if busNumber['aimed_departure_time'] == None and count < 5:
                        SecondUnsortedBusesInfo.append({'Bus' : busNumber['line'] , 'Direction' : busNumber['direction'], 'Time' : 'Unknown'})
                        count += 1
                    if count < 5:
                        SecondUnsortedBusesInfo.append({'Bus' : busNumber['line'] , 'Direction' : busNumber['direction'], 'Time' : busNumber['aimed_departure_time']})
                        count += 1
            count1 += 1
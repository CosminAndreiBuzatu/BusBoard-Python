import requests
from key import *

printStatements = []


class PostCode:


    def __init__(self, postcode):
        self.postcode = postcode

    def getPostcodeInfo(self):
        r = requests.get(f'https://api.postcodes.io/postcodes/{self.postcode}')
        response = r.json()
        return response

    def getCoordonate(self):
        r = self.getPostcodeInfo()
        longitude = r['result']['longitude']

        latitude = r['result']['latitude']
        return longitude, latitude


class BusStop:


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
        atcocode = []
        for busStop in busStops:
            if count < 2 and busStop['type'] == 'bus_stop':
                printStatements.append('Bus stop "' + busStop['name'] + '" the distance from your postcode to the bus - ' + str(busStop['distance']))
                count += 1
                atcocode.append(busStop['atcocode'])
        return atcocode


    def getInfoBusStation(self):
        actocodes = []
        busStopSerials = self.getTwoNearestBusStops()
        for busStopSerial in busStopSerials:
            r = requests.get(f'https://transportapi.com/v3/uk/bus/stop/{busStopSerial}/live.json?app_id={appId}&app_key={key}&group=no')
            response = r.json()
            actocodes.append(response)
        return actocodes


    def getDepartureBusesInfo(self):
        busStops = self.getInfoBusStation()
        for buses in busStops:
            departures = buses['departures']['all']
            count = 0
            for busNumber in departures:
                if busNumber['aimed_departure_time'] == None and count < 5:
                    printStatements.append('Bus number ' + busNumber['line'] + ' from ' + busNumber['direction'] + ' expected to arrive Uknown')
                if count < 5:
                    printStatements.append('Bus number ' + busNumber['line'] + ' from ' + busNumber['direction'] + ' expected to arrive ' + busNumber['aimed_departure_time'])
                count += 1
        return printStatements


class Display:


    def __init__(self, data):
        self.data = data


    def display(self):
        print(self.data[0] + ' \n\n The next 5 buses at this station are:  \n\n' + self.data[2] + '\n' + self.data[3] + '\n' + self.data[4] + '\n' + self.data[5] + '\n' + self.data[6] + ' \n')
        print(self.data[1] + ' \n\n The next 5 buses at this station are:  \n\n' + self.data[7] + '\n' + self.data[8] + '\n' + self.data[9] + '\n' + self.data[10] + '\n' + self.data[11])


def main():

    inputPostcode = input('Type a postcode: ')

    postcode1 = PostCode(inputPostcode)

    lat , lon = postcode1.getCoordonate()

    postcodeBuses = BusStop(lat , lon)

    data = postcodeBuses.getDepartureBusesInfo()

    display1 = Display(data)

    display1.display()


if __name__ == "__main__":
    main()
import requests
from key import *
printStatements =[]
def getInfoBusStation(atcoCode):
    actocodes = []
    for atco in atcoCode:
        r = requests.get(f'https://transportapi.com/v3/uk/bus/stop/{atco}/live.json?app_id={appId}&app_key={key}&group=no&limit=5&nextbuses=yes')
        response = r.json()
        actocodes.append(response)
    return actocodes


def departureBusesInfo(responseApi):
    for busStops in responseApi:
        departures = busStops['departures']['all']
        count = 0
        for busNumber in departures:
            if busNumber['aimed_departure_time'] == None and count < 5:
                printStatements.append('Bus number ' + busNumber['line'] + ' from ' + busNumber['direction'] + ' expected to arrive Uknown')
            if count < 5:
                printStatements.append('Bus number ' + busNumber['line'] + ' from ' + busNumber['direction'] + ' expected to arrive ' + busNumber['aimed_departure_time'])
            count +=1

def getPostcodeInfo(postcode):
    r = requests.get(f'https://api.postcodes.io/postcodes/{postcode}')
    response = r.json()
    return response


def coordonateInfo(responseApi):
    longitude = responseApi['result']['longitude']
    latitude = responseApi['result']['latitude']
    return longitude,latitude


def getNearBusStations(coord):
    r = requests.get(f'https://transportapi.com/v3/uk/places.json?app_id={appId}&app_key={key}&lat={coord[1]}&lon={coord[0]}')
    response = r.json()
    return response


def twoNearestBusStops(responseApi):
    count = 0
    atcocode = []
    busStops = responseApi['member']
    for bus in busStops:
        if count < 2 and bus['type'] == 'bus_stop':
            printStatements.append('Bus stop "' + bus['name'] + '" the distance from your postcode to the bus - ' + str(bus['distance']))
            count += 1
            atcocode.append(bus['atcocode'])
    return atcocode


def dispay(y):
            print(y[0] + ' \n The next 5 buses at this station are:  \n' + y[2] + '\n' + y[3] + '\n' + y[4] + '\n' + y[5] + '\n' + y[6]+ ' \n')
            print(y[1] + ' \n The next 5 buses at this station are:  \n' + y[7] + '\n' + y[8] + '\n' + y[9] + '\n' + y[10] + '\n' + y[11])


def main():
    postcode = input('Type a postcode: ')
    postApi = getPostcodeInfo(postcode)
    coord = coordonateInfo(postApi)
    x = getNearBusStations(coord)
    atcoCodes = twoNearestBusStops(x)
    y =getInfoBusStation(atcoCodes)
    departureBusesInfo(y)
    dispay(printStatements)


if __name__ == "__main__":
    main()

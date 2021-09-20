import requests
from constants import *

def getInfoBusStation(atcoCode):
    r = requests.get(f'https://transportapi.com/v3/uk/bus/stop/{atcoCode}/live.json?app_id={appId}&app_key={key}&group=no&limit=5&nextbuses=yes')
    response = r.json()
    return response
def departureBusesInfo(responseApi):
    departures = responseApi['departures']['all']
    for busNumber in departures:
        print('Bus number ' +busNumber['line'] + ' from ' + busNumber['direction'] + ' expected to arrive ' + busNumber['expected']['arrival']['time'])
def main():
    busStop = input('Type a bus stop code: ')
    apiResponse = getInfoBusStation(busStop)
    departureBusesInfo(apiResponse)
if __name__ == "__main__":
    main()

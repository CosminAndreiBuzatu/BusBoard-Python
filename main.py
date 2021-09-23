from Constants import *
from PostCode import PostCode
from BusStops import BusStops
from BusesInfo import BusesInfo
from Display import Display

def main():

    inputPostcode = input('Type postcode: ')

    postcode1 = PostCode(inputPostcode)

    lat , lon = postcode1.getCoordonate()

    postcodeBuses = BusStops(lat , lon)

    atcoCodes = postcodeBuses.getTwoNearestBusStops()

    busesInfo = BusesInfo(atcoCodes)

    busesInfo.getDepartureBusesInfo()

    FirstBusesInfo = sorted(FirstUnsortedBusesInfo, key=lambda k: k['Time'])

    SecondBusesInfo = sorted(SecondUnsortedBusesInfo, key=lambda k: k['Time'])

    display1 = Display(FirstStop,FirstBusesInfo)

    display2 = Display(SecondStop, SecondBusesInfo)

    display1.display('StopName','Distance','Bus', 'Direction', 'Time')

    display2.display('StopName','Distance','Bus', 'Direction', 'Time')

if __name__ == "__main__":
    main()
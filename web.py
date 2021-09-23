from flask import Flask, render_template, request
from main import *
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/busInfo")
def busInfo():
    postcode = request.args.get('postcode')
    postcode1 = PostCode(postcode)

    lat, lon = postcode1.getCoordonate()

    postcodeBuses = BusStops(lat, lon)

    atcoCodes = postcodeBuses.getTwoNearestBusStops()
    busesInfo = BusesInfo(atcoCodes)
    busesInfo.getDepartureBusesInfo()
    FirstBusesInfo = sorted(FirstUnsortedBusesInfo, key=lambda k: k['Time'])
    SecondBusesInfo = sorted(SecondUnsortedBusesInfo, key=lambda k: k['Time'])
    display1 = Display(FirstStop, FirstBusesInfo)
    display2 = Display(SecondStop, SecondBusesInfo)
    display1.displayWeb('StopName', 'Distance', 'Bus', 'Direction', 'Time')
    display2.displayWeb('StopName', 'Distance', 'Bus', 'Direction', 'Time')

    return render_template('info.html',postcode = postcode, web = web)

if __name__ == "__main__": app.run()
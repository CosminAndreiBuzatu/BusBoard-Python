from Constants import *

class Display:

    def __init__(self, busStops, busesInfo):
          self.busStops = busStops
          self.busesInfo = busesInfo

    def display(self,stop,distance,bus,direction,time):
        print('\nBus stop : ' + self.busStops[0][stop] + ' is at a distance of ' + str(self.busStops[0][distance]) + ' meters\n')
        for busInfo in self.busesInfo:
            print('Bus number : ' + busInfo[bus] + ' from ' + busInfo[direction] + ' expected to arrive at ' + busInfo[time])

    def displayWeb(self,stop,distance,bus,direction,time):
        web.append('<strong>Bus stop : ' + self.busStops[0][stop] + ' is at a distance of ' + str(self.busStops[0][distance]) + ' meters</strong>')
        for busInfo in self.busesInfo:
            web.append('Bus number : ' + busInfo[bus] + ' from ' + busInfo[direction] + ' expected to arrive at ' + busInfo[time])

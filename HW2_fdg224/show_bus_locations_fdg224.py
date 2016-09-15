#libraries
import os
import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

#functions
def getBusList(parsedMTAapi):
    ''' This function takes a parsed input as given by the MTA API for a single busline
    and returns a list of buses, where every element of a list is the VehicleActivity 
    of the bus'''
    return parsedMTAapi['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

def busLocation(bus,coordinate):
    '''This function takes the VehicleActivity of a bus (in dictionary format) and returns
    its latitude of longitude'''
    return bus['MonitoredVehicleJourney']['VehicleLocation'][coordinate]


#set arguments
mta_key = sys.argv[1]
bus_line = sys.argv[2]

#download data

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + mta_key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line 
response = urllib.urlopen(url)
rawData = response.read().decode("utf-8")
parseData = json.loads(rawData)

#create a list of buses 
busesList = getBusList(parseData)
amountOfBuses = len(busesList)

#print results
print 'Bus Line : %s' % bus_line
print 'Number of Active Buses : %d' % amountOfBuses
for busID in range(amountOfBuses):
    lat = busLocation(busesList[busID],'Latitude')
    longi =  busLocation(busesList[busID],'Longitude')
    print 'Bus %d is at latitude %2.6f and longitude %2.6f' %(busID,lat,longi)
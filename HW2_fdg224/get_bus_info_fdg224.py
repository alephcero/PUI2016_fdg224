#libraries
import os
import sys
import json
import csv

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

def busStopName(bus):
    '''This function takes a VehicleActivity of a bus (in dictionary format) and returns
    its stop name '''
    return bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    
def busStopStatus(bus):
    '''This function takes a VehicleActivity of a bus (in dictionary format) and returns
    its stop status'''
    return bus['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']


#set arguments
mta_key = sys.argv[1]
bus_line = sys.argv[2]
file = sys.argv[3]


#download data

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + mta_key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + bus_line 
response = urllib.urlopen(url)
rawData = response.read().decode("utf-8")
parseData = json.loads(rawData)

#create a list of buses 
busesList = getBusList(parseData)


#write to csv
#source: https://docs.python.org/2/library/csv.html
with open(file, 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Latitude','Longitude','Stop Name','Stop Status'])
    busID = 0
    '''
    lat = busLocation(busesList[busID],'Latitude')
    longi =  busLocation(busesList[busID],'Longitude')
    stopName = busStopName(busesList[busID])
    stopStatus = busStopStatus(busesList[busID])
    filewriter.writerow([lat,longi,stopName,stopStatus])


    '''
    while busID < len(busesList):
         lat = busLocation(busesList[busID],'Latitude')
         longi =  busLocation(busesList[busID],'Longitude')
         stopName = busStopName(busesList[busID])
         stopStatus = busStopStatus(busesList[busID])
         filewriter.writerow([lat,longi,stopName,stopStatus])
         busID += 1

    


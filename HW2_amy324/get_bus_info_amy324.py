# Author: Adriano M. Yoshino - amy324@nyu.edu

# Importing API code extracted by Dr. Bianco notebooks for PUI_2016 class
# Import data by API

from __future__ import print_function
import pylab as pl
import json
import urllib.request as ulr
import sys


if not len(sys.argv) == 4:
    print("Invalid number of arguments. Run as: python  get_bus_info_amy324.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()

# Bringing the information from MTA API and reading JSON file
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] \
    + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]
response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# Start writing .csv file named as argument 3 given by user
fout = open(sys.argv[3], "w")
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

# view quantity of buses runing at the time
n_buses = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

# Writing all information on created .csv file
for n in (range(0, n_buses)):
    line_lat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n] \
               ['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    line_lon = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n] \
               ['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    bus_stop = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n] \
              ['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    bus_status = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n]  \
                ['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances'] \
                ['PresentableDistance']

    #print ("Lat: %s, Lon: %s, Bus Stop: %s, Bus Status: %s" %(line_lat, line_lon, bus_stop, bus_status))

    fout.write("%s,%s,%s,%s\n" %(line_lat, line_lon, bus_stop, bus_status))

fout.close()

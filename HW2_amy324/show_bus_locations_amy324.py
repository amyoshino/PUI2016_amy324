# Author: Adriano M. Yoshino - amy324@nyu.edu

# Importing API code extracted by Dr. Bianco notebooks for PUI_2016 class
# Import data by API

from __future__ import print_function
import pylab as pl
import json
import urllib.request as ulr
import sys


if not len(sys.argv) == 3:
    print("Invalid number of arguments. Run as: python  show_bus_locations_amy324.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

# Bringing the information from MTA API and reading JSON file
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] \
    + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# Printing needed information
line = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['PublishedLineName']
n_buses = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

print ("Bus Line :", line)
print ("Number of Active Buses:", n_buses)

for n in (range(0, n_buses)):
    line_lat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n] \
               ['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    line_lon = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][n] \
               ['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print ("Bus %d is at latitude %s and longitude %s" %(n+1, line_lat, line_lon))

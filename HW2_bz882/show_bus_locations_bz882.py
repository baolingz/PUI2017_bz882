
# coding: utf-8

# In[2]:

import pylab as pl
import os
import json
import sys

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib 

pl.rc('font', size=15)

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + \
    sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


# In[64]:

BusLine = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['PublishedLineName']


# In[65]:

#print ('Bus Line : ' + BusLine)


# In[53]:

BusLoc = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']


# In[79]:

BusActivity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']


# In[78]:

print ('Bus Line : ' + BusLine)
print ('Number of Active Buses : ' + str(len(BusActivity)))
for i in range(len(BusActivity)):
    print ('Bus ' + str(i) +' is at latitude ' + str(BusActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']) + ' and longitude ' + str(BusActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])) 


# In[ ]:




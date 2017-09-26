
# coding: utf-8

# In[48]:

import pylab as pl
import os
import json
import sys
fout = open(sys.argv[3], "w")

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
    
pl.rc('font', size=15)

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]
#url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key" + "=763171d0-05d4-4baa-9e6e-2f2e707b759f&VehicleMonitoringDetailLevel=calls&LineRef=" + "B52"

print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


# In[49]:

BusActivity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']


# In[50]:

#40.755489,-73.987347,7 AV/W 41 ST,at stop
print ("Latitude,Longitude,Stop Name,Stop Status")
for i in range(len(BusActivity)):
    Latitude = str(BusActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    Longitude = str(BusActivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    if bool(BusActivity[i]['MonitoredVehicleJourney']['OnwardCalls']):
        StopName = BusActivity[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        Status = BusActivity[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
        print (Latitude + ',' + Longitude + ',' + StopName + ',' + Status)
        fout.write(Latitude + ',' + Longitude + ',' + StopName + ',' + Status + '\n')
    print (Latitude + ',' + Longitude + ',N/A,N/A')
    fout.write(Latitude + ',' + Longitude + ',N/A,N/A\n')


# In[ ]:




import requests 
from request import makeRequest
from dbConections import getCoordinates, getAPIKey

a = getCoordinates('CASA')
b = getCoordinates('UNIVERSIDAD ANAHUAC')

lat_ori = str(a[0])
lon_ori = str(a[1])
lat_des = str(b[0])
lon_des = str(b[1])

apiKey = getAPIKey()

theUrl = 'https://router.hereapi.com/v8/routes?origin=' + lat_ori + ',' + lon_ori + '&destination=' + lat_des + ',' + lon_des + '&return=summary,typicalDuration&transportMode=car&apikey=' + apiKey

r = requests.get(theUrl)
print(r.text)
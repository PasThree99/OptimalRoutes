from db import getAllPlaces, getCoordinates
from request import makeRequest




ori = 'CASA'
des = 'UNIVERSIDAD ANAHUAC'

print(makeRequest(getCoordinates(ori),getCoordinates(des)))
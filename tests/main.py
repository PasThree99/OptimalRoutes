from db import getAllPlaces, getCoordinates
from request import makeRequest


a = getAllPlaces()
print(a[-5:])

ori = 'CASA'
des = 'LA ASUNCION SEDENA'

print(makeRequest(getCoordinates(ori),getCoordinates(des))/60)
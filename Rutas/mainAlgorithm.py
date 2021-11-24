import requests
from Rutas.dbConections import getOrigin
from Rutas.dbConections import getCoordinates, getOrigin
from Rutas.request import makeRequest
from itertools import permutations

req = 0

def keyForRoute(a,b):
    l = [a,b]
    l.sort()
    s = l[0] + l[1]
    return s


def distancia(lugares,origin,dic):
    global req
    ua = origin
    distTotal = 0
    for su in lugares:
        if ((keyForRoute(ua,su) in dic) == False):
            d = makeRequest(getCoordinates(ua),getCoordinates(su))
            req +=1
            print('request')
            dic[keyForRoute(ua,su)] = d   

        distTotal += dic[keyForRoute(ua,su)]  
        ua = su
    
    if(not(keyForRoute(ua,origin) in dic)):
        d = makeRequest(getCoordinates(ua),getCoordinates(origin))
        req += 1
        print('request')
        dic[keyForRoute(ua,origin)] = d
    
    distTotal += dic[keyForRoute(ua,origin)]


    return (distTotal,dic)

                      
def calcularRuta(lugares): 
    origin = getOrigin()
    per = list(permutations(lugares))
    
    tiempoMinimo = 100000000
    ordenFinal = []
    dic =  {}
    for ordenActual in per:
        res = distancia(ordenActual,origin,dic)
        dic = res[1]
        if(res[0] < tiempoMinimo):
            tiempoMinimo = res[0]
            ordenFinal.append(ordenActual)
        
    st = origin + ' -> '
    for i in ordenFinal[-1]:
        st += i
        st += ' -> '
    
    st += origin

    print(req)
    tiempoMinimo *= 1.15

    return (tiempoMinimo,st)

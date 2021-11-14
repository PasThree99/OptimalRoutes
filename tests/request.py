import requests 

def extractTime(st):
    param = "duration"
    result = st.find(param)
    result = result + len(param) + 2
    end = result + 1
    while(st[end] != ","):
        end +=1 
    
    return st[result:end]

def makeRequest(origin, destination):
    
    lat_ori = str(origin[0])
    lon_ori = str(origin[1])
    lat_des = str(destination[0])
    lon_des = str(destination[1])

    apiKey = 'wzt7BjBZhuafsjAM4wAl7G5tQqAHlPcCRwacvMHIY5U'

    theUrl = 'https://router.hereapi.com/v8/routes?origin=' + lat_ori + ',' + lon_ori + '&destination=' + lat_des + ',' + lon_des + '&return=summary,typicalDuration&transportMode=car&apikey=' + apiKey

    r = requests.get(theUrl)
    return float(extractTime(r.text))
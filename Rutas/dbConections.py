import mysql.connector

def getAllPlaces():
    # Returns a list of the names of all the registered places. Each name is a string in CAPS
    conn = mysql.connector.connect(user='root', password='12345678', host='127.0.0.1', database='rutas2')
    cur = conn.cursor()
    cur.execute("Select nombre From places",[])
    r = cur.fetchall()
    l = []
    for i in r:
        l.append(i[0])
    conn.close()
    print(l[-1])
    #l.sort() #opcional
    return l

def getAPIKey():
    # Returns the updated API key value in a string
    conn = mysql.connector.connect(user='root', password='12345678', host='127.0.0.1', database='rutas2')
    cur = conn.cursor()
    cur.execute("Select api_key From APIKey where id=%s",[1])
    r = cur.fetchall()
    conn.close()
    return r[0][0]

def getCoordinates(place):
    # Retunrs the coordinates of the given Place. If the place is not registeres returns None
    conn = mysql.connector.connect(user='root', password='12345678', host='127.0.0.1', database='rutas2')
    cur = conn.cursor()
    cur.execute("Select latitud, longitud From places where nombre = %s",[place])
    r = cur.fetchall()
    if(len(r) < 1):
        print("No se encontro el lugar: " + place + "\nRevisa que este bien escrito")
        conn.close()
        return None
    t = [float(r[0][0]), float(r[0][1])]
    #print(t)
    conn.close()
    return t

def getOrigin():
    conn = mysql.connector.connect(user='root', password='12345678', host='127.0.0.1', database='rutas2')
    cur = conn.cursor()
    cur.execute('select nombre from places where origen=true')
    r = cur.fetchall()
    conn.close()
    return r[0][0]

def insertNewLocation(name,lat,lon):
    conn = mysql.connector.connect(user='root', password='12345678', host='127.0.0.1', database='rutas2')
    cur = conn.cursor()
    cur.execute('insert into places (nombre,latitud,longitud) values (%s,%s,%s)',[name,lat,lon])
    conn.commit()
    conn.close()

def updateOrigin(newOrigin):
    conn = mysql.connector.connect(user='root', password='12345678', host='127.0.0.1', database='rutas2')
    cur = conn.cursor()
    cur.execute('update places set origen = 0 where origen = 1 ')
    cur.execute('update places set origen = 1 where nombre = %s ',[newOrigin])
    conn.commit()
    conn.close()
    




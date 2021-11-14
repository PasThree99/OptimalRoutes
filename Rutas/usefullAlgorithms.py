def listOfTuples(l):
    r = []
    for i in l:
        r.append((i,i))
    
    return r

def deleteSlashes(l):
    r = []
    for i in l:
        if(i != '-'):
            r.append(i)
    
    return r
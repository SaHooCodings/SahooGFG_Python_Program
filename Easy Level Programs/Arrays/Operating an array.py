def searchEle(a, x):
    for e in a:
        if x==e:
            return True
    return False

def deleteEle(a, z):
    # Code here
    for e in range(len(a)):
        if(a[e]==z):
            del a[e]
            return True
    return True

def insertEle(a, y, yi):
    a.insert(yi, y)
    return True

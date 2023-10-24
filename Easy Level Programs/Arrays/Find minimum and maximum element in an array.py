def getMinMax( a, n):
    
     return [min(a),max(a)]



#orrrr
def getMinMax( a, n):
    max=a[0]
    min=a[0]
    for i in range(0,n):
        if(max<a[i]):
            max=a[i]
        if(min>a[i]):
            min=a[i]
    return min,max

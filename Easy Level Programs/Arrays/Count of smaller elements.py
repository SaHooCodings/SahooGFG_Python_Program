def countOfElements( a, n, x):
    ctr = 0 
    for i in a:
        if i > x:
            break;
        else:
            ctr+=1
    return ctr

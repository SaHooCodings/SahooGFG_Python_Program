def check_status(a, b, flag):
    ##Your code here
    if(a>0 and b>0):
        return False
    elif((a>=0 or b>=0) and flag == False):
        return True
    elif((a<=0 or b<=0) and flag == False):
        return False
    elif((a<0 and b<0) and flag == True):
        return True
    else:
        return False

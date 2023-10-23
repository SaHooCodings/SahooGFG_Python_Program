def pos(n):
    ## Write the code
    if(n==0):
        return "already Zero"
    for i in range(n):
        print(n-i-1, end = " ")
    
def neg(n):
    ##Write the code
    for i in range(-n+1):
        print(n+i, end = " ")

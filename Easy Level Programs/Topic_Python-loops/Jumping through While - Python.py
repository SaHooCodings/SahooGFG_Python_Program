def printIncreasingPower(x):
    ##Your code here
    start = 1
    jump = 1
    while(jump <= x):
        print(jump, end = " ")
        start+=1
        jump = start**2

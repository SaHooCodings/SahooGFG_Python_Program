def stringJumper(str):
    jump = 2
    for i in range(0,len(str),jump):
        print(str[i], end = "")

#Or

def stringJumper(str):
    for i in range(0,len(str),2):
        print(str[i], end = "")

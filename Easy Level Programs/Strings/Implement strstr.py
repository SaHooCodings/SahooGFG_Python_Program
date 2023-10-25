def strstr(s,x):
    #code here
    i = 0
    while i < len(s):
        if s[i] == x[0]:
            temp = i
            p = 0
            while temp < len(s) and s[temp] == x[p]:
                temp+=1
                p+=1
                if p == len(x):
                    return i
        i+=1
    return -1

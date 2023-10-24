def multiply (arr, n) :
    sum1 = 0
    s2 = 0
    if n%2 == 0:
        m = int(n/2)
        for i in range(0,m):
            sum1 += arr[i]
        for j in range(m, n):
            s2 += arr[j]
    else:
        m = int((n-1)/2)
        for i in range(0,m):
            sum1 += arr[i]
        for j in range(m, n):
            s2 += arr[j]
    return sum1*s2

def toBinary(n):
    s = ""
    while n >= 1:
        x = n%2
        n//=2
        s = str(x) + s
    print(s)

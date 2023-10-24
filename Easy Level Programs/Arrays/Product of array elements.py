def product(arr,n,mod):
    s=1
    for i in arr:
        a=i%mod 
        s=(s*a)%mod
    return s 

def missingNumber(A, N):
    sum=0    
    for i in range(N-1):  
        sum+=A[i]   
    return ((N*(N+1))//2)-sum 

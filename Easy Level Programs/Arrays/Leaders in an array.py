 def leaders(self, A, N): 
        arr=[]
        maxi=A[N-1]
        for i in range(N-1,-1,-1):
            if A[i]>=maxi:
                maxi=A[i]
                arr+=[A[i]]
        return arr[::-1]

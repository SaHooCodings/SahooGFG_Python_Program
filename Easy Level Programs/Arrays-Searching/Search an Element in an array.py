class Solution:
    def search(self,A,N,x):
        
        # check if x exists in array A
        if x in A:
            return A.index(x)
        return -1

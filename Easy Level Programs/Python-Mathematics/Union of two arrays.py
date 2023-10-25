class Solution:
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m): 
        hs=set() 
        for i in range(0,n): 
            hs.add(a[i]) 
        for i in range(0,m): 
            hs.add(b[i]) 
        return len(hs)

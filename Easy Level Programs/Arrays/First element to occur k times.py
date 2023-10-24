class Solution:
    def firstElementKTime(self,  a, n, k):
        m={}
        for i  in range(n):
            if a[i] not in m:
                m[a[i]]=0
            m[a[i]]+=1
            if m[a[i]]==k:
                return a[i]
        return -1

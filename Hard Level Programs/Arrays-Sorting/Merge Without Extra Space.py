class Solution:
    #Function to find next gap.
    def nextGap(self,gap):
        if(gap<=1):
            return 0
        return ((gap+1)//2)
    def merge(self,arr1,arr2,n,m):
        gap=n+m
        gap = self.nextGap(gap)
        while(gap>0):
            i=0
            while(i+gap<n):
                if(arr1[i]>arr1[i+gap]):
                    arr1[i],arr1[i+gap]=arr1[i+gap],arr1[i]
                i+=1
    
            j = max(0, gap - n)
            while(i<n and j<m):
                if(arr1[i]>arr2[j]):
                    arr1[i],arr2[j]=arr2[j],arr1[i]
                i+=1
                j+=1
        
            if(j<m):
                j=0
                while(j+gap < m):
                    if (arr2[j] > arr2[j + gap]):
                        arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                    j+=1
            gap = self.nextGap(gap)

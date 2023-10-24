class Solution:
    def findTriplets(self, a, n):

        a.sort()
        
        for i in range(n-2):
            
            l=i+1
            r=n-1
            
            while(l<r):
                curr_sum=a[i]+a[l]+a[r]
                
                if(curr_sum==0):
                    return 1
                elif(curr_sum<0):
                    l+=1
                else:
                    r-=1      
        return 0

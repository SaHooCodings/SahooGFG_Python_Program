class Solution:

	def getMoreAndLess(self,arr, n, x):
		# code here
        c=0
        c1=0
        for i in range(n):
            if(arr[i]>=x):
                c+=1
            if(arr[i]<=x):
                c1+=1
        return c1,c

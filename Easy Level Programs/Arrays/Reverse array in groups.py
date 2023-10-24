class Solution:	
	def reverseInGroups(self, arr, N, K):
	    i=0
	    while(i<N):
	        if (i+K<N):
	            arr[i:i+K]=reversed(arr[i:i+K])
	            i+=K
	        else:
	            arr[i:]=reversed(arr[i:])
	            i+=K

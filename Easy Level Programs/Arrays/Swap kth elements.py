class Solution:
	
	def swapKth(self,arr, n, k):
		# code here
        temp=arr[k-1]
        arr[k-1]=arr[-(k)]
        arr[-(k)]=temp

class Solution:	
	def bin_search(self, arr, left, right, key):
		if left > right:
			return -1
		mid = (left + right) // 2
		if arr[mid] == key:
			return mid
		elif arr[mid] > key:
			return self.bin_search (arr, left, mid - 1, key)
		else:
			return self.bin_search (arr, mid + 1, right, key)
	
	def binarysearch(self, arr, n, k):
		#call the recursive binary search function
		return self.bin_search(arr, 0, n-1, k)

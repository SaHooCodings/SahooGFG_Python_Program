class Solution:

	def valueEqualToIndex(self,arr, n):
		# code here
		ans = []
        for i in range(0, n):
            if i+1 == arr[i]:
                ans.append(arr[i])
        return ans

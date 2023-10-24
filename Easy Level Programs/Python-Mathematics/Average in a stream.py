class Solution:
	def streamAvg(self, arr, n):
		ans = []
		average = 0
		#iterating over the array
		for i in range(n):
			#calculating average by summing up all elements
			average += float(arr[i])
			#appending the average to the answer array
			ans.append(float(average/(i+1)))
		return ans;

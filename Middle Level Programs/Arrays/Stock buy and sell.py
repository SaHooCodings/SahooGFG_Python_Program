class Solution:
	def stockBuySell(self, A, n):
		result = []
		if(n==1):
			return result
		i=0
		cnt=0
		while(i<n-1):
			while((i<n-1) and (A[i+1]<=A[i])):
				i=i+1

			if(i==n-1):
				break
				
			e=[0,0] 
			e[0]=i
			i=i+1

			while((i<n) and A[i]>=A[i-1]):
				i=i+1
			e[1]=i-1
			
			result.append([e[0],e[1]])

			cnt=cnt+1
		if(cnt==0):
			return []
		else:
			return result

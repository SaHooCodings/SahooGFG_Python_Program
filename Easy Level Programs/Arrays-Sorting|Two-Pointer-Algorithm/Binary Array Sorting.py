class Solution:
    
    def binSort(self, A, N): 
        left = 0
        right = N-1
         
        while left < right: 
            while A[left] == 0 and left < right: 
                left += 1
            while A[right] == 1 and left < right: 
                right -= 1
            if left < right: 
                A[left] = 0
                A[right] = 1
                left += 1
                right -= 1

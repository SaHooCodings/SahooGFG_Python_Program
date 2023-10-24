class Solution:
    def minValue(self, a, b, n):
        # Sorting the arrays in ascending and descending order
        a.sort()
        b.sort(reverse=True)
        
        # Initializing the result
        res = 0
        
        # Calculating the product of corresponding elements from both arrays and summing them up
        for i in range(n):
            res += a[i] * b[i]
            
        # Returning the final result
        return res

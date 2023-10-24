class Solution:
    # Function to find the missing number in the array
    def missingNumber(self,array,n):
        total = (n + 1)*(n)//2  
        sum_of_A = sum(array) 
        return total - sum_of_A

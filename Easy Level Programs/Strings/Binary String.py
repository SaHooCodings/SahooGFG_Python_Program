class Solution:
    
    #Function to count the number of substrings that start and end with 1.
    def binarySubstring(self,n,s):
        
        #counting number of 1's in the string.
        number_of_ones=s.count('1')
        
        #returning count of possible pairs among total number of 1's.
        return ((number_of_ones*(number_of_ones-1))//2)

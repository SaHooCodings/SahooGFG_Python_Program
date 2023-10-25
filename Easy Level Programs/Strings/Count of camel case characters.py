class Solution:
    # Function to count the number of CamelCase characters in a string
    def countCamelCase (self,s):
        res = 0
        # Iterating over each character in the string
        for i in s:
            # Checking if the character is uppercase
            if i >= 'A' and i <= 'Z':
                res += 1
                
        return res

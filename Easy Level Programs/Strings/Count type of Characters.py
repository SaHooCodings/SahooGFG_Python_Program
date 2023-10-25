class Solution:
    def count (self,s):
        res = [0 for i in range (4)]
        
        for i in s:
            #Checking if the character is uppercase letter
            if i >= 'A' and i <= 'Z':
                res[0] += 1
            
            #Checking if the character is lowercase letter
            elif i >= 'a' and i <= 'z':
                res[1] += 1
            
            #Checking if the character is a digit
            elif i >= '0' and i <= '9':
                res[2] += 1
            
            #Counting other characters
            else:
                res[3] += 1
        
        return res

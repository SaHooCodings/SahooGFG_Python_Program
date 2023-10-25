class Solution:
    
    #Function to calculate sum of all numbers present in a string.
    def findSum(self,s):
        temp = "0"
        Sum = 0
      
        #iterating over the string.
        for ch in s:
      
            #if current character is digit, we store it in a temporary string.
            if (ch.isdigit()):
                temp += ch
      
            else:
                #incrementing final sum by number stored in temporary string.
                Sum += int(temp)
                #making the temporary string empty again.
                temp = "0"
      
        #adding any number if it's present in temporary
    	#string to final sum and returning it.
        return Sum + int(temp)

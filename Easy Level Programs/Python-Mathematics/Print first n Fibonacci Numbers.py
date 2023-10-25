class Solution:
    
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        
        #creating a list to store the numbers. 
        res = []
        
        #storing base values for a and b.
        a=b=1
        
        #pushing 1 once in the list if n>=1 and again if n>=2.
        if n>=1:
            res.append (1)
        if n>=2:
            res.append (1)
            
            
        for i in range(2,n):
            #pushing sum of a and b in the list.
            res.append (a+b)
            c=a+b
            #updating a as b and b as c (sum of a and b).
            a=b
            b=c
            
        #returning the list.
        return res

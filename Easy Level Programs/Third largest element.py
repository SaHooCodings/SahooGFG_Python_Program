class Solution:
    def thirdLargest(self,a, n):
        big1 = -1  #initialize the first biggest number
        big2 = -1  #initialize the second biggest number
        big3 = -1  #initialize the third biggest number
        
        for i in a:
            if i > big3:  
                big3 = i  
            
            if big3 > big2:  
                big2, big3 = big3, big2 
            
            if big2 > big1:  
                big1, big2 = big2, big1
        
        return big3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        
        #code here
        mp = {}
        for i in range(N):
            if A[i] not in mp.keys():
                mp[A[i]] = 1
            else:
                mp[A[i]] += 1
        for i in range(N):
            if B[i] not in mp.keys():
                return False
            else:
                mp[B[i]] -= 1
                
        for i in mp.keys():
            if mp[i] != 0:
                return False
        return True

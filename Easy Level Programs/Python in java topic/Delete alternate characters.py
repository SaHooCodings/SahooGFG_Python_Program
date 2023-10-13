class Solution:
    def delAlternate (ob, S):
        # code here 
        s = ""
        for i in range(0,len(S),2):
            s += S[i]
        return s

#ORR

class Solution:
    def delAlternate (ob, S):
        # code here 
        return S[::2]

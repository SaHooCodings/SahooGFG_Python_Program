class Solution:
    def findNth(self,N):
        result = 0
        p = 1
        while (N > 0):
            result += (p * (N % 9))
            N = N // 9
            p = p * 10
            
            
        return result

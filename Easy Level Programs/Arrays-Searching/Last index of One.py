class Solution:
    def lastIndex(self, s):
        n = len(s)
        if n==1:
            if s[0]=='1':
                return 0
        for i in range(n-1,-1,-1):
            if s[i]=='1':
                return i
        return -1

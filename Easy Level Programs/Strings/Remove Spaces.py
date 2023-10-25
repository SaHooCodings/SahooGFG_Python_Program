class Solution:
    def modify(self, s):
        lis=[]
        for i in range(len(s)):
            if s[i]!=" ":
                lis.append(s[i])
        return "".join(lis)

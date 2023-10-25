class Solution:
    def isIsogram(self,s):
        hash=[0]*26
        for i in range(len(s)):
            hash[ord(s[i])-ord('a')]+=1
            if hash[ord(s[i])-ord('a')]>1:
                return False
        return True

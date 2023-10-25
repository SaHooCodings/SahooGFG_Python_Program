class Solution:
    def removeVowels(self, S):
        # code here
        vow="aeiou"
        li=[]
        for i in range(0,len(S)):
            if S[i] not in vow:
                li.append(S[i])
                
        b="".join(li)
        return b

class Solution:
    def unique_substring(self,str):
        #code here
        s = set()
        for i in range (len(str)):
            for j in range(i, len(str)):
                s.add(str[i:j+1])
        return len(s)

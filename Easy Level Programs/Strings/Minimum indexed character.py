class Solution:
    def minIndexChar(self,st,patt):
        um = {}
        minIndex = sys.maxsize
      
        m = len(st)
        n = len(patt)
        for i in range (m):
            if (st[i] not in um):
                um[st[i]] = i
        for i in range(n):
            if (patt[i] in um and um[patt[i]] < minIndex):
                #updating minimum index.
                minIndex = um[patt[i]]
        if (minIndex != sys.maxsize):
            return minIndex
        else:
            return -1;

class Solution:
    def areAnagram(ob, S1, S2):
        # code here 
        if(len(S1) != len(S2)):
            return 0
        h = {}
        k = {}
        for i in S1:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        for i in S2:
            if i in k:
                k[i] += 1
            else:
                k[i] = 1
        if h==k:
            return 1
        else:
            return 0

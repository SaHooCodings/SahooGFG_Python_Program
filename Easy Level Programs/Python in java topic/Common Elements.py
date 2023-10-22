class Solution:
    def common_element(self,v1,v2):
        #code here
        d1 = dict()
        d2 = dict()
        
        for i in v1:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
                
        for i in v2:
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] += 1
                
        ans = []
        
        for i in sorted(d1):
            if i in d2:
                l = [i]*min(d1[i],d2[i])
                ans += l
                
        return ans

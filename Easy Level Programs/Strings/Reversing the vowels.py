class Solution:
    def modify(self, s):
        # code here
        a=list(s)
        vovels=set("aeiouAEIOU")
        left,right=0,len(a)-1
        while left<right:
            if a[left] not in vovels:
                left +=1
            elif a[right] not in vovels:
                right -=1
            else:
                a[left],a[right]=a[right],a[left]
                left +=1
                right -=1
        return ''.join(a) 

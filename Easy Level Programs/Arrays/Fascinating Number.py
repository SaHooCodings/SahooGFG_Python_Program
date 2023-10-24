class Solution:
def fascinating(self,n):
    # code here
    al="123456789"
    a=n*2
    b=n*3
    q= str(n)+str(a)+str(b)
    q=sorted(q)
    if q==list(al):
        return True

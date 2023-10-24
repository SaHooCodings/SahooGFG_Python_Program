class Solution:
    def findIndex (self,a, N, key ):
        #code here.
        start = -1
        for i in range(N):
            if key == a[i]:
                start = i
                break
        end = start
        for i in range(N-1,-1,-1):
            if key == a[i]:
                end = i
                break
        b = []
        b.append(start)
        b.append(end)
        return b

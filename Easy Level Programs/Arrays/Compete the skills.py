class Solution:
    def scores(self, a, b, cc):
        # Your code goes here
        for i in range(len(a)):
            if a[i] > b[i]:
                cc[0]+=1
            elif a[i] < b[i]:
                cc[1]+=1
        return cc

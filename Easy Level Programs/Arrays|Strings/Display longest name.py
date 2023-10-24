class Solution:
    def longest(self, names, n):
        n=""
        for i in names:
            if len(i)>len(n):
                n=i
        return n

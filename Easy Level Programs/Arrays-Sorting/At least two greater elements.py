class Solution:
    def findElements(self,a, n):
        # Your code goes here
        a.sort()
        return a[:n-2]

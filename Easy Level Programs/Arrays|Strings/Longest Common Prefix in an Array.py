class Solution:

    def longestCommonPrefix(self, arr, n):
        
        if n == 1 : return arr[0]
        res=""
        include=False

        for i in range(len(arr[0])):
            include=True
            for j in range(n):
                if i >= len(arr[j]) or arr[0][i]!=arr[j][i]:
                    include = False
                    break
            if include==False : break
            res+=arr[0][i]
        
        if res == "" : return "-1"
        return res

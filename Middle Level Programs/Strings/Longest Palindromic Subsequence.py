class Solution:
    #Function to find the length of the longest palindromic subsequence.
    def longestPalinSubseq(self, A):
        n = len(A)
        B = A
        B = B[::-1]
        
        #Creating a dp array with size n+1 x n+1.
        dp = []
        for i in range(n+1):
            l = [0]*(n+1)
            dp.append(l)
        
        #Filling up the dp array with the lengths of palindromic subsequences.
        for i in range(n+1):
            for j in range(n+1):
                if i==0 or j==0:
                    dp[i][j] = 0
                else:
                    if A[i-1] == B[j-1]:
                        dp[i][j] = 1+dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        #Returning the length of the longest palindromic subsequence.
        return dp[n][n]

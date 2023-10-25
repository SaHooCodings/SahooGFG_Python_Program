class Solution:
    #Function to check if A is a subsequence of B.
    def isSubSequence(self, A, B):
        i = j = 0
    
        #iterating over A and B to check if characters match.
        while i < len(B) and j < len(A):
            if A[j] == B[i]:
                j += 1
            i+=1
    
        #returning True if A is a subsequence of B, else False.
        return j == len(A)

class Solution:
    def IsPerfect(self,arr,n):
        #Complete the function
        for i in range(0,n//2):
            if arr[n-i-1] != arr[i]:
                return False
        return True

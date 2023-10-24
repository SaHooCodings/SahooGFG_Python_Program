class Solution:
    def leftElement(self, arr, n):
    # Your code goes here  
        arr.sort()
        if(n%2==0):
            even=n//2
            return(arr[even-1])
        else:
            odd=(math.ceil(n/2))
            return(arr[odd-1])

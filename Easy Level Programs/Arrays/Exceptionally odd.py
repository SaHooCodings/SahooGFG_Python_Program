class Solution:
    def getOddOccurrence(self, arr, n):
        # Initializing xor with first element of array
        xor = arr[0]
        
        # Calculating xor of all elements in array
        for i in range(1, n):
            xor ^= arr[i]
        
        # Returning xor which represents the odd occurring element
        return xor

class Solution{
    
    int Maximize(int arr[], int n)
    {
        // Complete the function
        class Solution:
    def Maximize(self, a, n): 
        
        arr.sort()
        
        mod = 1000000007
        
        s = 0
        
        for i in range(n): 
            s += arr[i] * i 
            s = s % mod
        
        return s%mod
    }   
}

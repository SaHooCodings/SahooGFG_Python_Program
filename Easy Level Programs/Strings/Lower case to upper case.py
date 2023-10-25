class Solution:
    #Function to convert string to uppercase.
    def to_upper(self, str):
        ans=''
        for i in str:
            ans+=chr(ord(i)-32) #Converting each character to uppercase by subtracting 32 from its ASCII value.
        return ans

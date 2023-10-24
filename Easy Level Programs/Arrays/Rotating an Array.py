class Solution:
    def leftRotate(self, arr, n, d):
        # code here
        for i in range(d):
            temp=arr[0]
            arr.pop(0)
            arr.append(temp)
        return arr

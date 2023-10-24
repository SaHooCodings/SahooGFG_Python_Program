class Solution:
    # Program for zig-zag conversion of array
    def zigZag(self, arr, n):
        flag = True
        for i in range(n - 1):
            # swapping elements if flag is True and current element is greater than next element
            if flag:
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            # swapping elements if flag is False and current element is smaller than next element
            else:
                if arr[i] < arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
            flag = not flag

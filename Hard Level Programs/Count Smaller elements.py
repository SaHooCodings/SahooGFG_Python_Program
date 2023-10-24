class Solution:
    def merge(self, left, right):
        i, j = 0, 0
        cnt = 0
        m, n = len(left), len(right)
        sorted_arr = []
        
        while i < m and j < n:
            if left[i][1] > right[j][1]:
                cnt += 1
                sorted_arr.append(right[j])
                j += 1
            else:
                sorted_arr.append(left[i])
                self.ans[left[i][0]] += cnt
                i += 1
        
        while i < m:
            sorted_arr.append(left[i])
            self.ans[left[i][0]] += cnt
            i += 1
        
        while j < n:
            sorted_arr.append(right[j])
            cnt += 1
            j += 1
        
        return sorted_arr
    
    def split(self, nums):
        if len(nums) == 1:
            return nums
        
        mid = (len(nums)) // 2
        
        left, right = self.split(nums[:mid]), self.split(nums[mid:])
        
        return self.merge(left, right)

    def constructLowerArray(self,arr, n):
        self.ans = [0 for _ in range(n)]
        
        nums = []
        for i, num in enumerate(arr):
            nums.append((i, num))
        
        sorted_arr = self.split(nums)
        
        return self.ans

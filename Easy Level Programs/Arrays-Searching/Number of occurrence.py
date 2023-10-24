import bisect

class Solution:
    def count(self, arr, n, x):
        # Get the index of the first occurrence of x
        low = bisect.bisect_left(arr, x)

        # If element is not present, return 0
        if low == n or arr[low] != x:
            return 0

        # Else get the index of the last occurrence of x.
        # Note that we are only looking in the subarray after the first occurrence
        high = bisect.bisect_right(arr, x, low)

        # Return count
        return high - low

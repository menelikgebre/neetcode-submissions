class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        left = 0
        for i, x in enumerate(nums):
            if left == (total - left - x):  # right sum
                return i
            left += x
        return -1
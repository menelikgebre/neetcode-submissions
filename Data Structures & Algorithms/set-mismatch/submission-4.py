class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        duplicate = missing = -1
        
        # 1. Find the duplicate by marking indices as negative
        for num in nums:
            val = abs(num)
            if nums[val - 1] < 0:
                duplicate = val  # Found the duplicate!
            else:
                nums[val - 1] *= -1
                
        # 2. Find the missing number (the index that stays positive)
        for i, num in enumerate(nums):
            if num > 0:
                missing = i + 1
                break # We can stop early here!
                
        return [duplicate, missing]
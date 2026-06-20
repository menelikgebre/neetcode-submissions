class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # max numbers for a, b and min numbers for c, d
            # always yield the best result
                # max value - min value 
        # easiest way to get these values is sort then grab top 2 bottom two
            # most efficient maybe loop through once and update along the way 
        
        sorted_nums = sorted(nums)
        return ((sorted_nums[-1] * sorted_nums[-2]) - (sorted_nums[0] * sorted_nums[1]))
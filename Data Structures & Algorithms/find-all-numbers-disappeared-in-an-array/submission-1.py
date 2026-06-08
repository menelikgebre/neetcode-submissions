class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # without extra space 
            # first thought was sort then go through
        # maybe convert nums to a set (get rid of duplicates)

        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
        
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        
        return res
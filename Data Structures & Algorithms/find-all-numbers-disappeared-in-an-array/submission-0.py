class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # nums includes values from 1 -> nums.length
            # return the missing values in nums

        check = set()
        for num in range(1, len(nums) + 1):
            check.add(num)
        
        for num in nums:
            if num in check:
                check.remove(num)
        
        return list(check)
            
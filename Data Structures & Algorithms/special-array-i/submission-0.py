class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # check array elements are all all diff parity 
            # even/odd/even/odd
        # array of len 1 is auto true, so default answer should be true 

        # dont think we need additional data structure, not referencing anything back

        # use var to check previous parity
        # use pointer to go through

        # 0 = even, 1 = odd
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i-1] % 2:
                return False
        return True
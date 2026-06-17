class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # need to know if we are checking for increasing or decreasing
            # first encounter determines that, set condition 
            # skip until we find value that sets our condition
            # then next instance != we use condition to determine

        asc, desc = False, False
        for i in range(1, len(nums)):
            # if we come across unequal values
            if nums[i] != nums[i-1]:
                # if its first encounter of this
                if not asc and not desc:
                    if nums[i] > nums[i-1]:
                        asc = True
                    if nums[i] < nums[i-1]:
                        desc = True
                # if we've already encountered asc values
                elif asc:
                    if nums[i] < nums[i - 1]:
                        return False
                # if we've already encountered desc values
                elif desc:
                    if nums[i] > nums[i - 1]:
                        return False
        return True
            
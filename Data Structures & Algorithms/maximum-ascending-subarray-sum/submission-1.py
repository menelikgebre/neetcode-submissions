class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # find max sum of ascending sub array
        #  requires window to find valid ascending sub array
            # all positive ints, but still max sum doesnt mean max len(subarray)
        
        # use stack to track curr subarray 
            # condition, add if first elem
                # add if curr elem > top of stack (prev elem)
                    # else restart stack with curr element
            # track max sum as you go 
                # always recalculate after each iteration

        stack = []
        maxSum = 0
        for i in range(len(nums)):
            if not stack:
                stack.append(nums[i])
                maxSum = max(maxSum, sum(stack))
            else:
                if nums[i] > stack[-1]:
                    stack.append(nums[i])
                    maxSum = max(maxSum, sum(stack))
                else:
                    stack = [nums[i]]
        
        return maxSum
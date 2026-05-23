class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        # prefix = [1,1,1,1,1]
        postfix = [1] * n
        # postfix = [1,1,1,1,1]

        # prefix[i] = product of nums[0..i-1]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # postfix[i] = product of nums[i+1..n-1]
        for i in range(n-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]
        
        # combine
        res = [prefix[i] * postfix[i] for i in range(n)]
        return res
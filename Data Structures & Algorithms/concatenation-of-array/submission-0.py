class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # concat array within itself 
        # always len >= 1, 0 indexed 

        length = len(nums)
        ans = [0] * (2*length)

        for i, num in enumerate(nums):
            ans[i] = num
            ans[i + length] = num
        
        return ans
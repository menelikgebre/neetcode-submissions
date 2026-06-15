class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # two ways to approach
            # sort the array first and store in sep
            # zip through arrays and where i does not equal each other, add to res
        
        res = 0
        sort_h = sorted(heights)

        for i, j in zip(heights, sort_h):
            if i != j:
                res += 1
        
        return res 
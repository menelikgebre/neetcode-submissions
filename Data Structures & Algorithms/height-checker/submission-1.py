class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # better option with O(1) memory 
        # look at each value
            # check against max seen
            # if value less than max seen add to count
                # if value > max seen update max seen
        
        count = [0] * 101
        for h in heights:
            count[h] += 1

        expected = []
        for h in range(1, 101):
            c = count[h]
            for _ in range(c):
                expected.append(h)
        
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        
        return res
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # array is always n^2 length 
            # contains values 1 - n^2
                # 1 - (len(grid) * 2)
        # a appears twice
        # b is missing 

        # simple approach, create dict with all possible values
        # count of grid
        # return where in dict that count equals two or missing 

        count = {}
        res = []
        for i in range(1, (len(grid) ** 2) + 1):
            count[i] = 0
        print(count)
        
        for nums in grid:
            for num in nums:
                count[num] = count.get(num, 0) + 1
        print(count)
        for idx, c in count.items():
            if c == 2:
                res.insert(0, idx)
            if c == 0:
                res.insert(1, idx)
        
        return res


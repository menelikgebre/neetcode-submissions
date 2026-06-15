class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # what we need to know
            # frequency of each variable
            # which variable value = frequency
        # from there we just need to return the largest one

        # from collections import Counter
        # count = Counter.arr
        count = {}
        res = -1
        for char in arr:
            count[char] = count.get(char, 0) + 1
        
        for char in count:
            if char == count[char]:
                res = max(res, char)
        
        return res
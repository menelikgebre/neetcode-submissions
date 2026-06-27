# from collections import Counter
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1
        count = {}
        for idx, char in enumerate(s):
            if char not in count:
                count[char] = idx
            else:
                res = max(res,(idx - count[char] - 1) )
                # res = max(res,len(s[count[char]:idx]) - 1)
        return res
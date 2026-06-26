from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        has_odd = False  # Track if we've seen ANY odd frequency

        for val in count.values():
            if val % 2 == 0:
                res += val
            else:
                res += (val - 1)  # Take the largest even part
                has_odd = True    # Mark that we have a leftover for the center
        
        # If we found at least one odd frequency, we can place 1 character in the middle
        if has_odd:
            res += 1
            
        return res
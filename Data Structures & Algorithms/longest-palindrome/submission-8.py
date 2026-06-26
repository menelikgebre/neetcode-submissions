from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        
        # Sum up the maximum even component of every character count
        res = sum((val // 2) * 2 for val in count.values())
        
        # If there's room left, we can put one unique character in the center
        return res + 1 if res < len(s) else res
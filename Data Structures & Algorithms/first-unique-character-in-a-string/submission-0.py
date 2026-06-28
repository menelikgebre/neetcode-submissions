from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:

        # convert to hash map of freq
        counts = Counter(s)

        # find first instance where freq = 1
        for char, freq in counts.items():
            if freq == 1:
                return s.index(char)
        return -1

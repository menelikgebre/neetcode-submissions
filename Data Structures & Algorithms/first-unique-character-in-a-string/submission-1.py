from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:

        # convert to hash map of freq
        counts = Counter(s)

        # find first instance where freq = 1
        for i, char in enumerate(s):
                    if counts[char] == 1:
                        return i  # Return the index immediately!
                
        return -1
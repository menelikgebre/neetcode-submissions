from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # use magazine chars to create ransomNote 

        pool = Counter(magazine) # {a: 2}
        word_count = Counter(ransomNote) # {a: 2, b: 1}
        return True if not word_count - pool else False
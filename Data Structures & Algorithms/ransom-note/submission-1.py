from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # use magazine chars to create ransomNote 

        pool, word_count  = Counter(magazine), Counter(ransomNote) 
        return True if not word_count - pool else False
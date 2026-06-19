class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        pool = set(allowed)
        return sum(set(word) <= pool for word in words)
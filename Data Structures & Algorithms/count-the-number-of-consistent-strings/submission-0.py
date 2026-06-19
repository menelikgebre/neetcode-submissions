class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        pool = set(allowed)

        for word in words:
            # check that all strings in word are in pool
            chars = set(word)
            print(f"pool + {pool}")
            print(f"chars + {chars}")
            if chars.issubset(pool):
                res += 1
        return res 

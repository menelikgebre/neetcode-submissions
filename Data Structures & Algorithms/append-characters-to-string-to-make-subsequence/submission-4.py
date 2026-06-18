class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p1, p2 = 0, 0
        len_s, len_t = len(s), len(t)

        while p1 < len(s) and p2 < len_t:
            if s[p1] == t[p2]:
                p2 += 1
            p1 += 1
        return len_t - p2
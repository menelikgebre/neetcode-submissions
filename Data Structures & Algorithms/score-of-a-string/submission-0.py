class Solution:
    def scoreOfString(self, s: str) -> int:
        # ord()
        # calculating sum of abs(ord(i) - ord(i-1))
        total = 0
        prev = ord(s[0])

        for char in s[1:]:
            curr = ord(char)
            total += abs(curr - prev)
            prev = curr
        return total
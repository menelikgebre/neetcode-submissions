class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        balloon = Counter("balloon")

        res = len(text) # default max 
        for char in balloon:
            res = min(res, count[char] // balloon[char])
        return res

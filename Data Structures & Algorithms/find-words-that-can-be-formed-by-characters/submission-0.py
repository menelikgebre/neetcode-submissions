from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = ""
        count = Counter(chars)

        for word in words:
            word_count = Counter(word)
            valid = all(char in count and freq <= count[char] for char, freq in word_count.items())
            if valid:
                res += word
        
        return len(res)
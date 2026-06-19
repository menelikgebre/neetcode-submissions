class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_pool = Counter(chars)
        
        # If (word_count - char_pool) is empty, char_pool completely covered the word
        return sum(len(w) for w in words if not Counter(w) - char_pool)
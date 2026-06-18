class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'} # Using a set is faster for lookups O(1)
        
        # Step 1: Create a running total (prefix sum) array
        # prefix[i] will store the total number of valid words from index 0 up to i-1
        prefix = [0] * (len(words) + 1)
        
        for i, word in enumerate(words):
            # Check if current word is valid
            is_vowel_string = 1 if word[0] in vowels and word[-1] in vowels else 0
            # Next prefix value is the previous total + current word's value
            prefix[i + 1] = prefix[i] + is_vowel_string
            
        # Step 2: Answer each query instantly in O(1) time
        ans = []
        for li, ri in queries:
            # The magic formula: total up to 'ri' minus total right before 'li'
            # Because of our +1 offset in the prefix array, this maps perfectly to:
            count = prefix[ri + 1] - prefix[li]
            ans.append(count)
            
        return ans
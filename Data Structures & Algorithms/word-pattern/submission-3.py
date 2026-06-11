class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # map letters in pattern -> words in s 
        # make sure that string follows the pattern
        # for this to work 
            # check that same length 
            # check that each letter -> word mapping is unique
                # also check that ONLY ONE letter -> word mapping exist per letter
            
            

        
        s = s.split(" ")
        if len(pattern) != len(s):
            return False
        pairs, seen = {}, set()
        for key, char in enumerate(pattern):
            if char in pairs:
                if pairs[char] != s[key]:
                    return False
            else:
                if s[key] in seen:
                    return False
                pairs[char] = s[key]
                seen.add(s[key])
        
        return True


        # words = [dog, cat, cat, fish]
        # pairs = {dog: a, cat:b,  }

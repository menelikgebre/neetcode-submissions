class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # words at least len >= 1, each element len >= 1
            # all elements unique 
        # finding common sequence -> comparing against each other inevitable

        # for each element i, check against rest of elements j is i in j
            # first instance we find it being true add to result
            # wrost case loop through whole rest of list dont find any matches
        
        # sort by len? 
        # 

        words_sorted = sorted(words, key=len)
        # words=["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
        res = []
        i = 0

        while i < len(words_sorted) - 1:
            for word in words_sorted[i+1:]:
                if words_sorted[i] in word:
                    res.append(words_sorted[i])
                    break 
            i += 1
        
        return res 
                    

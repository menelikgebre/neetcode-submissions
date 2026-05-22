class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) < 1:
            return [[""]]
        
        groups = {} # {sort_key: [words]}
        for word in strs:
            key = "".join(sorted(word))
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
        
        return list(groups.values())
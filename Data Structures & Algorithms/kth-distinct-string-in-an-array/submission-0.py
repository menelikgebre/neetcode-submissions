class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # return the kth distinct value in the list
            # distinct value means only appears once 
        # if there is no kth distinct value return empty string 

        # dict use insertion order 
        # count values in the array
        # for each pair in dict, check if count is = 1
            # every time you distinct value, substract one from k
            # once you find the kth distinct value return it 

        # O(n) memory and O(n) time 

        counts = {}
        for char in arr:
            counts[char] = counts.get(char, 0) + 1
                
        for char, count in counts.items():
            if count == 1 and k == 1:
                return char
            elif count == 1 and k > 1:
                k -= 1
        
        return ""
            
                         
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # maximum number of instances of "balloon" can be formed
            # len(text) >= 1
        
        # want to know whats available in ballon?

        count = {}
        # {'n': 1, 'l': 2, 'a': 1, 'e': 1, 'b': 1, 'o': 2, 'k': 1}
        res = 0
        for s in text:
            count[s] = count.get(s, 0) + 1
        
        # go through balloon, check count if we have elem to spare
            # if so continue, once we get to end of balloon res + 1
            # if we are missing elem, just stop and return res 
        
        while count:
            for char in "balloon":
                if char in count and count[char] >= 1:
                    count[char] -= 1
                else:
                    return res 
            res += 1


class Solution:
    def maxDifference(self, s: str) -> int:
        # len(s) >= 3
        # always at least one odd and one even freq

        # brute force ->   
            # loop through string, count up freq in dict
            # dict.values() -> find max odd number and min even number

        # aaaaabbc
        # {a:5, b:2, c:1}
        # [5,2,1]
        # 
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        max_o, min_e = 0,max(count.values())
        for num in count.values():
            if num % 2 == 0:
                min_e = min(min_e, num)
                # get min even value, cant start from zero
            else:
                max_o = max(max_o, num)
        
        return max_o - min_e

                

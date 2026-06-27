class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # find one duplicate
        # return duplicate value and missing value

        # duplicate, just track w/ set and return dip
        # get missing value
            # set(1 - n) - set(seen)
        
        # what if just want to go until dup found and return

        res = []
        seen = set()
        for num in nums:
            if num in seen:
                res.append(num)
                continue
            seen.add(num)
        res.extend(set(range(1, len(nums) + 1)) - seen)

        return res
            
        
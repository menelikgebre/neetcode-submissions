class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # good pairs means
            # two equal values + one index less than the other
            # can reuse elements to create more than one pair 
    
        
        # need to go through the whole list
        # need to track what we've seen to some extent

        # if you see value then store it, index important
            # if it comes up again at higher index
                # find all instances at previous indexes
        
        # {i: [0, 3, 4]}
            # when we see 1 at i=3, len(seen[1] = 1)
                # so we add 1 to res
                # then at i=4, len(seen[1] = 2 so add 2 to res

        seen = {}
        res = 0

        for i, num in enumerate(nums):
            if seen.get(num):
                res += len(seen[num])
                seen[num].append(i)
            else:
                seen[num] = [i]
        
        return res 


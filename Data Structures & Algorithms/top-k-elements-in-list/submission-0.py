class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # clarifying 
        # k can be less than number of distinct lements but not greater
            # k = 2 nums = [1,1,2,4,3,3,5,5] OK (return most frequent)
            # k = 2 nums = [1, 2, 2] X (not possible)
        # len(nums) >= 1

        # thoughts
            # thinking have to count up first
            # then use dict to select top two values?
                # loop through dict k times, add max to result then remove
        
        count = {}
        result = []
        for i, num in enumerate(nums):
            count[num] = count.get(num, 0) + 1
            # {2 : 1, 3: 2, ....}
        
        while k > 0:
            rep_char = max(count, key=count.get)
            result.append(rep_char)
            count.pop(rep_char)
            k -= 1

        return result
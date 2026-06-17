class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # looking for pairs, requires tracking whats been seen to extent
            # create dict of seen

        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        for freq in seen.values():
            if freq % 2 != 0:
                return False
        
        return True
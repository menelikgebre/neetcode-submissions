class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # looking for pairs, requires tracking whats been seen to extent
            # create dict of seen

        seen = set()

        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)

        return len(seen) == 0
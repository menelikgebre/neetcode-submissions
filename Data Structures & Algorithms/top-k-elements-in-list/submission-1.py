class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort approach
        
        # count: maps each number -> how many times it appears
        count = {}
        
        # freq: index = frequency, value = list of numbers that appear that many times
        # Size is len(nums) + 1 because the max possible frequency is len(nums)
        # (if every element in nums is the same). We need index len(nums) to be valid,
        # hence +1. Index 0 is unused (no number has frequency 0).
        # Example for nums = [1,1,1,2,2,3]:
        #   freq = [[], [3], [2], [1], [], [], []]
        #            0   1    2    3   4   5   6
        freq = [[] for i in range(len(nums) + 1)]
        
        # Step 1: count occurrences of each number — O(n)
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # After this: count = {1: 3, 2: 2, 3: 1} for the example above
        
        # Step 2: bucket each number by its frequency — O(d) where d = distinct elements
        # We're inverting the dict: instead of "number -> count",
        # we now have "count -> list of numbers with that count"
        for n, c in count.items():  # returns key, value pairs
            freq[c].append(n)
        # After this: freq = [[], [3], [2], [1], [], [], []]
        
        res = []
        
        # Step 3: walk freq from highest index (most frequent) down to 1 — O(n) total
        # We start at len(freq) - 1 (highest possible frequency) and go down to 1.
        # The third arg -1 means step backwards.
        for i in range(len(freq) - 1, 0, -1):
            # Each bucket may have multiple numbers (ties in frequency),
            # so loop through them
            for n in freq[i]:
                res.append(n)
                # Stop as soon as we have k elements — they're guaranteed
                # to be the most frequent because we walked top-down
                if len(res) == k:
                    return res
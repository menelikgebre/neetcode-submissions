class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
# Initialize our tracking variables
        # Float infinity ensures any number in the array will overwrite them
        max1 = max2 = float('-inf')
        min1 = min2 = float('inf')
        
        for num in nums:
            # 1. Update the two largest numbers
            if num > max1:
                max2 = max1  # Old biggest slides down to second biggest
                max1 = num   # New biggest found
            elif num > max2:
                max2 = num   # Shacks up in second place
                
            # 2. Update the two smallest numbers
            if num < min1:
                min2 = min1  # Old smallest slides down to second smallest
                min1 = num   # New smallest found
            elif num < min2:
                min2 = num   # Shacks up in second smallest place
                
        return (max1 * max2) - (min1 * min2)
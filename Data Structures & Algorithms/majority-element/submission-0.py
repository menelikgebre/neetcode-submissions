class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # can there be more than one majority element, and need to find highest value?
            # will assume there will always only be one majority element

        # majority -> shows up more than 50% of the time 
            # can assume there will always be one that exists 

        # threshold = (len(nums) / 2) -> may return float type 
        
        # brute force -> iterate the whole list 
            # count element and values in dict {element: count}
            # loop through dict to find element w/ value > threshold 
        
        counts = {}
        threshold = (len(nums) + 1) / 2
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        for element, count in counts.items():
            if count >= threshold:
                return element 
                    
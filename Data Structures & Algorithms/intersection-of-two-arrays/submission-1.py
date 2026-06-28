class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # what elements present in both arrays 
        # convert to sets and subtract from each other 

        return list(set(nums1) & set(nums2))
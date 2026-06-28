class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # what elements present in both arrays 
        # convert to sets and subtract from each other 

        set1, set2 = set(nums1), set(nums2)
        res = []
        for num in set1:
            if num in set2:
                res.append(num)
        return res
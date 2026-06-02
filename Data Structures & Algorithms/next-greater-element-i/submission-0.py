class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_map = {val:index for index, val in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] not in nums1_map:
                continue 
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    index = nums1_map[nums2[i]]
                    res[index] = nums2[j]
                    break
        return res
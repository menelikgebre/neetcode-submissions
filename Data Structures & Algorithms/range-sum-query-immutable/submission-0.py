class NumArray:

    def __init__(self, nums: List[int]):
        # initiate array
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        # sum of left -> right (inclusive)
        # left and right will always be in bounds, left always <= right
        sumRange, p1= 0, left
        while p1 <= right:
            sumRange += self.nums[p1]
            p1 += 1
        return sumRange


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
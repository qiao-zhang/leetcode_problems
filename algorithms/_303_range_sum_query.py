from collections import defaultdict
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.sum = sum(nums)
        self.leftsums = {}
        leftsum = 0
        for i, n in enumerate(nums):
            self.leftsums[i] = leftsum = leftsum + n


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.leftsums[j] - self.leftsums[i] + self.nums[i]




# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySI(nums, target)

    def binarySI(self, nums, target):
        lo, hi = 0, len(nums)
        while lo < hi:
            m = (lo + hi) // 2
            if nums[m] == target: return m
            if nums[m] > target:
                hi = m
            else:
                lo = m + 1
        return hi

    def bisectSI(self, nums, target):
        return bisect.bisect_left(nums, target)

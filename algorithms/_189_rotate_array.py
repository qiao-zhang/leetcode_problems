class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l <= 1:
            return
        r = k % l
        if r <= l // 2:
            right = nums[-r:]
            nums[r:] = nums[:-r]
            nums[:r] = right
        else:
            left = nums[:-r]
            nums[:r] = nums[-r:]
            nums[r:] = left

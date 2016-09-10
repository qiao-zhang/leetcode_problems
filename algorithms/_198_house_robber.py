class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) is 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        mx = [0 for _ in nums]
        mx[0] = nums[0]
        mx[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            mx[i] = max(mx[i - 1], mx[i - 2] + nums[i])
        return mx[-1]

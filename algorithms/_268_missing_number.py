class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums) + 1
        s = l * len(nums) / 2
        return s - sum(nums)

    def missingNumberXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i, n in enumerate(nums):
            res ^= n ^ i
        return res ^ len(nums)

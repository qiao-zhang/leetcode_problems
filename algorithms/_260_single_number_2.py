class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(nums) - 1
        while j - i > 1:
            mid = (j - i) // 2
            l, r = 0, 0
            x = i
            while x <= mid:
                l ^=

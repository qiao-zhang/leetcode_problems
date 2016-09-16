class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def solveBS():
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                m = (lo + hi) // 2
                if nums[m] < nums[hi]: hi = m
                else: lo = m + 1
            return nums[hi]
        return solveBS()
        

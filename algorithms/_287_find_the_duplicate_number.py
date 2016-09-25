class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        assert len(nums) > 1
        def solveBS():
            lo, hi = 1, len(nums) - 1
            while lo < hi:
                m = (lo + hi) // 2
                se = 0
                for num in nums:
                    if num <= m: se += 1
                if se > m: hi = m
                else: lo = m + 1
            return hi

        def solveLinearTime():
            slow, fast = nums[0], nums[nums[0]]
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]
            finder = 0
            while slow != finder:
                slow = nums[slow]
                finder = nums[finder]
            return slow
            
        return solveLinearTime()

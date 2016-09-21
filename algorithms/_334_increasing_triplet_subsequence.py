class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def bisect_left(nums, num):
            lo, hi = 0, len(nums)
            while lo < hi:
                m = (lo + hi) // 2
                if nums[m] == num: return m
                if nums[m] < num: lo = m + 1
                else: hi = m
            return hi
            
        def solve(k=3):
            dp = [float('inf')] * (k - 1)
            for num in nums:
                i = bisect_left(dp, num)
                if i >= k - 1: return True
                dp[i] = num
            return False

        return solve()

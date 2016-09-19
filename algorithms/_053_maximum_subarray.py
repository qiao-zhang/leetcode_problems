class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def solveIteratively():
            s, ms = 0, -float('inf')
            for num in nums:
                s += num
                ms = max(s, ms)
                if s < 0: s = 0
            return ms

        def solveDC():
            assert nums
            def helper(lo=0, hi=len(nums)-1):
                if hi == lo: return (nums[lo], ) * 4
                m = (lo + hi) // 2
                fb, fn, fl, fr = helper(lo, m)
                sb, sn, sl, sr = helper(m+1, hi)
                return fb + sb, max(fn, sn, fr + sl), max(fl, fb + sl), max(fr + sb, sr)
            return max(helper())
        return solveDC()

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def solveIteratively():
            assert nums
            s, ms = 0, -float('inf')
            for num in nums:
                s += num
                ms = max(s, ms)
                s = max(0, s)
            return ms

        def solveDC():
            assert nums
            def helper(nums=nums):
                if len(nums) == 1: return (nums[0],) * 4
                m = len(nums) // 2
                fb, fn, fl, fr = helper(nums[:m])
                sb, sn, sl, sr = helper(nums[m:])
                return fb + sb, max(fn, sn, fr + sl), max(fl, fb + sl), max(fr + sb, sr)
            return max(helper())

        return solveDC()

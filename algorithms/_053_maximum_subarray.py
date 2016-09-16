class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def solveIteratively():
            if not nums: return
            s, ms = 0, -float('inf')
            for num in nums:
                s += num
                ms = max(s, ms)
                s = max(0, s)
            return ms

        def solveRecursively(start=0):
            if start >= len(nums): return -float('inf')
            i, s, ms = start+1, nums[start], nums[start]
            while i < len(nums) and s > 0:
                s += nums[i]
                ms = max(ms, s)
                i += 1
            return max(ms, solveRecursively(i))
        return solveIteratively()

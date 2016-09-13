class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        D = [1] + [0] * target
        for i in range(1, target + 1):
            for j in nums:
                if j > i: continue
                D[i] += D[i - j]
        return D[target]

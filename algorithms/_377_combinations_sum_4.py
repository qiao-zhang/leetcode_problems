class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        D = [1] + [0] * target
        for i in range(1, target + 1):
            D[i] = sum(D[i - j] for j in nums if j <= i)
        return D[target]

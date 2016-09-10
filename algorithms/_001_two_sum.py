class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sn = sorted((num, i) for i, num in enumerate(nums))
        i, j = 0, len(nums) - 1
        while i < j:
            n, k = sn[i]
            m, l = sn[j]
            if n + m == target:
                return [k, l]
            if n + m < target:
                i += 1
                continue
            j -= 1

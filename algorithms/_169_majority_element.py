class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = len(nums) // 2
        C = {}
        for num in nums:
            if num not in C:
                C[num] = 0
            C[num] += 1
            if C[num] > t:
                return num

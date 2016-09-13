class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mask = reduce(operator.xor, nums)
        ans = reduce(operator.xor, (x for x in nums if x & mask & -mask))
        return [ans, ans ^ mask]

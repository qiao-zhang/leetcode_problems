class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        num = n
        while num > 0:
            result += num % 2
            num = num // 2
        return result

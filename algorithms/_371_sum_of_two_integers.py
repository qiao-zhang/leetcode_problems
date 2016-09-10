from math import log2
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # return sum([a, b])
        return log2(2**a * 2**b)

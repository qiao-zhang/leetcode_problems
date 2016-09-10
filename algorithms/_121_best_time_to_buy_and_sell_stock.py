class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        highest, o = 0, 0
        for i in prices[::-1]:
            highest = max(highest, o - i)
            o = max(o, i)
        return highest

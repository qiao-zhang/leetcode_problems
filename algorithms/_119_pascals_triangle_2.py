class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        assert rowIndex >= 0
        def chooseFrom(k, n):
            assert 0 <= k <= n
            from math import factorial
            return factorial(n) / factorial(k) / factorial(n-k)
        return [chooseFrom(k, rowIndex) for k in range(0, rowIndex+1)]

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        D = [1, 1] + [0] * (n - 1)
        for i in range(2, n+1):
            for left in range(i):
                D[i] += D[left] * D[i-1-left]
        return D[n]

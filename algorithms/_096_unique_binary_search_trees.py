class Solution(object):
    def numTreesDP(self, n):
        """
        :type n: int
        :rtype: int
        """
        D = [1] + [0] * n
        for i in range(1, n+1):
            for left in range(i):
                D[i] += D[left] * D[i-1-left]
        return D[n]

    def numTrees(self, n):
        return math.factorial(n*2) / (math.factorial(n) * math.factorial(n+1))

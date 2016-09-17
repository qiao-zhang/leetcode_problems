class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        def solveDP():
            D = [1] * (n + 1)
            for i in range(1, n+1):
                D[i] = sum(D[k] * D[i-k-1] for k in range(i))
            return D[n]
        def solveMath():
            return math.factorial(n * 2) / math.factorial(n) / math.factorial(n + 1)
        return solveDP()

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.numTreesDP(n)

    def numTreesDP(self, n):
        d = [1] + [0] * n
        for i in range(1, n+1):
            d[i] = sum(d[left] * d[i-1-left] for left in range(i))
        return d[n]

    def numTreesMath(self, n):
        return math.factorial(n * 2) / math.factorial(n) / math.factorial(n+1)

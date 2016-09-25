class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def solveRecursively(n=n):
            if n == 0: return [0]
            half = solve(n - 1)
            return half + [2 ** (n-1) + e for e in half[::-1]]

        def solveIteratively():
            res = [0]
            for i in range(n):
                res += [2 ** i + num for num in res[::-1]]
            return res

        return solveIteratively()

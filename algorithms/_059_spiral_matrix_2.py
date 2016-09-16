class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n: return []
        def solveIteratively():
            res = [[0] * n for _ in range(n)]
            r, c, dr, dc = 0, 0, 0, 1
            for i in range(1, n * n + 1):
                res[r][c] = i
                if A[(r+dr) % n][(c+dc) % n]:
                    di, dj = dj, -di
                r, c = r + dr, c + dc
            return res
        return solveIteratively()

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def solveDP():
            if not grid: return 0
            rows, cols = len(grid), len(grid[0])
            D = [0] + [float('inf')] * (cols - 1)
            for r in range(rows):
                D[0] += grid[r][0]
                for c in range(1, cols):
                    D[c] = min(D[c] + grid[r][c], D[c-1] + grid[r][c])
            return D[-1]
        return solveDP()

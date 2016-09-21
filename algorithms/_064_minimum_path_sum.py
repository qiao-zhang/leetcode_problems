class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def solveDP():
            if not grid: return 0
            cols = len(grid[0])
            D = [0] + [float('inf')] * (cols - 1)
            for row in grid:
                D[0] += row[0]
                for c in range(1, cols):
                    D[c] = min(D[c], D[c-1]) + row[c]
            return D[-1]
        return solveDP()

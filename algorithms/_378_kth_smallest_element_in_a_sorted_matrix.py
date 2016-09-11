from heapq import heappush, heappop
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        Q = [(matrix[0][0], 0, 0)]
        v, n = None, len(matrix)
        for i in range(k):
            v, r, c = heappop(Q)
            # elements not on the top and right would be pushed
            # into the heap twice
            if r > 0 and c > 0: heappop(Q)
            if c + 1 < n:
                heappush(Q, (matrix[r][c+1], r, c+1))
            if r + 1 < n:
                heappush(Q, (matrix[r+1][c], r+1, c))
        return v

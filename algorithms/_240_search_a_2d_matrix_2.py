class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        c = len(matrix[0]) - 1
        for row in matrix:
            while maxc >= 0 and row[c] > target:
                maxc -= 1
            if row[maxc] == target: return True
        return False

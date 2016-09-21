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
            while c >= 0 and row[c] > target:
                c -= 1
            if c < 0: return False
            if row[c] == target: return True
        return False

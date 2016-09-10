from collections import Counter
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        validChars = Counter('.123456789')
        def valid9(nums):
            c = Counter(nums)
            if set(c) > set(validChars):
                return False
            r = c - validChars
            if '.' in r:
                return len(r) == 1
            else:
                return len(r) == 0

        for row in board:
            if not valid9(row):
                return False
        for c in range(9):
            col = [row[c] for row in board]
            if not valid9(col):
                return False
        for r in range(9):
            rows = board[r//3*3:r//3*3+3]
            square = [row[r%3*3:r%3*3+3] for row in rows]
            if not valid9(square):
                return False
        return True

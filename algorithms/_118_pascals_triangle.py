class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        tri = [[1]]
        for r in range(numRows-1):
            lastRow = tri[-1]
            thisRow = [1] + \
                [lastRow[i] + lastRow[i-1] for i in range(1, len(lastRow))] +\
                [1]
            tri.append(thisRow)
        return tri

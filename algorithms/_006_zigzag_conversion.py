class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        for i, l in enumerate(s):
            x = numRows * 2 - 2
            r = i % x
            r = r if r <= x/2 else x - r
            rows[r].append(l)
        return ''.join(l for row in rows for l in row)

"""
0   0
1 3 1
2
0    6      12
1  5 7   11
2 4  8 10
3    9
"""

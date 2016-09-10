# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        i, j = 1, n
        while i < j:
            m = (i + j) // 2
            if isBadVersion(m):
                j = m
            else:
                i = m + 1
        return i

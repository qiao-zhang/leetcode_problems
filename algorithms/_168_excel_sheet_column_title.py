from math import log, floor
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 26:
            return chr(n + 64)
        r = n % 27
        return self.convertToTitle((n - r) // 26) + chr(r + 64)

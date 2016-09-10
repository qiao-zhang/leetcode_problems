from math import log, floor

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        assert n >= 0
        if n < 5:
            return 0
        r, groups = 0, floor(n / 5)
        m = int(5 ** floor(log(n, 5)))
        while m >= 5:
            r += int(floor(n / m))
            m /= 5
        return r

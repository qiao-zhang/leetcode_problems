class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        assert n >= 0
        m, p = n, 0
        while m >= 2:
            m = m // 2
            p += 1
        i = 2 ** (p // 2)
        while i * i <= n:
            i += 1
        return i - 1

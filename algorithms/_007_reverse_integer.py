class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        m, s, r = abs(x), x / abs(x), 0
        while m > 0:
            r = r * 10 + m % 10
            if (x < 0 and r > 2**31) or (x > 0 and r >= 2**31) :
                return 0
            m = m // 10
        return r * s

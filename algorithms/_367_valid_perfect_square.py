class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def binarySearch():
            lo, hi = 1, num/2
            while lo < hi:
                m = (lo + hi) // 2
                if m * m == num: return True
                if m * m < num: lo = m + 1
                else: hi = m - 1
            return lo * lo == num

        def newton():
            r = num
            while r * r > num:
                r = (r + num/r) / 2
            return r * r == num
            
        return newton()

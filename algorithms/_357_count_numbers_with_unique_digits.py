class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        assert n >= 0
        return self.__table[min(n, 10)]

    def __init__(self):
        self.__table = [1] * 11
        self.__table[1] = 10
        inc = 9 * 9
        for i in range(2, 11):
            self.__table[i] = self.__table[i - 1] + inc
            inc *= (10 - i)

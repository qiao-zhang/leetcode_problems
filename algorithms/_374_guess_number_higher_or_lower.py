# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def makeGuess(low, high):
            assert low <= high
            return (low + high) // 2
        low, high = 1, n
        while low <= high:
            g = makeGuess(low, high)
            if guess(g) == 0:
                return g
            if guess(g) == 1:
                low = g + 1
            else:
                high = g - 1
        return None

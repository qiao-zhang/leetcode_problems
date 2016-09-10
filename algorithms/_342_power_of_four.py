class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        s = bin(num-1)[2:]
        if '0' in s:
            return False
        if len(s) % 2 != 0:
            return False
        return True

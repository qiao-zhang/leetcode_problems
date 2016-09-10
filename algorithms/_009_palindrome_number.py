class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        n, rev = x, 0
        while n > 0:
            last = n % 10
            rev = rev * 10 + last
            n /= 10
        if x == rev:
            return True
        return False

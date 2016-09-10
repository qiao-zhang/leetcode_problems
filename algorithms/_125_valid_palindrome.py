import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(s):
            l = len(s)
            if l <= 1:
                return True
            i, j = 0, l - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        chars = re.sub(r'[^A-Za-z0-9]+', '', s).lower()
        return isPalindrome(chars)

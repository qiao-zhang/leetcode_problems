class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        D = {}
        for n in range(65, 91):
            D[chr(n)] = n - 64
        i, num = 0, 0
        while i < len(s):
            num += D[s[i]] * (26 ** (len(s) - i - 1))
            i += 1
        return num

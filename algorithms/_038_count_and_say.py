class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        last = self.countAndSay(n-1)
        l = []
        d, c = last[0], 1
        i = 1
        while i < len(last):
            if last[i] == d:
                c += 1
                i += 1
                continue
            l.append(str(c) + d)
            d, c = last[i], 1
            i += 1
        l.append(str(c) + d)
        return ''.join(l)

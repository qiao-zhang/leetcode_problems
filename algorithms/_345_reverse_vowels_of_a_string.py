from collections import deque
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        pos, r = deque([]), list(s)
        for i, l in enumerate(r):
            if l in 'aeiouAEIOU':
                pos.append(i)
        while len(pos) > 1:
            i, j = pos.popleft(), pos.pop()
            r[i], r[j] = r[j], r[i]
        return ''.join(r)

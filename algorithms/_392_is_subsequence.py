class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i >= len(s) else False

    def isSubsequence2(self, s, t):
        """
        :type s: str
        :type t: AdvancedString
        :rtype: bool
        """
        if not s: return True
        if t.length == 0: return False
        i = 0
        for l in s:
            j = t.minValidAfter(l, i)
            if j < 0: return False
            i = j
        return True

from collections import defaultdict
class AdvancedString(object):
    def __init__(self, t):
        self.length = len(t)
        self._indexes = defaultdict(list)
        for i, l in enumerate(t):
            self.__indexes[l].append(i)

    def minValidIndex(self, letter, i):
        indexes = self._indexes[letter]
        if i >= indexes[-1]: return -1
        l, r = 0, len(indexes) - 1
        while l < r:
            m = (l + r) // 2
            if i == indexes[m]: return indexes[m+1]
            if i < indexes[m]:
                r = m
            else:
                l = m + 1
        return indexes[l]

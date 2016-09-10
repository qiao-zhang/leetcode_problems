from heapq import heappush, heappop
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        if len(strs) == 2:
            s, l = strs[0], strs[1]
            if len(s) > len(l):
                s, l = l, s
            if s == '':
                return ''
            for i, c in enumerate(s):
                if c != l[i]:
                    return s[:i]
            return s
        half1 = self.longestCommonPrefix(strs[:len(strs)//2])
        half2 = self.longestCommonPrefix(strs[len(strs)//2:])
        return self.longestCommonPrefix([half1, half2])

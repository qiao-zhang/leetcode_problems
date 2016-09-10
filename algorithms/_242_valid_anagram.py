class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        D = {}
        for sl in s:
            if sl not in D:
                D[sl] = 1
            else:
                D[sl] += 1
        for tl in t:
            if tl not in D:
                return False
            else:
                D[tl] -= 1
        for l in D:
            if D[l] != 0:
                return False
        return True

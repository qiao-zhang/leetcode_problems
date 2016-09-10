class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        assert len(s) == len(t)
        m, u = {}, set()
        for i, l in enumerate(s):
            if l not in m:
                if t[i] in u:
                    return False
                m[l] = t[i]
                u.add(t[i])
                continue
            if t[i] != m[l]:
                return False
        return True

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = version1.split('.'), version2.split('.')
        l = min(len(v1), len(v2))
        i = 0
        while i < l:
            if int(v1[i]) > int(v2[i]):
                return 1
            if int(v1[i]) < int(v2[i]):
                return -1
            i += 1
        if len(v1) < len(v2) and sum(int(n) for n in v2[i:]) > 0:
            return -1
        if len(v1) > len(v2) and sum(int(n) for n in v1[i:]) > 0:
            return 1
        return 0

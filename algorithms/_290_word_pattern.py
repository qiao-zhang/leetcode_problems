class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')
        if len(pattern) != len(words):
            return False
        mapping, vals = {}, set()
        for i, l in enumerate(pattern):
            if l not in mapping:
                if words[i] in vals:
                    return False
                mapping[l] = words[i]
                vals.add(words[i])
                continue
            if words[i] != mapping[l]:
                return False
        return True

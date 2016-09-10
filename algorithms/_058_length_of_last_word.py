class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # words = s.split()
        # if words:
        #     return len(s.split()[-1])
        # return 0
        end = len(s) - 1
        while end >= 0:
            if s[end] != ' ':
                break
            end -= 1
        if end < 0:
            return 0
        beg = end - 1
        while beg >= 0:
            if s[beg] == ' ':
                break
            beg -= 1
        return end - beg

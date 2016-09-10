class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l = len(needle)
        i = 0
        while i <= len(haystack) - l:
            j = 0
            while j < l:
                if haystack[i+j] != needle[j]:
                    break
                j += 1
            if j == l:
                return i
            i += 1
        return -1

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
                continue
            if c not in mapping:
                return False
            if len(stack) == 0:
                return False
            if c in mapping and stack.pop() != mapping[c]:
                return False
        if len(stack) > 0:
            return False
        return True

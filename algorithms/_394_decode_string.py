class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [['', 1]]
        numStr = ''
        for c in s:
            if c.isdigit():
                numStr += c
            elif c == '[':
                stack.append(['', int(numStr)])
                numStr = ''
            elif c == ']':
                st, k = stack.pop()
                stack[-1][0] += (st * k)
            else:
                stack[-1][0] += c
        return stack[0][0]

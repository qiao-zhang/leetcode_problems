class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def solveIteratively():
            stack, num = [['', 1]], ''
            for ch in s:
                if ch.isdigit():
                    num += ch
                elif ch == '[':
                    stack.append(['', int(num)])
                    num = ''
                elif ch == ']':
                    p, n = stack.pop()
                    stack[-1][0] += p * n
                else:
                    stack[-1][0] += ch
            return stack[-1][0]
        return solveIteratively()

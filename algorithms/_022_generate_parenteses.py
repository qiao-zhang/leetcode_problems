from collections import deque
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(pattern, left, right):
            if left: yield from generate(pattern + '(', left-1, right)
            if right > left: yield from generate(pattern + ')', left, right-1)
            if not right: yield pattern
        return list(generate('', n, n))

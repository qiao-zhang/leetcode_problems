class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def solveDFS():
            def helper(pattern='', left=n, right=n)
                if left:
                    for p in solveDFS(pattern + '(', left-1, right):
                        yield p
                if right > left:
                    for p in solveDFS(pattern + ')', left, right-1):
                        yield p
                if not right:
                    yield pattern
            return list(helper())

        def solveBFS():
            res, queue = [], collections.deque([('', n, n)])
            while queue:
                pattern, left, right = queue.popleft()
                if left: queue.append((pattern + '(', left-1, right))
                if right > left: queue.append((pattern + ')', left, right-1))
                if not right:
                    res.append(pattern)
            return res

        return solveBFS()

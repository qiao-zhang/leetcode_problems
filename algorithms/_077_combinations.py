class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def solveUsingLibrary():
            return itertools.combinations(range(1, n+1), k)
        def solveRecursively():
            def helper(lo=1, k=k):
                if n - lo + 1 < k or k <= 0:
                    yield []
                elif n - lo + 1 == k:
                    yield list(range(lo, lo+k))
                else:
                    for i in range(lo, n-k+2):
                        for lst in helper(i+1, k-1):
                            yield [i] + lst
            return list(helper())
        return solveRecursively()

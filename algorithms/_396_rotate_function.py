class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A: return 0
        s = sum(i * n for i, n in enumerate(A))
        t, mx = sum(A), s
        for i in range(len(A)-1, 0, -1):
            s += t - A[i] * len(A)
            mx = max(mx, s)
        return mx

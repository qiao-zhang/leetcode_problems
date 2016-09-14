class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def ksum(start, k, step=1):
            return start * k + k * (k - 1) * step / 2
        def solve(k, n, lo=1, hi=9):
            if k <= 0: return []
            res = []
            for i in range(lo, hi - k + 2):
                s = ksum(i, k)
                if n < s: break
                if n == s:
                    res.append(list(range(i, i+k)))
                    break
                res.extend([i] + lst for lst in solve(k-1, n-i, i+1))
            return res
        return solve(k, n)

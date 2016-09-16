class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def ksum(start, k, step=1):
            return start * k + k * (k - 1) * step / 2

        def solveRecursively(k=k, n=n, lo=1):
            if k <= 0: return []
            if n > ksum(9, k, -1): return []
            res = []
            for i in range(lo, 10):
                s = ksum(i, k)
                if n < s: break
                if n == s: res.append(list(range(i, i+k)))
                else: res.extend([[i] + lst for lst in solveRecursively(k-1, n-i, i+1)])
            return res

        def solveUsingLibrary():
            return [comb for comb in itertools.combinations(range(1, 10), k) if sum(comb) == n]

        return solveRecursively()

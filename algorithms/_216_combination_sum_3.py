class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def solveRecursively():
            def solve(n=n, k=k, lo=1):
                if k <= 0: return
                if n > ksum(9, k, -1): return
                for i in range(lo, 10):
                    m = ksum(i, k)
                    if m > n: return
                    elif m == n:
                        yield list(range(i, i + k))
                        return
                    else:
                        for lst in solve(n-i, k-1, i+1):
                            yield [i] + lst
            def ksum(start, k, step=1):
                return start * k + (k - 1) * k * step / 2
            return list(solve())

        def solveUsingLibrary():
            return [comb for comb in itertools.combinations(range(1, 10), k) if sum(comb) == n]

        return solveRecursively()

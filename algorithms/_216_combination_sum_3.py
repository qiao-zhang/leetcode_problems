class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def solve(k, n, l):
            if k <= 0: return []
            if n <= 0: return []
            if n > (19 - k) * k / 2: return []
            i, res = l, []
            while True:
                mn = (i * 2 + k - 1) * k / 2
                if n < mn: break
                if n == mn:
                    res.append(list(range(i, i+k)))
                    break
                res.extend([i] + p for p in solve(k-1, n-i, i+1))
                i += 1
            return res
        return solve(k, n, 1)

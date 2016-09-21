class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]
        merged = heapq.merge(*map(lambda p: (u * p for u in uglies), primes))
        uniqued = (u for u, _ in itertools.groupby(merged))
        while len(uglies) < n:
            uglies.append(next(uniqued))
        return uglies[-1]

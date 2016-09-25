class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        def solveRegularly():
            assert n > 0
            uglies, ugliesSet, hp = [1], {1}, [(p, p, 0) for p in primes]
            while len(uglies) < n:
                u, p, i = heapq.heappop(hp)
                if u not in ugliesSet:
                    uglies.append(u)
                    ugliesSet.add(u)
                i += 1
                heapq.heappush(hp, (p * uglies[i], p, i))
            return uglies[-1]

        def solveUsingGenerator():
            assert n > 0
            uglies = [1]
            merged = heaqp.merge(*map(lambda p: (p * u for u in uglies), primes))
            uniqued = (u for u, _ in itertools.groupby(merged))
            while len(uglies) < n:
                uglies.append(next(uniqued))
            return uglies[-1]
        return solveRegularly()

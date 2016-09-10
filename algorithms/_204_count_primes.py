class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_prime = [0, 0] + [1] * (n - 2)

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i] == 1:
                for j in range(i*i, n, i):
                    is_prime[j] = False

        return sum(is_prime)

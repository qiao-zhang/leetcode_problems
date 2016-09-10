class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def reverseXBits(n, bits=32):
            assert bits in [32, 16, 8, 4, 2]
            if bits == 2:
                if n == 1:
                    return 2
                if n == 2:
                    return 1
                if n == 0 or n == 3:
                    return n
            left = n // (2**(bits//2))
            right = n % (2**(bits//2))
            return reverseXBits(right, bits//2) * 2**(bits//2) + reverseXBits(left, bits//2)
        return reverseXBits(n)

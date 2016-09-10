class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = [0] * (num + 1)
        for i in range(1, num+1):
            if i % 2 == 1:
                bits[i] = bits[i - 1] + 1
            else:
                bits[i] = bits[i // 2]
        return bits

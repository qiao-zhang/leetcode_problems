# class Solution(object):
#     def integerBreak(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         assert 2 <= n <= 58
#         return self.table[n]
#
#     def __init__(self):
#         self.table = [0, 0, 1, 2, 4, 6, 9, 12] + [0] * 51
#         for i in range(8, 59):
#             p, self.table[i] = 1, i - 1
#             while p <= 3:
#                 if self.table[i - p] * p > self.table[i]:
#                     self.table[i] = self.table[i - p] * p
#                 p += 1
class Solution(object):
    def integerBreak(self, n):
        if n == 2: return 1
        if n == 3: return 2
        r = [4, 6, 9]
        p = (n - 4) // 3
        i = (n - 4) % 3
        return 3 ** p * r[i]

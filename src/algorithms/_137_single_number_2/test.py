import unittest, random
from solution import Solution

class Tests(unittest.TestCase):
    def test(self):
        sol = Solution()
        nums = [1, 1, 1, 2, 2, 3, 4, 4, 3, 2, 3, 4, 2]
        self.assertEqual(sol.another_single_number(nums), 4)

if __name__ == '__main__':
    unittest.main()
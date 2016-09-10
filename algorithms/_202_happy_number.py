class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        met = {n}
        def helper(n, nums):
            s, sm = str(n), 0
            for d in s:
                sm += int(d) ** 2
            if sm == 1:
                return True
            if sm in nums:
                return False
            nums.add(sm)
            return helper(sm, nums)
        return helper(n, met)

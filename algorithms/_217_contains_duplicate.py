class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        C = set()
        for num in nums:
            if num not in C:
                C.add(num)
            else:
                return True
        return False

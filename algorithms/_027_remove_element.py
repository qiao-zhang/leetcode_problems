class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        f, s, l = 0, len(nums) - 1, 0
        while f <= s:
            if nums[s] == val:
                nums[s] == None
                s -= 1
                l += 1
                continue
            if nums[f] != val:
                f += 1
                continue
            nums[f] = nums[s]
            s -= 1
            f += 1
            l += 1
        return len(nums) - l

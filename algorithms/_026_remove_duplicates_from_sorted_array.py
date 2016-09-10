class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        last, cur = 0, 1
        while cur < len(nums):
            if nums[cur] == nums[last]:
                cur += 1
                continue
            if cur - last > 1:
                nums[last+1] = nums[cur]
            last += 1
            cur += 1
        return last + 1

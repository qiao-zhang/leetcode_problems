class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        leftZeroes = 0
        for i, num in enumerate(nums):
            if num == 0:
                leftZeroes += 1
                continue
            nums[i-leftZeroes] = num
        j = len(nums) - 1
        while leftZeroes > 0:
            nums[j] = 0
            leftZeroes -= 1
            j -= 1

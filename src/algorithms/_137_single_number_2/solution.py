'''
Created on 28 May 2015

@author: Qiao Zhang
@question:
Given an array of integers, every element appears three times except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?
'''

class Solution:
    def singleNumber(self, nums):
        """
            @param {int[]} nums: 
            @return {integer}
        """
        pass
    
    def another_single_number(self, nums):
        check_idx = 0
        new_idx = 0
        sum = 0
        while check_idx < len(nums):
            sum += nums[check_idx]
            found = False
            for idx in range(new_idx):
                if nums[check_idx] == nums[idx]:
                    found = True
                    break
            if not found:
                nums[new_idx] = nums[check_idx]
                new_idx += 1
            check_idx += 1
        for idx in range(new_idx):
            sum -= nums[idx] * 3 # sum = (n-3) * sn
        n = len(nums) - new_idx * 3 + 3
        return sum / (n - 3)
    
    def naive_single_number(self, nums):
        counts = {}
        for num in nums:
            if num in counts:
                if counts[num] == 3:
                    return num
                else:
                    counts[num] += 1
            else:
                counts[num] = 1
        for num in counts:
            if not counts[num] == 3:
                return num
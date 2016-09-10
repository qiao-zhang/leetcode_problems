class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        s = numbers[i] + numbers[j]
        while s != target:
            if s < target:
                i += 1
            else:
                j -= 1
            s = numbers[i] + numbers[j]
        return [i + 1, j + 1]

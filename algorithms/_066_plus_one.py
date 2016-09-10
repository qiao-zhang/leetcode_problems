class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        reversedDigits = digits[::-1]
        k = 1
        for i in range(len(digits)):
            if reversedDigits[i] != 9:
                reversedDigits[i] += 1
                k = 0
                break
            if reversedDigits[i] == 9:
                reversedDigits[i] = 0
        if k == 1:
            reversedDigits.append(1)
        return reversedDigits[::-1]

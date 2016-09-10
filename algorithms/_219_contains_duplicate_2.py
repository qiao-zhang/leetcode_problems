from collections import Counter
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k <= 0:
            return False
        ctr = Counter(nums)
        mode, maxCount = ctr.most_common(1)[0]
        if maxCount <= 1:
            return False
        windowWidth = k + 1
        windowNum = len(nums) / windowWidth if len(nums) % windowWidth == 0 else len(nums) / windowWidth + 1
        if maxCount > windowNum:
            return True
        candidates = [n for n in ctr if ctr[n] > 1]
        lastOccurrences = dict.fromkeys(candidates, -float('inf'))
        for i, n in enumerate(nums):
            if n not in candidates:
                continue
            if i - lastOccurrences[n] <= k:
                return True
            lastOccurrences[n] = i
        return False

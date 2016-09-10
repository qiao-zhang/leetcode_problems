from heapq import _heapify_max
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [e for e, c in Counter(nums).most_common(k)]

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        C = {}
        for num in nums1:
            if num not in C:
                C[num] = 0
            C[num] += 1
        def helper():
            for num in nums2:
                if num not in C or C[num] is 0:
                    continue
                yield num
                C[num] -= 1
        return list(helper())

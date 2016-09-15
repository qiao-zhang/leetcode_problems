class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def solveUsingLib():
            return [list(p) for p in itertools.permutations(nums)]

        def solve(iter):
            if not iter: return
            if len(iter) == 1: yield [iter[0]]
            for i, n in enumerate(iter):
                newIter = iter[:i] + iter[i+1:]
                for perm in solve(newIter):
                    yield [n] + perm

        return list(solve(nums))

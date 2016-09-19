class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def solveUsingLibrary():
            return [list(perm) for perm in itertools.permutations(nums)]

        def solveRecursively():
            def helper(nums=nums):
                if not nums: yield []
                for i, num in enumerate(nums):
                    for lst in solveDFS(nums[:i] + nums[i+1:]):
                        yield [num] + lst

        return solveRecursively()

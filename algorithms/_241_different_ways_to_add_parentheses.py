class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def solveRecursively():
            tokens = re.split('(\D)', input)
            nums = map(int, tokens[::2])
            ops = map({'*': operator.mul, '+': operator.add, '-': operator.sub}.get, tokens[1::2])
            def helper(lo=0, hi=len(nums)-1):
                if lo == hi:
                    yield nums[hi]
                    return
                for i in range(lo, hi):
                    for n1 in helper(lo, i):
                        for n2 in helper(i+1, hi):
                            yield ops[i](n1, n2)
            return list(helper())
        return solveRecursively()
                

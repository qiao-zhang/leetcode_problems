class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        def recArea(A, B, C, D):
            return (C - A) * (D - B)
        # one = {'left': A, 'bottom': B, 'right': C, 'top': D}
        # two = {'left': E, 'bottom': F, 'right': G, 'top': H}
        one, two = [A, B, C, D], [E, F, G, H]
        exW = max(0, min(one[2], two[2]) - max(one[0], two[0]))
        exH = max(0, min(one[3], two[3]) - max(one[1], two[1]))
        return recArea(*one) + recArea(*two) - exW * exH

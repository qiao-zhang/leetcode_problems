# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val == q.val:
            return p
        small, big = (p, q) if p.val < q.val else (q, p)
        def helper(r, s, b):
            if r.val < s.val:
                return helper(r.right, s, b)
            if r.val > b.val:
                return helper(r.left, s, b)
            return r
        return helper(root, small, big)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def solveRecursively():
            def helper(node=root):
                if not node: return 0, 0
                lw, lo = helper(node.left)
                rw, ro = helper(node.right)
                return node.val + lo + ro, max(lw, lo) + max(rw, ro)
            return max(helper())
        return solveRecursively()

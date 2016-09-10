# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkBalanced(node):
            if node is None:
                return (0, True)
            lH, lB = checkBalanced(node.left)
            if not lB:
                return (None, False)
            rH, rB = checkBalanced(node.right)
            if not rB:
                return (None, False)
            return (max(lH, rH) + 1, abs(lH - rH) <= 1)
        _, b = checkBalanced(root)
        return b

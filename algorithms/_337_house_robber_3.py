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
        def postorder(node):
            if not node:
                return 0, 0
            left, right = postorder(node.left), postorder(node.right)
            return node.val + left[1] + right[1], max(left) + max(right)
        return max(postorder(root))

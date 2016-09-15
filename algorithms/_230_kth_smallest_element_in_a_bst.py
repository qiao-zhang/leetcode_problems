# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from itertools import islice

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: str
        :rtype: int
        """
        return next(islice(self.inorder(root), k-1, k))

    def inorder(self, root):
        if root:
            for val in self.inorder(root.left):
                yield val
            yield root.val
            for val in self.inorder(root.right):
                yield val

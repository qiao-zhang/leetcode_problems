# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        Q = deque([(root, root.val)])
        while Q:
            node, length = Q.popleft()
            if node.left is None and node.right is None:
                if length == sum:
                    return True
            if node.left is not None:
                Q.append((node.left, length + node.left.val))
            if node.right is not None:
                Q.append((node.right, length + node.right.val))
        return False

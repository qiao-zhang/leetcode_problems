from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        Q = deque([(root, 0)])
        while Q:
            node, depth = Q.popleft()
            if node.left is None and node.right is None:
                return depth + 1
            if node.left is not None:
                Q.append((node.left, depth + 1))
            if node.right is not None:
                Q.append((node.right, depth + 1))

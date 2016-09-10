# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        def stringifyPath(path):
            return '->'.join(str(node.val) for node in path)
        if root is None:
            return []
        Q, paths = deque([[root]]), []
        while Q:
            path = Q.popleft()
            if path[-1].left is None and path[-1].right is None:
                paths.append(path)
            if path[-1].left:
                Q.append(path + [path[-1].left])
            if path[-1].right:
                Q.append(path + [path[-1].right])
        return [stringifyPath(path) for path in paths]

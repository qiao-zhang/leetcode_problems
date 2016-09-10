# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def helper(node):
            if node is None:
                return deque()
            res = deque([[node.val]])
            L = helper(node.left)
            R = helper(node.right)
            while len(L) is not 0 and len(R) is not 0:
                res.append(L.popleft() + R.popleft())
            if len(L) == 0:
                res.extend(R)
            if len(R) == 0:
                res.extend(L)
            return res
        res = helper(root)
        return list(res)[::-1]

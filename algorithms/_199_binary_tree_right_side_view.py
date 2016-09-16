# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def solveIteratively():
            res, cur, i, stack = [], root, 0, []
            while True:
                while cur:
                    stack.append((cur, i))
                    if i == len(res):
                        res.append(cur.val)
                    cur, i = cur.right, i + 1
                if not stack: break
                node, level = stack.pop()
                if node.left:
                    cur = node.left
                    i = level + 1
            return res
        return solveIteratively()

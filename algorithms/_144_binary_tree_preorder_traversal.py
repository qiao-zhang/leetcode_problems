# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def solveIteratively():
            cur, stack, res = root, [], []
            while True:
                while cur:
                    res.append(cur.val)
                    stack.append(cur)
                    cur = cur.left
                if not stack: break
                node = stack.pop()
                cur = node.right
            return res
        return solveIteratively()

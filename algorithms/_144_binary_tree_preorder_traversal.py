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
            def helper():
                cur, stack = root, []
                while True:
                    while cur:
                        yield cur.val
                        stack.append(cur)
                        cur = cur.left
                    if not stack: break
                    cur = stack.pop().right
            return list(helper())
        return solveIteratively()

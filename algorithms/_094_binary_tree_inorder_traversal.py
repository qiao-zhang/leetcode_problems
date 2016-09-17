# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorderIterWithGen(root=root):
            def helper():
                cur, stack = root, []
                while True:
                    while cur:
                        stack.append(cur)
                        cur = cur.left
                    if not stack: break
                    node = stack.pop()
                    yield node.val
                    cur = node.right
            return list(helper())
        return inorderIterWithGen()

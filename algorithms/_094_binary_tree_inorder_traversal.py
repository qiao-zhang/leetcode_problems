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
        cur, res, stack = root, [], []
        while True:
            while cur:
                stack.append(cur)
                cur = cur.left
            if not stack: break
            node = stack.pop()
            res.append(node.val)
            cur = node.right
        return res

    def inorderTraversalRec(self, root):
        if not root:
            return []
        return self.inorderTraversalRec(root.left) +\
            [root.val] +\
            self.inorderTraversalRec(root.right)

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
        if not root:
            return []
        l = root.left
        r = root.right
        return self.inorderTraversal(l) + [root.val] + self.inorderTraversal(r)

    def preorderTraversal(self, root):
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) +\
            self.preorderTraversal(root.r)

    def postorderTraversal(self, root):
        if not root:
            return []
        return self.postorderTraversal(root.left) +\
            self.postorderTraversal(root.right) + [root.val]

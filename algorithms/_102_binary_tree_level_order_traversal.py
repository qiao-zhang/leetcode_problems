# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        T, Q = [], [root]
        while Q:
            T.append([node.val for node in Q])
            nextLvl = []
            for node in Q:
                if node.left is not None:
                    nextLvl.append(node.left)
                if node.right is not None:
                    nextLvl.append(node.right)
            Q = nextLvl
        return T

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
        def solveBFS():
            if not root: return []
            res, level = [], [root]
            while level:
                res.append(level[-1].val)
                level = [kid for node in level for kid in (node.left, node.right) if kid]
            return res

        def solveDFSIteratively():
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

        def solveDFSRecursively():
            res = []
            def helper(node=root, depth=0):
                if not node: return
                if depth == len(res):
                    view.append(node.val)
                helper(node.right, depth+1)
                helper(node.left, depth+1)
            helper()
            return res
        return solveDFSRecursively()

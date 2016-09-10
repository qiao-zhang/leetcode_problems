# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def traverse(node, order):
            assert order == 'left' or order == 'right'
            if node is None:
                yield None
                return
            yield node.val
            if order == 'left':
                for v in traverse(node.left, order):
                    yield v
                for v in traverse(node.right, order):
                    yield v
            else:
                for v in traverse(node.right, order):
                    yield v
                for v in traverse(node.left, order):
                    yield v

        if root is None:
            return True
        l, r = traverse(root.left, 'left'), traverse(root.right, 'right')
        sentinel = object()
        for vl in l:
            vr = next(r, sentinel)
            if vl != vr:
                return False
        vr = next(r, sentinel)
        if vr is not sentinel:
            return False
        return True

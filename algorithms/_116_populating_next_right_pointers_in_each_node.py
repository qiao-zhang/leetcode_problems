# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        parent = root
        while parent and parent.left:
            kid = parent.left
            while parent:
                parent.left.next = parent.right
                if parent.next:
                    parent.right.next = parent.next.left
                parent = parent.next
            parent = kid

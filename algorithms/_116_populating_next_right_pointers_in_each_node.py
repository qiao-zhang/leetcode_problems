# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        parent = root
        while parent and parent.left:
            kid = parent.left
            while parent.next:
                parent.left.next = parent.right
                parent.right.next = parent.next.left
                parent = parent.next
            parent.left.next = parent.right
            parent = kid

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
        if not root: return
        head, nextHead = root, root.left
        while nextHead:
            while head.next:
                head.left.next = head.right
                head.right.next = head.next.left
                head = head.next
            head.left.next = head.right
            head, nextHead = nextHead, nextHead.left

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def helper(head):
            if head is None or head.next is None:
                return head, head
            newHead, newTail = helper(head.next)
            newTail.next = head
            head.next = None
            return newHead, head
        newHead, tail = helper(head)
        return newHead

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            cur, mv = head, head.next
            while mv:
                if mv.val != cur.val:
                    cur.next = mv
                    cur = mv
                mv = mv.next
            cur.next = None
        return head

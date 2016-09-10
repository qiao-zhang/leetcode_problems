# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def reverseLL(head):
            pre, cur = None, head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre, cur = cur, nxt
            return pre

        def lengthOfLL(head):
            cur, length = head, 0
            while cur:
                length += 1
                cur = cur.next
            return length

        if headA is None or headB is None:
            return None
        lenA, lenB = lengthOfLL(headA), lengthOfLL(headB)
        headS, headL = headA, headB
        if lenA > lenB:
            headS, headL = headB, headA
        tailS = reverseLL(headS)
        cur = headL
        while cur.next:
            cur = cur.next
        if cur is not headS:
            reverseLL(tailS)
            return None
        n = (lenA + lenB - lengthOfLL(headL) - 1) / 2
        intersection = tailS
        while n > 0:
            intersection = intersection.next
            n -= 1
        reverseLL(tailS)
        return intersection

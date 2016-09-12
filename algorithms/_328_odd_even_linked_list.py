# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        odd, evenHead, even = head, head.next, head.next
        while odd and even:
            if even.next:
                odd.next = even.next
                odd = odd.next
            else:
                break
            if odd.next:
                even.next = odd.next
                even = even.next
            else:
                break
        even.next = None
        odd.next = evenHead
        return head

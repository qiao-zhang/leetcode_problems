# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        v = id(head)
        next_ = head.next
        while next_:
            if next_.val == v:
                return True
            next_.val = v
            next_ = next_.next
        return False

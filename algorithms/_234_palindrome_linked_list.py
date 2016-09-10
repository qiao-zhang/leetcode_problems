# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def lengthOfLL(head):
            cur, length = head, 0
            while cur:
                length += 1
                cur = cur.next
            return length

        def reverseLL(head):
            pre, cur = None, head
            while cur:
                nxt = cur.next
                cur.next = pre
                pre, cur = cur, nxt
            return pre

        length = lengthOfLL(head)
        if length <= 1:
            return True
        mid = head
        for _ in range(length // 2):
            mid = mid.next
        tail, palindrome = reverseLL(mid), True
        beg, end = head, tail
        while beg and end:
            if beg.val != end.val:
                palindrome = False
                break
            beg, end = beg.next, end.next
        reverseLL(mid)
        return palindrome

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from random import randrange

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.length = 1
        while head.next:
            head = head.next
            self.length += 1
        self.tail = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        steps = randrange(0, self.length)
        dest = self.head
        for _ in range(steps):
            dest = dest.next
        return dest.val



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

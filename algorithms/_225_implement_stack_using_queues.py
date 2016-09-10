from collections import deque
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main = deque()
        self.secondary = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.main.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        assert len(self.main) > 0
        while len(self.main) > 1:
            self.secondary.append(self.main.popleft())
        self.main.popleft()
        self.main, self.secondary = self.secondary, self.main

    def top(self):
        """
        :rtype: int
        """
        assert len(self.main) > 0
        return self.main[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.main) == 0

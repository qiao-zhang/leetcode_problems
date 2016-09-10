class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main = []
        self.reversed = []

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
        if self.reversed:
            self.reversed.pop()
            return
        while len(self.main) > 1:
            self.reversed.append(self.main.pop())
        self.main.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.reversed:
            return self.reversed[-1]
        return self.main[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.main and not self.reversed

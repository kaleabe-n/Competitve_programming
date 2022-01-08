class MyQueue(object):

    def __init__(self):
        self.mainList = []
        self.otherList = []

    def push(self, x):
        self.mainList.append(x)
        """
        :type x: int
        :rtype: None
        """

    def pop(self):
        for i in range(len(self.mainList)):
            self.otherList.append(self.mainList.pop())
        front = self.otherList.pop()
        for i in range(len(self.otherList)):
            self.mainList.append(self.otherList.pop())
        return front
        """
        :rtype: int
        """

    def peek(self):
        for i in range(len(self.mainList)):
            self.otherList.append(self.mainList.pop())
        front = self.otherList[-1]
        for i in range(len(self.otherList)):
            self.mainList.append(self.otherList.pop())
        return front
        """
        :rtype: int
        """

    def empty(self):
        if len(self.mainList) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

class MinStack(object):    ##failed on negative numbers

    def __init__(self):
        self.stack=[]
        self.minimum=None
    def push(self, val):
        self.stack.append(val)
        if self.minimum==None or val<self.minimum:
            self.minimum=val
        """
        :type val: int
        :rtype: None
        """

    def pop(self):
        if len(self.stack)==0:
            return None
        temp=self.stack.pop()
        if self.minimum==temp:
            if len(self.stack)==0:
                self.minimum=None
            else:
                self.minimum=self.stack[0]
                for i in self.stack:
                    if self.minimum>i:
                        self.minimum=i
        return temp
        """
        :rtype: None
        """

    def top(self):
        if len(self.stack)==0:
            return None
        return self.stack[-1]
        """
        :rtype: int
        """

    def getMin(self):
        if len(self.stack)==0:
            return None
        return self.minimum
        """
        :rtype: int
        """
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class RecentCounter(object):
    

    def __init__(self):
        self.calls =[]
        

    def ping(self, t):
        self.calls.append(t)
        num = t-3000
        for i in range(len(self.calls)):
            if self.calls[0] < num:
                self.calls.pop(0)
            elif self.calls[0] >= num:
                return len(self.calls)
        """
        :type t: int
        :rtype: int
        """

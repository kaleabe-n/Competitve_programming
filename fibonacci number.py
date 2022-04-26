class Solution(object):
    fibDict = {}
    def fib(self, n):
        if n in self.fibDict:
            return self.fibDict[n]
        elif n>1:
            temp = self.fib(n-1)+self.fib(n-2)
            self.fibDict[n] = temp
            return temp
        elif n==1:
            return 1
        elif n==0:
            return 0
        """
        :type n: int
        :rtype: int
        """
        

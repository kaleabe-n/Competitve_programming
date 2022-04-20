class Solution(object):
    def isPowerOfFour(self, n):
        if n>1:
            return self.isPowerOfFour(n/4.0)
        elif n==1:
            return True
        else:
            return False
        """
        :type n: int
        :rtype: bool
        """
        

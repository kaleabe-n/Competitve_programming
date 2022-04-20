class Solution(object):
    def isPowerOfThree(self, n):
        if n>1:
            return self.isPowerOfThree(n/3.0)
        elif n==1:
            return True
        else:
            return False
        """
        :type n: int
        :rtype: bool
        """
        

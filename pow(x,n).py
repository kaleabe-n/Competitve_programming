class Solution(object):
    def myPow(self, x, n):
        def power(num,exp):
            if exp<10:
                return num**exp
            else:
                if exp%2 == 0:
                    return power(num,exp/2)**2
                else:
                    return power(num,exp//2)**2*num
        return power(x,n)
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        

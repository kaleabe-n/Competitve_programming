class Solution(object):
    def fib(self, n):
        return dpfunc(n,{0:0,1:1})
        """
        :type n: int
        :rtype: int
        """

def dpfunc(n,di):
    if n in di:
        return di[n]
    else:
        return dpfunc(n-1,di)+dpfunc(n-2,di)

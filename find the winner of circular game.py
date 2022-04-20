class Solution(object):
    def findTheWinner(self, n, k):
        l = list(range(1,n+1))
        current = 0
        while len(l)>1:
            current = (current-1+k)%len(l)
            l.pop(current)
        return l[0]
        """
        :type n: int
        :type k: int
        :rtype: int
        """

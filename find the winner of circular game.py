class Solution(object):
    def findTheWinner(self, n, k):
        def find(arr,k,curr):
                if len(arr) == 1:
                    return arr[0]
                curr = (curr + k - 1)%len(arr)
                arr.pop(curr)
                return find(arr,k,curr)
        
        return find(list(range(1,n+1)),k,0)
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        

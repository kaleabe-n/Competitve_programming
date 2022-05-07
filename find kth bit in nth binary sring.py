class Solution(object):
    def findKthBit(self, n, k):
        def recur(n):
            if n==1:
                return "0"
            else:
                temp = recur(n-1)
                temp2 = ""
                for i in temp:
                    if i=="0":
                        temp2+="1"
                    else:
                        temp2+="0"
                return temp + "1" + temp2[::-1]
        ans = recur(n)
        return ans[k-1]
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        

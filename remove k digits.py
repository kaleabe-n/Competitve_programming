class Solution(object):
    def removeKdigits(self, num, k):
        sta = []
        nums = list(num)
        for i in nums:
            if len(sta)==0 or i >= sta[-1]:
                sta.append(i)
            else:
                while k>0 and len(sta)>0:
                    if sta[-1]>i:
                        sta.pop()
                        k-=1
                    else:
                        break
                sta.append(i)
        for i in range(k):
            if len(sta)!=0:
                sta.pop()
        ans = ""
        for i in sta:
            ans+=i
        ans = ans.lstrip("0")
        if ans == "":
            return "0"
        return ans
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        

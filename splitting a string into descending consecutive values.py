class Solution:
    def splitString(self, s: str) -> bool:
        return helper(None,s,0)
        
def helper(prev,s,start):
    if start>=len(s):
        if prev != int(s):
            return True
        return False
    for i in range(start,len(s)):
        if prev is None or int(s[start:i+1]) == prev-1:
            ans = helper(int(s[start:i+1]),s,i+1)
            if ans:
                return True
            

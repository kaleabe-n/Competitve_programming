class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = collections.Counter(s)
        for i in t:
            if s[i] == 0:
                return i
            else:
                s[i]-=1
                
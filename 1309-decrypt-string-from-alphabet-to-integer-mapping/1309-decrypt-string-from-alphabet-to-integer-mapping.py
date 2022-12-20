class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        ans = []
        while i<len(s):
            if i+2<len(s) and s[i+2] == "#":
                ans.append(chr(ord('a')+int(s[i]+s[i+1])-1))
                i+=3
            else:
                ans.append(chr(ord('a')-1+int(s[i])))
                i+=1
        return "".join(ans)
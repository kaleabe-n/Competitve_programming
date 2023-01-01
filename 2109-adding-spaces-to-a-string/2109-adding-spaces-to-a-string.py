class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        j = 0
        k = 0
        ans = []
        
        for i in range(len(s)):
            if j<len(spaces) and k<len(s) and i == spaces[j]:
                ans.append(" ")
                ans.append(s[i])
                j+=1
            else:
                ans.append(s[i])
                k+=1
                
        return "".join(ans)
        
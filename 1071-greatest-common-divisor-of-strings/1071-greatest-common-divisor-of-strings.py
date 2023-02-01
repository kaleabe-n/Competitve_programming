class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = []
        for i in range(min(len(str1),len(str2))):
            if str1[i] == str2[i]:
                ans.append(str1[i])
            else:
                break
        finalAns = ""
        if len(ans) > 0:
            for i in range(1,len(ans)+1):
                temp = "".join(ans[:i])
                count = len(str1) // (i)
                if temp * count != str1:
                    continue
                count = len(str2) // (i)
                if temp * count != str2:
                    continue
                finalAns = temp
        return finalAns
            
                    
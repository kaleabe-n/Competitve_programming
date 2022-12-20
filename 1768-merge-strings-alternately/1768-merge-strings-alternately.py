class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        maxLen = max(len(word1),len(word2))
        ans = []
        for i in range(maxLen):
            if i<len(word1):
                ans.append(word1[i])
            if i<len(word2):
                ans.append(word2[i])
        return "".join(ans)
        
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        ans = []
        for word in words:
            dp = [[""]]
            for i in range(len(word)):
                newPossibilities = []
                for j in range(len(dp)):
                    dp[j][-1] += word[i]
                    if dp[j][-1] in wordSet:
                        new = dp[j].copy()
                        new.append("")
                        newPossibilities.append(new)
                        
                dp.extend(newPossibilities)
                        
            for li in dp:
                if len(li)>2 and li[-1] == "":
                    ans.append(word)
                    break
            
        return ans
                    
                        
                
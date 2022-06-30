class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = []
        maxLen = 0
        for i in s:
            if i in letters:
                ind = letters.index(i)
                letters = letters[ind+1:]
                letters.append(i)
            else:
                letters.append(i)
            maxLen = max(maxLen,len(letters))
        return maxLen
            
        

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        leftCount = 0
        rightCount = 0
        ans = float('-inf')
        for i in range(len(s)):
            if i<k-1:
                rightCount+= 1 if s[i] in vowels else 0
            else:
                if i != k-1:
                    leftCount+= 1 if s[i-k] in vowels else 0
                rightCount+=1 if s[i] in vowels else 0
                ans = max(ans,rightCount-leftCount)
        return ans
        
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        leftCount = 0
        rightCount = 0
        for i in range(len(s)):
            if isVowel(s[i].lower()) and i<len(s)/2:
                leftCount+=1
            elif isVowel(s[i].lower()) and i>=len(s)/2:
                rightCount+=1
        return leftCount == rightCount
        
def isVowel(ch):
    return ch in ('a,e,i,o,u')
class Solution:
    def countVowels(self, word: str) -> int:
        vowels = "aeiou"
        curr = 1 if word[0] in vowels else 0
        ans  = curr
        for i in range(1,len(word)):
            if word[i] in vowels:
                curr = curr+i+1
            ans+=curr
        return ans
        
            
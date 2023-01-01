class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False
        letter = {}
        words = {}
        for i in range(len(s)):
            if s[i] in words and words[s[i]] != pattern[i]:
                return False
            if pattern[i] in letter and letter[pattern[i]] != s[i]:
                return False
            if s[i] not in words:
                words[s[i]] = pattern[i]
            if pattern[i] not in letter:
                letter[pattern[i]] = s[i]
        
        return True
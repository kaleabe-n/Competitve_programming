class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = [0] * 26
        for letter in s1:
            s1Count[ord(letter)-ord('a')] += 1
        window = [0] * 26
        i = 0
        for j in range(len(s2)):
            window[ord(s2[j])-ord('a')] += 1
            if j + 1 > len(s1):
                window[ord(s2[i])-ord('a')] -= 1
                i+=1
            for k in range(26):
                if window[k] != s1Count[k]:
                    break
            else:
                return True
        return False
        
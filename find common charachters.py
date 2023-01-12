class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        prevCount = [float("inf")] * 26
        letters = []
        aOrd = ord('a')
        for word in words:
            newCount = [0] * 26
            for letter in word:
                ind = ord(letter) - aOrd
                newCount[ind] += 1
            for i in range(26):
                prevCount[i] = min(prevCount[i], newCount[i])
        for i in range(26):
            for j in range(prevCount[i]):
                letters.append(chr(aOrd + i))
        
        return letters

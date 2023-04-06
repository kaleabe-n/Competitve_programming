class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bit_rep = {}
        ans = 0
        for word in words:
            wordSet = set(word)
            mask = 1
            bit = 0
            for i in range(26):
                if chr(i+ord('a')) in wordSet:
                    bit+=mask
                mask<<=1

            bit_rep[word] = bit

        for i in range(len(words)):
            word1 = bit_rep[words[i]]
            for j in range(i+1,len(words)):     
                word2 = bit_rep[words[j]]
                if not word1 & word2:
                    ans = max(ans,(len(words[i]) * len(words[j])))

        return ans

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = lambda x:[len(x),x])
        trie = {}
        maxx = ""
        for word in words:
            curr = trie
            for i,letter in enumerate(word):
                if letter in curr:
                    curr = curr[letter]
                else:
                    if i<len(word)-1:
                        break
                    else:
                        curr[letter] = {}
            else:
                maxx = max(maxx,word,key=lambda x:len(x))
        return maxx
                

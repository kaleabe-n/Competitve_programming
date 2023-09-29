class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = {}
        ans = []
        for word in words:
            addHelper(0,trie,word)
        for word in words:
            currDict = trie
            summ = 0
            for letter in word:
                val,di = currDict[letter]
                currDict = di
                summ+=val
            ans.append(summ)
        return ans
def addHelper(ind,dictionary,word):
    if ind == len(word)-1:
        if word[ind] in dictionary:
            dictionary[word[ind]][0] += 1
        else:
            dictionary[word[ind]] = [1,{}]
    else:
        if word[ind] in dictionary:
            dictionary[word[ind]][0]+=1
            addHelper(ind+1,dictionary[word[ind]][1],word)
        else:
            newDict = {}
            dictionary[word[ind]] = [1,newDict]
            addHelper(ind+1,newDict,word)

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = {}
        for word in words:
            addHelper(0,trie,word)
        return helper(0,s,trie,self)
        
def helper(i,word,dictionary,obj):
    total = 0
    for j in range(i,len(word)):
        if not dictionary:
            break
        if word[j] in dictionary:
            total += dictionary[word[j]][0]
            total += helper(j+1,word,dictionary[word[j]][1],obj)
            dictionary.pop(word[j])
    return total
        
        

def addHelper(ind,dictionary,word):
    if ind == len(word)-1:
        if word[ind] in dictionary:
            dictionary[word[ind]][0] += 1
        else:
            dictionary[word[ind]] = [1,{}]
    else:
        if word[ind] in dictionary:
            addHelper(ind+1,dictionary[word[ind]][1],word)
        else:
            newDict = {}
            dictionary[word[ind]] = [0,newDict]
            addHelper(ind+1,newDict,word)

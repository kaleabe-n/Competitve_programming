class MapSum:

    def __init__(self):
        self.trie = {}

    def insert(self, key: str, val: int) -> None:
        addHelper(0,self.trie,key,val)
        

    def sum(self, prefix: str) -> int:
        curr = self.trie
        summ = 0
        for letter in prefix:
            if letter in curr:
                _,summ,curr = curr[letter]
            else:
                return 0
        return summ
            

def addHelper(i,trie,word,val):
    if i == len(word)-1:
        if word[i] in trie:
            prev,down,downTrie = trie[word[i]]
            down = down-prev+val
            trie[word[i]][0] = val
            trie[word[i]][1] = down
            return prev
        else:
            trie[word[i]] = [val,val,{}]
            return 0
    else:
        if word[i] in trie:
            toSub = addHelper(i+1,trie[word[i]][2],word,val)
            trie[word[i]][1]+=val-toSub
            return toSub
        else:
            newDict = {}
            trie[word[i]] = [0,val,newDict]
            addHelper(i+1,newDict,word,val)
            return 0

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

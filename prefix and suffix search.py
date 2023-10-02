class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = {}
        for j,word in enumerate(words):
            for i in range(len(word)+1):
                curr = word[i:] + "{" + word
                addHelper(0,curr,self.trie,j)
                
    def f(self, pref: str, suff: str) -> int:
        curr = self.trie
        for letter in suff:
            if letter in curr:
                curr = curr[letter][1]
            else:
                return -1
        if "{" in curr:
            curr = curr["{"][1]
        else:
            return -1
        prev,prevLet = None,None
        for letter in pref:
            if letter in curr:
                prev = curr
                prevLet = letter
                curr = curr[letter][1]
            else:
                return -1
        maxx = prev[prevLet][0] if prev[prevLet][0] is not None else -1
        for letter in curr:
            stack = [[letter,curr]]
            if curr[letter][0] is not None:
                maxx = max(maxx,curr[letter][0])
            while stack:
                node,di = stack.pop()
                if di[node][0] is not None:
                    maxx = max(maxx,di[node][0])
                for n in di[node][1]:
                    stack.append([n,di[node][1]])
        return maxx
        

        
def addHelper(i,word,trie,index):
    if word[i] in trie:
        if i == len(word)-1:
            trie[word[i]][0] = index
            return
        addHelper(i+1,word,trie[word[i]][1],index)
    else:
        trie[word[i]] = [None,{}]
        if i == len(word)-1:
            trie[word[i]][0] = index
            return
        addHelper(i+1,word,trie[word[i]][1],index)
        

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)

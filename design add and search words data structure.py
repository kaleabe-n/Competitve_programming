class WordDictionary:

    def __init__(self):
        self.dict = {}

    def addWord(self, word: str) -> None:
        addHelper(0,self.dict,word)

    def search(self, word: str) -> bool:
        return searchHelper(0,self.dict,word)
        
    
def addHelper(ind,dictionary,word):
    if ind == len(word)-1:
        if word[ind] in dictionary:
            dictionary[word[ind]][0] = True
        else:
            dictionary[word[ind]] = [True,{}]
    else:
        if word[ind] in dictionary:
            addHelper(ind+1,dictionary[word[ind]][1],word)
        else:
            newDict = {}
            dictionary[word[ind]] = [False,newDict]
            addHelper(ind+1,newDict,word)

def searchHelper(ind,dictionary,word):
    if word[ind] == '.':
        if ind == len(word)-1:
            for letter in dictionary:
                if dictionary[letter][0]:
                    return True
            return False
        else:
            ans = False
            for letter in dictionary:
                ans = ans or searchHelper(ind+1,dictionary[letter][1],word)
            return ans
    elif ind == len(word)-1:
        if word[ind] in dictionary:
            return dictionary[word[ind]][0]
        else:
            return False
    else:
        if word[ind] in dictionary:
            return searchHelper(ind+1,dictionary[word[ind]][1],word)
        else:
            return False
    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

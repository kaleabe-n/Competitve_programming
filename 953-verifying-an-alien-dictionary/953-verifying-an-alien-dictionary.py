class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {}
        maxLen = len(max(words,key = lambda x:len(x)))
        for i in range(len(order)):
            index[order[i]] = i
        orderedInds = set()
        for i in range(maxLen):
            if i<len(words[0]):
                temp = words[0][i]
            else:
                temp = ""
            for j in range(1,len(words)):
                if j in orderedInds:
                    continue
                if temp != "" and i>=len(words[j]):
                    return False
                elif temp == "":
                    continue
                elif i>=len(words[j]):
                    temp = ""
                elif index[words[j][i]] < index[temp]:
                    return False
                elif index[words[j][i]] == index[temp]:
                    temp = words[j][i]
                elif index[words[j][i]] > index[temp]:
                    orderedInds.add(j)
                    temp = words[j][i]
                
        return True
                
                
                
                
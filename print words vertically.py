class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        longest = max(words,  key = lambda x:len(x))
        maxWordLen = len(longest)
        wordsVertical = [[] for i in range(maxWordLen)]
        wordsVerticalString = []
        
        #consturct array of the words vertically
        for word in words:
            for index in range(maxWordLen):
                if index < len(word):
                    wordsVertical[index].append(word[index])
                else:
                    wordsVertical[index].append(" ")
        
        #change the words to string
        for word in wordsVertical:
            wordsVerticalString.append("".join(word))
            
        #remove trailing spaces
        for index in range(len(wordsVerticalString)):
            wordsVerticalString[index] = wordsVerticalString[index].rstrip(" ")
        
        return wordsVerticalString
            

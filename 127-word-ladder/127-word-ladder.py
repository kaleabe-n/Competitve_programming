from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList = set(wordList)
        curr = beginWord
        que = deque()
        que.append([curr,0])
        visited = set()
        visited.add(curr)
        letters = [chr(ord('a')+i) for i in range(26)]
        while que:
            curr,count = que.popleft()
            if curr == endWord:
                return count+1
            for i in range(len(curr)):
                for j in letters:
                    if curr[:i]+j+curr[i+1:] in wordList and curr[:i]+j+curr[i+1:] not in visited:
                        que.append([curr[:i]+j+curr[i+1:],count+1])
                        visited.add(curr[:i]+j+curr[i+1:])
        return 0
        
                
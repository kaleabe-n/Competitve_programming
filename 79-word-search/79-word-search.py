class Solution(object):
    def exist(self, board, word):
        initial = []
        for j in range(len(board)):
            for i in range(len(board[j])):
                if board[j][i] == word[0]:
                    initial.append([j,i])
        if len(word) == 1 and len(initial)>0:
            return True
        elif len(word) == 1 and len(initial) == 0:
            return False
        for location in initial:
            ans = dfs(board,word,1,location,[location])
            if ans is not None and ans == True:
                return True
        return False
                        
                    
                
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
def dfs(board,word,wordInd,location,visited):
    for i in neighbours(location,board):
        if len(word) == wordInd+1 and board[i[0]][i[1]] == word[wordInd] and i not in visited:
            return True
        elif len(word) == wordInd+1:
            pass
        elif board[i[0]][i[1]] == word[wordInd] and i not in visited:
            temp = dfs(board,word,wordInd+1,i,visited+[i])
            if temp is not None and temp == True:
                return True
        
        
def neighbours(location,board):
    neighbours = []
    if len(board)!=location[0]+1:
        neighbours.append([location[0]+1,location[1]])
    if len(board[0])!=location[1]+1:
        neighbours.append([location[0],location[1]+1])
    if location[0]-1>=0:
        neighbours.append([location[0]-1,location[1]])
    if location[1]-1>=0:
        neighbours.append([location[0],location[1]-1])
    return neighbours

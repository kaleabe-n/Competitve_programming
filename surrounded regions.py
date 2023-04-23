class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ignored = set()
        for i in range(len(board[0])):
            dfs([0,i],ignored,board)
            if len(board)>1:
                dfs([len(board)-1,i],ignored,board)
        for i in range(1,len(board)-1):
            dfs([i,0],ignored,board)
            if len(board[0])>1:
                dfs([i,len(board[0])-1],ignored,board)
        for j in range(len(board)):
            for i in range(len(board[j])):
                if board[j][i] == "O" and tuple([j,i]) not in ignored:
                    board[j][i] = "X"
                
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
def dfs(location,ignored,board):
    ignored.add(tuple(location))
    for i in neighbours(location,len(board[0]),len(board)):
        if tuple(i) not in ignored and board[location[0]][location[1]] == "O":
            dfs(i,ignored,board)
    
def neighbours(location,rowLen,colLen):
    neighbours = []
    if location[0]-1>=0:
        neighbours.append([location[0]-1,location[1]])
    if location[0]+1<colLen:
        neighbours.append([location[0]+1,location[1]])
    if location[1]-1>=0:
        neighbours.append([location[0],location[1]-1])
    if location[1]+1<rowLen:
        neighbours.append([location[0],location[1]+1])
    return neighbours

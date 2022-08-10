from collections import defaultdict

class Solution(object):
    def updateBoard(self, board, click):
        # print(neighbours([0,0],1,1))
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = 'X'
        else:
            dfs(click,board,defaultdict(lambda:False))
        return board
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        
def dfs(location,board,visited):
    if board[location[0]][location[1]] == 'E':  
        visited[tuple(location)] = True
        toReveal = []
        mineCount = 0
        for i in neighbours(location,len(board[0]),len(board)):
            if board[i[0]][i[1]] == 'M':
                mineCount+=1
            if board[i[0]][i[1]] == 'E' and not visited[tuple([i[0],i[1]])]:
                toReveal.append(i)
        if mineCount>0:
            board[location[0]][location[1]] = str(mineCount)
        else:
            board[location[0]][location[1]] = 'B'
            for i in range(len(toReveal)-1,-1,-1):
                dfs(toReveal[i],board,visited)
        
        
def neighbours(location,rowLen,colLen):
    neighbours = []
    if location[0]-1>=0:
        neighbours.append([location[0]-1,location[1]])
    if location[1]-1>=0:
        neighbours.append([location[0],location[1]-1])
    if location[0]+1<colLen:
        neighbours.append([location[0]+1,location[1]])
    if location[1]+1<rowLen:
        neighbours.append([location[0],location[1]+1])
    if location[0]-1>=0 and location[1]-1>=0:
        neighbours.append([location[0]-1,location[1]-1])
    if location[0]+1<colLen and location[1]+1<rowLen:
        neighbours.append([location[0]+1,location[1]+1])
    if location[0]+1<colLen and location[1]-1>=0:
        neighbours.append([location[0]+1,location[1]-1])
    if location[0]-1>=0 and location[1]+1<rowLen:
        neighbours.append([location[0]-1,location[1]+1])
    return neighbours

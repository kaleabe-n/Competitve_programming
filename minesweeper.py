class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        grid = board
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        stack = [click]
        visited = set(tuple(click))
        while stack:
            x,y = stack.pop()
            if board[x][y] != "E":
                continue
            count = 0
            for i,j in directions:
                if isValid(x+i,y+j,board) and board[i+x][y+j] == "M":
                    count += 1
            if count > 0:
                board[x][y] = str(count)
            else:
                board[x][y] = "B"
                for i,j in directions:
                    if isValid(x+i,y+j,board) and (x+i,y+j) not in visited:
                        stack.append([x+i,y+j])
                        visited.add((x+i,y+j))
                        
                        
        return board
                        
        
        
def isValid(row,col,grid):
    if row>=len(grid) or row<0:
        return False
    if col>=len(grid[0]) or col<0:
        return False
    return True









# from collections import defaultdict

# class Solution(object):
#     def updateBoard(self, board, click):
#         # print(neighbours([0,0],1,1))
#         if board[click[0]][click[1]] == "M":
#             board[click[0]][click[1]] = 'X'
#         else:
#             dfs(click,board,defaultdict(lambda:False))
#         return board
#         """
#         :type board: List[List[str]]
#         :type click: List[int]
#         :rtype: List[List[str]]
#         """
        
# def dfs(location,board,visited):
#     if board[location[0]][location[1]] == 'E':  
#         visited[tuple(location)] = True
#         toReveal = []
#         mineCount = 0
#         for i in neighbours(location,len(board[0]),len(board)):
#             if board[i[0]][i[1]] == 'M':
#                 mineCount+=1
#             if board[i[0]][i[1]] == 'E' and not visited[tuple([i[0],i[1]])]:
#                 toReveal.append(i)
#         if mineCount>0:
#             board[location[0]][location[1]] = str(mineCount)
#         else:
#             board[location[0]][location[1]] = 'B'
#             for i in range(len(toReveal)-1,-1,-1):
#                 dfs(toReveal[i],board,visited)
        
        
# def neighbours(location,rowLen,colLen):
#     neighbours = []
#     if location[0]-1>=0:
#         neighbours.append([location[0]-1,location[1]])
#     if location[1]-1>=0:
#         neighbours.append([location[0],location[1]-1])
#     if location[0]+1<colLen:
#         neighbours.append([location[0]+1,location[1]])
#     if location[1]+1<rowLen:
#         neighbours.append([location[0],location[1]+1])
#     if location[0]-1>=0 and location[1]-1>=0:
#         neighbours.append([location[0]-1,location[1]-1])
#     if location[0]+1<colLen and location[1]+1<rowLen:
#         neighbours.append([location[0]+1,location[1]+1])
#     if location[0]+1<colLen and location[1]-1>=0:
#         neighbours.append([location[0]+1,location[1]-1])
#     if location[0]-1>=0 and location[1]+1<rowLen:
#         neighbours.append([location[0]-1,location[1]+1])
#     return neighbours

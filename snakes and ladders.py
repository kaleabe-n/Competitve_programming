class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        que = collections.deque([[[len(board)-1,0],0]])
        visited = set()
        visited.add((len(board)-1,0))
        rowLen = len(board[0])
        colLen = len(board)
        dest = [0, rowLen -1]
        if rowLen % 2 == 0:
            dest = [0,0]
        while que:
            curr,moves = que.popleft()
            if curr == dest:
                return moves
            #the last minus one
            lastM1 = None
            for _ in range(1,7):
                if (colLen - 1 - curr[0])%2 == 1:
                    curr[1] -= 1
                else:
                    curr[1] += 1
                if curr[1] == rowLen or curr[1] == -1:
                    curr[0]-=1
                    curr[1] = 0
                    if (colLen - 1 - curr[0])%2 == 1:
                        curr[1] = rowLen - curr[1] - 1
                if board[curr[0]][curr[1]] == -1:
                    lastM1 = list(curr)
                if curr == dest:
                    return moves+1
                if board[curr[0]][curr[1]] != -1:
                    new = board[curr[0]][curr[1]] - 1
                    row = new // rowLen
                    col = new % rowLen
                    if (row % 2) == 1:
                        col = rowLen - col -1
                    row = colLen - row - 1
                    if [row,col] == dest:
                        return moves + 1
                    if (row,col) not in visited:
                        que.append([[row,col],moves+1])
                        visited.add((row,col))
            if lastM1 and tuple(lastM1) not in visited:
                que.append([lastM1,moves+1])
        

        return -1



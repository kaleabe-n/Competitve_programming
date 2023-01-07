class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        winRowCount = 0
        winColCount = 0
        xWon = False
        oWon = False
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != " ":
                winRowCount += 1
                if board[i][0] == "X":
                    xWon = True
                if board[i][0] == "O":
                    oWon = True
            if board[0][i] == board[1][i] == board[2][i] != " ":
                winColCount += 1
                if board[0][i] == "X":
                    xWon = True
                if board[0][i] == "O":
                    oWon = True
        winCount = winRowCount + winColCount
        if board[0][0] == board[1][1] == board[2][2] != " ":
            winCount += 1
            if board[0][0] == "X":
                xWon = True
            if board[0][0] == "O":
                oWon = True
        if board[0][2] == board[1][1] == board[2][0] != " ":
            winCount += 1
            if board[0][2] == "X":
                xWon = True
            if board[0][2] == "O":
                oWon = True
        count = defaultdict(int)
        for row in board:
            for square in row:
                count[square] += 1
        if winRowCount > 1 or winColCount > 1 or winCount > 2:
            return False
        if count['X'] < count["O"] or count["X"] > count["O"] + 1 or (xWon and count["X"] == count["O"]) or (oWon and count["X"] > count["O"]):
            return False
        return True

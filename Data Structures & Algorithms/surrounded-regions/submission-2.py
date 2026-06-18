class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])

        def capture(r, c):
            if (r not in range(ROW) or c not in range(COL)
            or board[r][c] != "O"):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        
        for i in range(ROW):
            for j in range(COL):
                if (i in [0, ROW - 1] or j in [0, COL - 1]) and board[i][j] == "O":
                    capture(i, j)

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == "T":
                    board[i][j] = "O"

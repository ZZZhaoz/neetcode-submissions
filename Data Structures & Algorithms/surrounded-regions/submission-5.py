class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        
        def capture(i, j):
            if (i not in range(ROW) or j not in range(COL) or board[i][j] != "O"):
                return 
            board[i][j] = "T"
            capture(i + 1, j)
            capture(i - 1, j)
            capture(i, j + 1)
            capture(i, j - 1)
        
        for r in range(ROW):
            for c in range(COL):
                if (r == 0 or c == 0 or r == ROW - 1 or c == COL - 1) and board[r][c] == "O":
                    capture(r, c)
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "T":
                    board[r][c] = "O"
        
        
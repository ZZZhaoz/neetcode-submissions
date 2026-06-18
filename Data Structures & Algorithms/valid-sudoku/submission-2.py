class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        num = set("123456789")
        for i in range(n):
            rmap = {}
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in num:
                    return False
                if board[i][j] not in rmap:
                    rmap[board[i][j]] = 1
                else:
                    return False
        
        for i in range(n):
            cmap = {}
            for j in range(n):
                if board[j][i] == ".":
                    continue
                if board[j][i] not in num:
                    return False
                if board[j][i] not in cmap:
                    cmap[board[j][i]] = 1
                else:
                    return False

        gmap = {}
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in num:
                    return False
                r, c = i//3, j//3
                if (r, c) not in gmap:
                    gmap[(r, c)] = []
                if board[i][j] in gmap[(r, c)]:
                    return False
                gmap[(r, c)].append(board[i][j])
        
        return True


                




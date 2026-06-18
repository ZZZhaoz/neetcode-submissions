class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, s, preHeight):
            if (r not in range(ROWS) or c not in range(COLS)
            or (r, c) in s or preHeight > heights[r][c]):
                return
            s.add((r,c))
            dfs(r + 1, c, s, heights[r][c])
            dfs(r - 1, c, s, heights[r][c])
            dfs(r, c + 1, s, heights[r][c])
            dfs(r, c - 1, s, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res
        
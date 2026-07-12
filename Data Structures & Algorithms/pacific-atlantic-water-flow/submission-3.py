class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, s, preHeight):
            if (r not in range(ROW) or c not in range(COL) or heights[r][c] < preHeight or (r, c) in s):
                return 
            s.add((r, c))
            dfs(r + 1, c, s, heights[r][c])
            dfs(r - 1, c, s, heights[r][c])
            dfs(r, c - 1, s, heights[r][c])
            dfs(r, c + 1, s, heights[r][c])
        
        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COL - 1, atl, heights[r][COL - 1])

        for c in range(COL):
            dfs(0, c, pac, heights[0][c])
            dfs(ROW - 1, c, atl, heights[ROW - 1][c])
        
        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        res = []
        DIRECTION = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        def bfs(r, c):
            area = 0
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))
            area += 1
            while q:
                row, col = q.popleft()

                for rd, cd in DIRECTION:
                    r = row + rd
                    c = col + cd
                    if (r in range(ROWS) and c in range(COLS)
                    and grid[r][c] == 1 and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
                        area += 1
            res.append(area)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visit:
                    bfs(i, j)
        
        return max(res, default = 0)
        
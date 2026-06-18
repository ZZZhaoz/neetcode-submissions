class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))
            while q:
                row, col = q.popleft()

                for rd, cd in DIRECTION:
                    newr = row + rd
                    newc = col + cd
                    if (newr in range(ROWS) and newc in range(COLS) 
                    and grid[newr][newc] == "1" and (newr, newc) not in visit):
                        q.append((newr, newc))
                        visit.add((newr, newc))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visit:
                    bfs(i, j)
                    res += 1
        return res

        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                row, col = q.popleft()
                direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for rd, cd in direction:
                    r = row + rd
                    c = col + cd
                    if (r in range(ROWS) and c in range(COLS) 
                    and (r, c) not in visited and grid[r][c] == "1"):
                        visited.add((r, c))
                        q.append((r, c))
 

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    res += 1
        return res


        
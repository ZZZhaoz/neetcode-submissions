class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROW, COL = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            visited.add((i, j))

            while q:
                r, c = q.popleft()
                for rc, cc in DIRECTIONS:
                    r2 = r + rc
                    c2 = c + cc
                    if (r2 in range(ROW) and c2 in range(COL) and (r2, c2) 
                    not in visited and grid[r2][c2] == "1"):
                        visited.add((r2, c2))
                        q.append((r2, c2))
            
        islands = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        return islands
        
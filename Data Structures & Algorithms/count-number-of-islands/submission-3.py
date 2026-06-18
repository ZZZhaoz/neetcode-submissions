class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROW, COL = len(grid), len(grid[0])
        DIRCTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        islands = 0

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            visited.add((i, j))

            while q:
                r, c = q.popleft()
                for rd, cd in DIRCTION:
                    nr = r + rd
                    cr = c + cd
                    if (nr in range(ROW) and cr in range(COL)
                    and (nr, cr) not in visited and grid[nr][cr] == "1"):
                        visited.add((nr, cr))
                        q.append((nr, cr))
        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        return islands


        
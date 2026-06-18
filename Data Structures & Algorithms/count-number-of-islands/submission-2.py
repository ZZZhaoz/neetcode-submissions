class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROW, COW = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        islands = 0

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            visited.add((i, j))

            while q:
                row, col = q.popleft()
                for rd, cd in directions:
                    r = row + rd
                    c = col + cd
                    if (r in range(ROW) and c in range(COW)
                        and grid[r][c] == "1" and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        for i in range(ROW):
            for j in range(COW):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        
        return islands

        
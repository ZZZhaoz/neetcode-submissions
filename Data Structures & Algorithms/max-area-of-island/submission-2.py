class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROW, COW = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        res = []

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            visited.add((i, j))
            area = 1
            while q:
                row, col = q.popleft()
                
                for rd, cd in directions:
                    r = row + rd
                    c = col + cd
                    if (r in range(ROW) and c in range(COW)
                        and grid[r][c] == 1 and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
                        area += 1
            res.append(area)

        for i in range(ROW):
            for j in range(COW):
                if grid[i][j] == 1 and (i, j) not in visited:
                    bfs(i, j)
        
        return max(res, default=0)
        
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ROW, COL = len(grid), len(grid[0])
        res = []
        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            visited.add((i, j))
            area = 1
            while q:
                r, c = q.popleft()
                for rd, cd in directions:
                    r1 = r + rd
                    c1 = c + cd
                    if (r1 in range(ROW) and c1 in range(COL) and 
                    (r1, c1) not in visited and grid[r1][c1] == 1 ):
                        visited.add((r1, c1))
                        q.append((r1, c1))
                        area += 1
            res.append(area)
        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1 and (i, j) not in visited:
                    bfs(i, j)
        return max(res, default = 0)
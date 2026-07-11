class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return 
        
        visited = set()
        q = collections.deque()
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROW, COL = len(grid), len(grid[0])

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
        
        d = 0
        while q:

            for _ in range(len(q)):
                r1, c1 = q.popleft()
                grid[r1][c1] = d
                for rd, cd in DIRECTIONS:
                    r = r1 + rd
                    c = c1 + cd
                    if (r in range(ROW) and c in range(COL) and 
                    (r, c) not in visited and grid[r][c] == 2147483647):
                        q.append((r, c))
                        visited.add((r, c))
            d += 1
        
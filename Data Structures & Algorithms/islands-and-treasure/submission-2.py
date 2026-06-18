class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        ROW, COL = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        q = collections.deque()

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for rd, cd in directions:
                    nr, nc = r + rd, c + cd
                    if (nr in range(ROW) and nc in range(COL) and 
                    grid[nr][nc] == 2147483647 and (nr, nc) not in visited):
                        q.append((nr, nc))
                        visited.add((nr, nc))
            dist += 1

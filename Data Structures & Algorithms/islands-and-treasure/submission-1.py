class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return 0

        ROW, COW = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        q = collections.deque()

        for i in range(ROW):
            for j in range(COW):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))
                    
        dist = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = dist
                for rd, cd in directions:
                    r = row + rd
                    c = col + cd
                    if (r in range(ROW) and c in range(COW)
                        and grid[r][c] == 2147483647 and (r, c) not in visited):
                        q.append([r, c])
                        visited.add((r, c))
            dist += 1

        
        
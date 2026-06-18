class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh = 0
        q = collections.deque()

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for rd, cd in directions:
                    nr, nc = r + rd, c + cd
                    if (nr in range(ROW) and nc in range(COL) and
                    grid[nr][nc] == 1):
                        q.append((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            time += 1
        
        if fresh == 0:
            return time
        else:
            return -1
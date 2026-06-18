class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTION = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time, fresh = 0, 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        while q and fresh > 0:
            lenq = len(q)
            for i in range(lenq):
                r, c = q.popleft()
                
                for rd, cd in DIRECTION:
                    row, col = r + rd, c + cd
                    if (row in range(ROWS) and col in range(COLS) and grid[row][col] == 1):
                        q.append((row, col))
                        grid[row][col] = 2
                        fresh -= 1
            time += 1
        if fresh > 0:
            return -1
        else:
            return time

        
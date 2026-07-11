class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = collections.deque()

        fresh = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        
        time = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r1, c1 = q.popleft()
                for rd, cd in DIRECTIONS:
                    r = r1 + rd
                    c = c1 + cd
                    if ( r in range(ROW) and c in range(COL)
                    and grid[r][c] == 1):
                        q.append((r, c))
                        fresh -= 1
                        grid[r][c] = 2 
            time += 1
        if fresh != 0:
            return -1
        else:
            return time
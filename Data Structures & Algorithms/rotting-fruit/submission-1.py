class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COW = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh = 0
        time = 0
        q = collections.deque()

        for i in range(ROW):
            for j in range(COW):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))

        while fresh > 0 and q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for rd, cd in directions:
                    r = row + rd
                    c = col + cd
                    if (r in range(ROW) and c in range(COW)
                        and grid[r][c] == 1):
                        q.append((r, c))
                        grid[r][c] = 2 
                        fresh -= 1
            time += 1
        if fresh > 0:
            return -1
        return time
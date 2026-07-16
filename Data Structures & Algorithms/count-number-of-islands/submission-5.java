class Solution {
    public int numIslands(char[][] grid) {
        if (grid.length == 0) {
            return 0;
        }

        int ROW = grid.length;
        int COL = grid[0].length;

        int[][] DIRECTIONS = new int[][]{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        Set<List<Integer>> visit = new HashSet<>();

        int islands = 0;
        for (int i = 0; i < ROW; i ++){
           for (int j = 0; j < COL; j ++){
               if (grid[i][j] == '1' && !visit.contains(Arrays.asList(i, j))){
                   bfs(i, j, grid, visit, DIRECTIONS);;
                   islands++;
               }

           }
        }
        return islands;
    }

    private void bfs(int i, int j, char[][] grid, Set<List<Integer>> visit, int[][] DIRECTIONS) {
        int ROW = grid.length;
        int COL = grid[0].length;
        
        Queue<List<Integer>> queue = new LinkedList<>();
        queue.add(Arrays.asList(i, j));
        visit.add(Arrays.asList(i, j));
        while (!queue.isEmpty()) {
            List<Integer> list = queue.poll();
            int row = list.get(0);
            int col = list.get(1);
            for (int[] direction : DIRECTIONS) {
                int r = row + direction[0];
                int c = col + direction[1];
                if (r < ROW && r >= 0 && c < COL && c >= 0 && grid[r][c] == '1' && !visit.contains(Arrays.asList(r, c))) {
                    visit.add(Arrays.asList(r, c));
                    queue.add(Arrays.asList(r, c));
                }
            }
        }
    }
}

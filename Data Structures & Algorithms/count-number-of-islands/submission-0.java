class Solution {
    public int numIslands(char[][] grid) {

        if(grid == null || grid.length == 0)
            return 0;


        int count = 0;
        for(int i=0;i<grid.length;i++) {
            for(int j=0;j<grid[i].length;j++) {
                // 
                if(grid[i][j] == '1') {
                    count = count + bfs(grid, i, j);
                }
            }
        }

        return count;
    }

    public int bfs(char[][] grid, int i, int j) {
        if(Math.min(i,j) < 0 || i == grid.length || j == grid[0].length || grid[i][j] == '0') {
            return 0;
        }

        grid[i][j] = '0';

        bfs(grid, i+1, j);
        bfs(grid, i-1, j);
        bfs(grid, i, j+1);
        bfs(grid, i, j-1);

        return 1;
    }
}

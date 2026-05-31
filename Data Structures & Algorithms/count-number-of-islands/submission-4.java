class Solution {
    public int numIslands(char[][] grid) {
        
        if(grid == null || grid.length == 0)
            return 0;
        int count = 0;
        for(int i=0;i<grid.length;i++) {
            for(int j=0;j<grid[i].length;j++) {
                if(grid[i][j] == '1') {
                    count = count + dfs(grid, i,j);
                }
            }
        }

        return count;
    }
}


    public int dfs(char[][] grid, int i, int j) {
        if(Math.min(i,j) < 0 || i == grid.length || j == grid[0].length || grid[i][j] == '0') {
            return 0;
        }

        grid[i][j] = '0'; // make sure its not counted again
        
        dfs(grid, i+1, j);
        dfs(grid, i-1, j);
        dfs(grid, i, j+1);
        dfs(grid, i, j-1);

        return 1;
    }

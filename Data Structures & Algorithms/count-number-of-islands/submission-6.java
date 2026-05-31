class Solution {
    public int numIslands(char[][] grid) {
        
        int ROW = grid.length;
        int COL = grid[0].length;

        int count = 0;
        for(int r=0;r<grid.length;r++) {
            for(int c=0;c<grid[0].length;c++) {
                count = count + dfs(grid, r, c);
            }   
        }

        return count;
    }

    public int dfs(char[][] grid, int row, int col) {
        if(row < 0 || col < 0 || row >= grid.length || col >= grid[0].length || grid[row][col] == '0') {
            return 0;
        }

        grid[row][col] = '0';

        dfs(grid, row+1, col);
        dfs(grid, row-1, col);
        dfs(grid, row, col+1);
        dfs(grid, row, col-1);

        return 1;
    }
}




class Solution {
    public int countPaths(int[][] grid) {

        //int ROW = grid.length;
        //int COL = grid[0].length;

        Set<String> set = new HashSet<String>();
        return helper(grid, 0, 0, set);

    }


    public int helper(int[][] grid, int r, int c, Set<String> set) {

        if(Math.min(r,c) < 0 || r == grid.length || c == grid[0].length) 
            return 0;

        if (set.contains(r + "." + c) || grid[r][c] == 1)
            return 0;
        
        // when does it return 1
        if(r == grid.length - 1 && c == grid[0].length - 1)
            return 1;

        set.add(r + "." + c);
        int count = 0;
        count = count + helper(grid, r+1, c, set);
        count = count + helper(grid, r, c+1, set);
        count = count + helper(grid, r-1, c, set);
        count = count + helper(grid, r, c-1, set);

        set.remove(r + "." + c);

        return count;
    }
}

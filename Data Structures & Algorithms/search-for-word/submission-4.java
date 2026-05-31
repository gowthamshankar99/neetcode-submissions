class Solution {
    public boolean exist(char[][] board, String word) {

        int ROW = board.length;
        int COL = board[0].length;

        Set<String> visited = new HashSet<String>();


        for(int i=0;i<ROW;i++)  {
            for(int j=0;j<COL;j++)  {
                if(dfs(board, word, i, j, 0, visited)) 
                    return true;
        }
        }

        return false;
        
    }

    public boolean dfs(char[][] board, String word, int r, int c, int i, Set<String> set) {
        // true condition
        if(i == word.length()) 
            return true;

        // false condition 
        if(r < 0 || c < 0 || r >= board.length || c >= board[0].length || board[r][c] != word.charAt(i) || set.contains(r + "." + c)) {
            return false;
        }
        // do the visited set here 

        set.add(r + "." + c);

        // perform the dfs 

        boolean res = dfs(board, word, r+1, c, i+1, set) || dfs(board, word, r-1, c, i+1, set)  || dfs(board, word, r, c+1, i+1, set)  || dfs(board, word, r, c-1, i+1, set) ;
        
        // remove visited path 
        set.remove(r + "." + c);
        // return results
        return res;
    }
}

class Solution {
    public boolean exist(char[][] board, String word) {
        int ROW = board.length;
        int COL = board[0].length;

        Set<String> visited = new HashSet<>();

        for(int r=0;r<ROW;r++) {
            for(int c=0;c<COL;c++) {
                if(dfs(board, word, r, c,  0, visited)) {
                    return true;
                }
            }
        }

        return false;
    }


    public boolean dfs(char[][] board, String word, int r, int c, int i, Set<String> visited) {
        if(i == word.length()) {
            return true;
        }

        if(r < 0 || c < 0 || r >= board.length || c >= board[0].length || board[r][c] != word.charAt(i) || visited.contains(r + "." + c)) {
             return false;
        }

        // make the set value visited 
        visited.add(r + "." + c);

        boolean res = dfs(board, word, r+1,c, i+1, visited) || dfs(board, word, r-1,c, i+1, visited) || dfs(board, word, r,c+1, i+1, visited) || dfs(board, word, r,c-1, i+1, visited);

        // make the cell unvisited

        visited.remove(r + "." + c);
        return res;
    }
}

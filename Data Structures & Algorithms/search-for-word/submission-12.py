class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROW = len(board)
        COL = len(board[0])
        visited = set()

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0]:
                    if self.dfs(board, r,c, ROW, COL, 0, visited, word):
                        return True


        return False


    def dfs(self, board, r,c, ROW, COL, i, visited, word):



        if r < 0 or c < 0 or r >= ROW or c >= COL or (r,c) in visited or board[r][c] != word[i]:
            return False

        if i == len(word)-1:
            return True            


        visited.add((r,c))

        res = self.dfs(board, r,c+1, ROW, COL, i+1, visited, word) or self.dfs(board, r,c-1, ROW, COL, i+1, visited, word) or self.dfs(board, r+1,c, ROW, COL, i+1, visited, word) or self.dfs(board, r-1,c, ROW, COL, i+1, visited, word)

        visited.remove((r,c))

        return res


        
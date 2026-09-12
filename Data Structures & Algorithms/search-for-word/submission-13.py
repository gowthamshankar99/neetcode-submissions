class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROW = len(board)
        COL = len(board[0])
        visited = set()

        for r in range(ROW):
            for c in range(COL):
                if self.dfs(board, r,c, word, 0, visited):
                    return True

        return False



    def dfs(self, board, r,c,word, i, visited):
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r,c) in visited or board[r][c] != word[i]:
            return False


        if i == len(word)-1:
            return True

        visited.add((r,c))
        found = self.dfs(board, r+1,c,word, i+1, visited) or self.dfs(board, r,c+1,word, i+1, visited) or self.dfs(board, r-1,c,word, i+1, visited) or self.dfs(board, r,c-1,word, i+1, visited)
        visited.remove((r,c))

        return found
        







        
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        if len(grid) == 0:
            return 0

        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        count = 0
        for r in range(ROW):
            for c in range(COL):
                count += self.dfs(r,c, visited, grid, ROW, COL)

        
        return count

    def dfs(self, r, c, visited, grid, ROW, COL):
        if r >= ROW or c >= COL or r < 0 or c < 0 or (r,c) in visited or grid[r][c] == '0':
            return 0

        visited.add((r,c))

        self.dfs(r+1, c, visited, grid, ROW, COL)
        self.dfs(r-1, c, visited, grid, ROW, COL)
        self.dfs(r, c+1, visited, grid, ROW, COL)
        self.dfs(r, c-1, visited, grid, ROW, COL)

        return 1

        





        
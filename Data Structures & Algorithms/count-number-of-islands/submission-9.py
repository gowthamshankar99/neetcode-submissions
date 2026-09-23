class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        count = 0

        for r in range(ROW):
            for c in range(COL):
                count += self.dfs(r,c, ROW, COL, grid, visited)

        

        return count


    def dfs(self, r, c, ROW, COL, grid, visited):
        if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] == '0' or (r,c) in visited:
            return 0

        visited.add((r,c))

        self.dfs(r+1, c, ROW, COL, grid, visited)
        self.dfs(r-1, c, ROW, COL, grid, visited)
        self.dfs(r, c+1, ROW, COL, grid, visited)
        self.dfs(r, c-1, ROW, COL, grid, visited)

    

        return 1
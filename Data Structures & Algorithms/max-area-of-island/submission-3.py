class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        max_area = 0 
        for r in range(ROW):
            for c in range(COL):
                max_area = max(max_area, self.dfs(ROW, COL, r,c, grid, visited))

        return max_area



    def dfs(self, ROW, COL, r,c, grid, visited):
        if r < 0 or c < 0 or r >= ROW or c >= COL or grid[r][c] == 0 or (r,c) in visited:
            return 0

        visited.add((r,c))

        return 1+self.dfs(ROW, COL, r+1, c, grid, visited)+self.dfs(ROW, COL, r-1, c, grid, visited)+self.dfs(ROW, COL, r, c+1, grid, visited)+self.dfs(ROW, COL, r, c-1, grid, visited)
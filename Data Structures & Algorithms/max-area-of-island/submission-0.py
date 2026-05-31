class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        
        area = 0
        for r in range(ROW):
            for c in range(COL):
                area = max(area, self.dfs(grid, r, c, visited))
                

        return area


    def dfs(self, grid, row, col, visited):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or (row,col) in visited or grid[row][col] == 0:
            return 0
        
        visited.add((row,col))


        return 1 + self.dfs(grid, row+1, col, visited) + self.dfs(grid, row-1, col, visited) + self.dfs(grid, row, col+1, visited) + self.dfs(grid, row, col-1, visited)

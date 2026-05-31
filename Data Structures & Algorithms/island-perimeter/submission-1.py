class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        count = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]:
                    return self.dfs(grid, r, c, visited)


    def dfs(self, grid, r, c, visited):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0:
            return 1

        if (r,c) in visited:
            return 0


        visited.add((r,c))

        return self.dfs(grid, r+1, c, visited) + self.dfs(grid, r, c+1, visited) + self.dfs(grid, r-1, c, visited) + self.dfs(grid, r, c-1, visited)
            
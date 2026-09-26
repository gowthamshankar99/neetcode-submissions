class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        row_count = [0]*ROW
        col_count = [0]*COL

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1

        res = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    if row_count[r] > 1 or col_count[c] > 1:
                        res += 1

        return res
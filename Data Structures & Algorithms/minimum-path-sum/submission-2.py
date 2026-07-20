class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid)+1, len(grid[0])+1
        #res = [[0] * COL for _ in range(ROW)]
        res = [[float('inf')] * COL for _ in range(ROW)]
        res[0][1] = 0
        
        for r in range(1,ROW):
            for c in range(1,COL):
                res[r][c] = grid[r-1][c-1] + min(res[r-1][c], res[r][c-1])


        return res[ROW-1][COL-1]
        
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Creates a grid with m rows and n columns filled with 1s
        
        res = [[-1 for _ in range(n)] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                res[r][c] = -1

        for i in range(m):
            res[i][0] = 1
        
        for i in range(n):
            res[0][i] = 1

        for r in range(1, m):
            for c in range(1,n):
                res[r][c] = res[r-1][c] + res[r][c-1]

        return res[m-1][n-1]
        
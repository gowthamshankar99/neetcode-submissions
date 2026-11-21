class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ROW = len(word1)+1
        COL = len(word2)+1

        grid = [[0 for _ in range(COL)] for _ in range(ROW)]

        for i in range(ROW):
            grid[i][0] = i

        for i in range(COL):
            grid[0][i] = i


        for i in range(1, ROW):
            for j in range(1, COL):

                if word1[i-1] == word2[j-1]:
                    grid[i][j] = grid[i-1][j-1]

                else:
                    grid[i][j] = 1 + min(grid[i-1][j-1], grid[i-1][j], grid[i][j-1])

        
        return grid[ROW-1][COL-1]




        
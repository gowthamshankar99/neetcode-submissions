class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        ROW = len(obstacleGrid)
        COL = len(obstacleGrid[0])        
        res = [[0 for _ in range(COL)] for _ in range(ROW)]

        # where is the obstacle 

        for i in range(ROW):
            if obstacleGrid[i][0] == 1:
                break
            res[i][0] = 1
        
        for i in range(COL):
            if obstacleGrid[0][i] == 1:
                break            
            res[0][i] = 1

        
        for r in range(1,ROW):
            for c in range(1,COL):
                if obstacleGrid[r][c] == 1:
                    res[r][c] = 0
                else:
                    res[r][c] = res[r-1][c] + res[r][c-1]


        return res[ROW-1][COL-1]

                



        
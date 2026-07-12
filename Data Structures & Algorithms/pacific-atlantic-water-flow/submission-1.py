class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific, atlantic = set(),set()
        ROW = len(heights)
        COL = len(heights[0])

        # pacific 
        for c in range(COL):
            self.dfs(ROW, COL, 0, c, heights, pacific, heights[0][c])
            self.dfs(ROW, COL, ROW-1, c, heights, atlantic, heights[ROW-1][c])



        # atlantic 
        for r in range(ROW):
            self.dfs(ROW, COL, r, 0, heights, pacific, heights[r][0])
            self.dfs(ROW, COL, r, COL-1, heights, atlantic, heights[r][COL-1])

        res =  []
            
        # check for both of them 
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in atlantic and (r,c) in pacific:
                    res.append((r,c))

        return res
                    





    def dfs(self, ROW, COL, r, c, heights, visited, prev_height):

        if r < 0 or c < 0 or r >= ROW or c >= COL or (r,c) in visited or heights[r][c] < prev_height:
            return 

        visited.add((r,c))

        self.dfs(ROW, COL,r+1,c, heights, visited, heights[r][c])
        self.dfs(ROW, COL,r-1,c, heights, visited, heights[r][c])
        self.dfs(ROW, COL,r,c+1, heights, visited, heights[r][c])
        self.dfs(ROW, COL,r,c-1, heights, visited, heights[r][c])






        
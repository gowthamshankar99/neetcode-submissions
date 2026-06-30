from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh = 0
        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()
        time = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh +=1
                elif grid[r][c] == 2:
                    # rotten 
                    queue.append((r,c))
        
        directions = [(0,-1), (1,0), (-1,0), (0,1)]
        while queue and fresh > 0:
            time += 1
            size = len(queue)
            

            for i in range(size):
                r,c = queue.popleft()

                for dr, dc in directions:
                    nr,nc = r+dr, c+dc
                    if min(nr,nc) < 0 or nr == ROW or nc == COL:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            

        print(fresh)
        if fresh == 0:
            return time
        else:
            return -1









        

        
        
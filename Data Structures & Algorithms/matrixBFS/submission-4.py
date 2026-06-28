from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:

        ROW = len(grid)
        COL = len(grid[0])
        length = 0
        queue = deque([(0,0, length)])
        visited = set()
        visited.add((0,0))
        

        while queue:
            size = len(queue)
            for i in range(size):
                # pop the value from the queue 
                r,c, length = queue.popleft()
                if r == ROW - 1 and c == COL - 1:
                    return length

                neighbors = [(-1,0), (0,-1),(1,0), (0,1)]
                for dr, dc in neighbors:
                    nr, nc = r+dr, c+dc
                    if min(nr, nc) < 0 or nr == ROW or nc == COL or (nr,nc) in visited or grid[nr][nc] == 1:
                        continue
                    
                    queue.append((nr,nc, length+1))
                    visited.add((nr,nc))

            #length +=1

        return -1





        
        